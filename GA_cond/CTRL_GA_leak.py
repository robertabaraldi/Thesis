#%%
import random
from math import log10
import matplotlib.pyplot as plt
from scipy.signal import find_peaks 
import seaborn as sns 
from multiprocessing import Pool
import numpy as np
import pandas as pd

from deap import base, creator, tools 
import myokit

#%%
class Ga_Config():
    def __init__(self,
             population_size,
             max_generations,
             params_lower_bound,
             params_upper_bound,
             tunable_parameters,
             mate_probability,
             mutate_probability,
             gene_swap_probability,
             gene_mutation_probability,
             tournament_size,
             cost,
             feature_targets):
        self.population_size = population_size
        self.max_generations = max_generations
        self.params_lower_bound = params_lower_bound
        self.params_upper_bound = params_upper_bound
        self.tunable_parameters = tunable_parameters
        self.mate_probability = mate_probability
        self.mutate_probability = mutate_probability
        self.gene_swap_probability = gene_swap_probability
        self.gene_mutation_probability = gene_mutation_probability
        self.tournament_size = tournament_size
        self.cost = cost
        self.feature_targets = feature_targets

#%%
def run_ga(toolbox):
    """
    Runs an instance of the genetic algorithm.

    Returns
    -------
        final_population : List[Individuals]
    """
    print('Evaluating initial population.')

    # 3. Calls _initialize_individuals and returns initial population
    population = toolbox.population(GA_CONFIG.population_size)

    # 4. Calls _evaluate_fitness on every individual in the population
    fitnesses = toolbox.map(toolbox.evaluate, population)
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = (fit,)
    # Note: visualize individual fitnesses with: population[0].fitness
    gen_fitnesses = [ind.fitness.values[0] for ind in population]

    avg_fit= np.mean(gen_fitnesses)
    best_fit= np.min(gen_fitnesses)

    print(f'\tAvg fitness is: {avg_fit}')
    print(f'\tBest fitness is {best_fit}')

    avg=[] 
    best=[]
    gen=[]

    # Store initial population details for result processing.
    final_population = [population]

    # Individuals Excel
    tempdata = [i[0] for i in population]
    df_data = pd.DataFrame(tempdata)
    df_error = pd.DataFrame(gen_fitnesses, columns=["Error"])
    df = df_data.join(df_error, how="outer")

    for generation in range(1, GA_CONFIG.max_generations):
        print('Generation {}'.format(generation))
        # Offspring are chosen through tournament selection. They are then
        # cloned, because they will be modified in-place later on.
        gen.append(generation)

        # 5. DEAP selects the individuals 
        selected_offspring = toolbox.select(population, len(population))

        offspring = [toolbox.clone(i) for i in selected_offspring]

        # 6. Mate the individualse by calling _mate()
        for i_one, i_two in zip(offspring[::2], offspring[1::2]):
            if random.random() < GA_CONFIG.mate_probability:
                toolbox.mate(i_one, i_two)
                del i_one.fitness.values
                del i_two.fitness.values

        # 7. Mutate the individualse by calling _mutate()
        for i in offspring:
            if random.random() < GA_CONFIG.mutate_probability:
                toolbox.mutate(i)
                del i.fitness.values

        # All individuals who were updated, either through crossover or
        # mutation, will be re-evaluated.

        # 8. Evaluating the offspring of the current generation
        updated_individuals = [i for i in offspring if not i.fitness.values]
        fitnesses = toolbox.map(toolbox.evaluate, updated_individuals)
        for ind, fit in zip(updated_individuals, fitnesses):
            ind.fitness.values = (fit,)

        population = offspring

        gen_fitnesses = [ind.fitness.values[0] for ind in population]

        avg_fit= np.mean(gen_fitnesses)
        best_fit= np.min(gen_fitnesses)

        print(f'\tAvg fitness is: {avg_fit}')
        print(f'\tBest fitness is {best_fit}')

        # Individuals Excel
        tempdata = [i[0] for i in population]
        df_data = pd.DataFrame(tempdata)
        df_error = pd.DataFrame(gen_fitnesses, columns=["Error"])
        df1 = df_data.join(df_error, how="outer")
        df = pd.concat([df, df1])

        final_population.append(population)
 
        avg.append(avg_fit)
        best.append(best_fit)
    
    # Average and Best Errors in Excel file
    df_avg_err = pd.DataFrame(avg, columns=["Avg Error"])
    df_best_err = pd.DataFrame(best, columns=["Best Error"])
    dfe = df_avg_err.join(df_best_err, how="outer")
    dfe.to_excel('Errors.xlsx', sheet_name='Sheet1', index=False)
    
    # Individuals in Excel file
    df.to_excel('Individuals.xlsx', sheet_name='Sheet1',index=False)
    
    #plt.plot(gen, avg, '*m', label= 'Avg')
    plt.plot(gen, best, '*b', label= 'Best')
    plt.legend()
    plt.xlabel('Generations',fontsize=14)
    plt.ylabel('Errors', fontsize=14)
    plt.savefig('Errors.png')
    plt.show()
    
    return final_population

#%%
def _initialize_individuals():
    """
    Creates the initial population of individuals. The initial 
    population 

    Returns:
        An Individual with conductance parameters 
    """
    # Builds a list of parameters using random upper and lower bounds.
    lower_exp = log10(GA_CONFIG.params_lower_bound)
    upper_exp = log10(GA_CONFIG.params_upper_bound)
    initial_params = [10**random.uniform(lower_exp, upper_exp)
                      for i in range(0, len(
                          GA_CONFIG.tunable_parameters))]

    keys = [val for val in GA_CONFIG.tunable_parameters]
    return dict(zip(keys, initial_params))

#%%
def _evaluate_fitness(ind):
    """
    Calls cost functions and adds costs together

    Returns
    -------
        fitness : number 
    """
    feature_error = get_feature_errors(ind)

    # Returns 
    if feature_error == 500000:
        return feature_error

    fitness = feature_error

    return fitness

#%%
def _mate(i_one, i_two):
    """Performs crossover between two individuals.

    There may be a possibility no parameters are swapped. This probability
    is controlled by `GA_CONFIG.gene_swap_probability`. Modifies
    both individuals in-place.

    Args:
        i_one: An individual in a population.
        i_two: Another individual in the population.
    """
    for key, val in i_one[0].items():
        if random.random() < GA_CONFIG.gene_swap_probability:
            i_one[0][key],\
                i_two[0][key] = (
                    i_two[0][key],
                    i_one[0][key])

#%%
def _mutate(individual):
    """Performs a mutation on an individual in the population.

    Chooses random parameter values from the normal distribution centered
    around each of the original parameter values. Modifies individual
    in-place.

    Args:
        individual: An individual to be mutated.
    """
    keys = [k for k, v in individual[0].items()]

    for key in keys:
        if random.random() < GA_CONFIG.gene_mutation_probability:
            new_param = -1

            while ((new_param < GA_CONFIG.params_lower_bound) or
                   (new_param > GA_CONFIG.params_upper_bound)):
                new_param = np.random.normal(
                        individual[0][key],
                        individual[0][key] * .1)

            individual[0][key] = new_param

#%%
def get_feature_errors(ind):
    """
    Compares the simulation data for an individual to the HCM values. The returned error value is a sum of the differences between the individual and HCM values.

    Returns
    ------
        error
    """
    ap_features = {}
    t, v, cai, i_ion = get_normal_sim_dat(ind)

    # Returns really large error value if cell AP is not valid 
    if ((min(v) > -60) or (max(v) < 0)):
        return 500000 
    
    # Voltage/APD features#######################
    mdp = min(v)
    max_p = max(v)
    max_p_idx = np.argmax(v)
    apa = max_p - mdp
    dvdt_max = np.max(np.diff(v[0:30])/np.diff(t[0:30]))

    ap_features['dvdt_max'] = dvdt_max
    peak_v = find_peaks(v, distance=100)
    peak = v[peak_v[0][0]]
    ap_features['peak'] = peak
    ap_features['apa']= apa

    for apd_pct in [50, 90]:
        repol_pot = max_p - apa * apd_pct/100
        idx_apd = np.argmin(np.abs(v[max_p_idx:] - repol_pot))
        apd_val = t[idx_apd+max_p_idx]

        ap_features[f'apd{apd_pct}'] = apd_val

    ap_features['mdp']= mdp
 
    error = 0
    err = {}

    if GA_CONFIG.cost == 'function_1':
        for k, v in ap_features.items():
            error += (GA_CONFIG.feature_targets[k][1] - v)**2
            err[f'{k}'] = error
    else:
        for k, v in ap_features.items():
            if ((v < GA_CONFIG.feature_targets[k][0]) or
                    (v > GA_CONFIG.feature_targets[k][2])):
                error += 1000 

    # Parameters Errors in Excel file
    tempdata = [err]
    df_data = pd.DataFrame(tempdata)
    df_data.to_excel('Parameters_Errors.xlsx', sheet_name='Sheet1',index=False)

    # Features
    f = [ap_features]
    df1_data = pd.DataFrame(f)
    df1_data.to_excel('Features.xlsx', sheet_name='Sheet1',index=False)

    return error

#%%
def get_normal_sim_dat(ind):
    """
        Runs simulation for a given individual. If the individuals is None,
        then it will run the HCM model

        Returns
        ------
            t, v, cai, i_ion
    """
    mod, proto, x = myokit.load('./kernik_leak_fixed.mmt')
    if ind is not None:
        for k, v in ind[0].items():
            k1, k2 = k.split('.')
            mod[k1][k2].set_rhs(v)
    else:
        mod['membrane']['gLeak'].set_rhs(0.2)

    proto.schedule(4, 10, 1, 1000, 0)
    
    sim = myokit.Simulation(mod, proto)
    sim.pre(1000 * 100) #pre-pace for 100 beats
    dat = sim.run(50000) # set time in ms

    # Get t, v, and cai for second to last AP#######################
    i_stim = dat['stimulus.i_stim']
    peaks = find_peaks(-np.array(i_stim), distance=100)[0]
    start_ap = peaks[-3] 
    end_ap = peaks[-2]

    t = np.array(dat['engine.time'][start_ap:end_ap])
    t = t - t[0]
    max_idx = np.argmin(np.abs(t-900))
    t_leak = t[0:max_idx]
    end_ap = start_ap + max_idx

    v_leak = np.array(dat['membrane.V'][start_ap:end_ap])
    cai = np.array(dat['cai.Cai'][start_ap:end_ap])
    i_ion = np.array(dat['membrane.i_ion'][start_ap:end_ap])

    peak_v = find_peaks(-v_leak, height=0, distance=100)

    if len(peak_v[0])>1:
        first_peak = peak_v[0][0] #first is to choose between the peaks and the peak_height, then to choose the first peak
        t_leak = t_leak[0:first_peak]
        n_array = 1000 - t[first_peak] #compute time needed to arrive to 1000ms after end of AP
        t_array = np.array([i+1 for i in range(int(t[first_peak]),1000)])
        v_leak = v_leak[0:first_peak]
        last_v = v_leak[-1] #last potential value
        v_array = np.full(int(n_array+1),last_v)

        v_leak = np.concatenate((v_leak, v_array))
        t_leak = np.concatenate((t_leak, t_array))

    return (t_leak, v_leak, cai, i_ion)

#%%
def plot_generation(inds,
                    gen=None,
                    is_top_ten=True,
                    lower_bound=.1,
                    upper_bound=10):
    if gen is None:
        gen = len(inds) - 1

    pop = inds[gen]

    pop.sort(key=lambda x: x.fitness.values[0])
    best_ind = pop[0]

    if is_top_ten:
        pop = pop[0:10]

    keys = [k for k in pop[0][0].keys()]
    empty_arrs = [[] for i in range(len(keys))]
    all_ind_dict = dict(zip(keys, empty_arrs))

    fitnesses = []

    for ind in pop:
        for k, v in ind[0].items():
            all_ind_dict[k].append(v)

        fitnesses.append(ind.fitness.values[0])

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    for ax in axs:
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

    curr_x = 0

    for k, conds in all_ind_dict.items():
        for i, g in enumerate(conds):
            g = log10(g)
            x = curr_x + np.random.normal(0, .01)
            g_val = 1 - fitnesses[i] / max(fitnesses)
            axs[0].scatter(x, g, color=(0, g_val, 0))
            #if i < 10:
            #    axs[0].scatter(x-.1, g, color='r')


        curr_x += 1
    # curr_x -> variable in order to shift by 1 on the graph
    # in order to distinguish between conductances

    curr_x = 0

    axs[0].hlines(0, -.5, (len(keys)-.5), colors='grey', linestyle='--')
    axs[0].set_xticks([i for i in range(0, len(keys))])
    axs[0].set_xticklabels(['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak','GbNa','GbCa','GNak'], fontsize=10)
    axs[0].set_ylim(log10(lower_bound), 
                    log10(upper_bound))
    axs[0].set_ylabel('Log10 Conductance', fontsize=14)

    t, v, cai, i_ion = get_normal_sim_dat(best_ind)
    axs[1].plot(t, v, 'b--', label='HCM')

    t, v, cai, i_ion = get_normal_sim_dat(None)
    axs[1].plot(t, v, 'k', label='Kernik')

    axs[1].set_ylabel('Voltage (mV)', fontsize=14)
    axs[1].set_xlabel('Time (ms)', fontsize=14)

    axs[1].legend()

    fig.suptitle(f'Generation {gen+1}', fontsize=14)
    fig.savefig(f'Model_{gen+1}Gen_.png')

    plt.show()

    # Best Individuals Excel
    tempdata = best_ind
    df = pd.DataFrame(tempdata)
    df.to_excel('Best_ind.xlsx', sheet_name='Sheet1', index=False)

#%%
def start_ga(pop_size=100, max_generations=20):
    feature_targets  =     {'dvdt_max': [6.72, 7.15, 7.58],
                             'peak': [21.4, 24.1, 26.8],
                             'apa': [73.6, 79.68, 85.76],
                             'apd50': [351.05, 450.22, 549.39],
                             'apd90': [510.19, 564.82, 619.45],
                             'mdp': [-60.65, -58.44, -56.23],
                            }

    # 1. Initializing GA hyperparameters
    global GA_CONFIG
    GA_CONFIG = Ga_Config(population_size=pop_size,
                          max_generations=max_generations,
                          params_lower_bound=0.1,
                          params_upper_bound=10,
                          tunable_parameters=['iks.g_scale',
                                              'ical.g_scale',
                                              'ikr.g_scale',
                                              'ina.g_scale',
                                              'ito.g_scale',
                                              'ik1.g_scale',
                                              'ifunny.g_scale',
                                              'membrane.gLeak',
                                              'ibna.g_scale',
                                              'ibca.g_scale',
                                              'inak.g_scale'],
                          mate_probability=0.9,
                          mutate_probability=0.9,
                          gene_swap_probability=0.2,
                          gene_mutation_probability=0.2,
                          tournament_size=2,
                          cost='function_1',
                          feature_targets=feature_targets)

    creator.create('FitnessMin', base.Fitness, weights=(-1.0,))

    creator.create('Individual', list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register('init_param',
                     _initialize_individuals)
    toolbox.register('individual',
                     tools.initRepeat,
                     creator.Individual,
                     toolbox.init_param,
                     n=1)
    toolbox.register('population',
                     tools.initRepeat,
                     list,
                     toolbox.individual)

    toolbox.register('evaluate', _evaluate_fitness)
    toolbox.register('select',
                     tools.selTournament,
                     tournsize=GA_CONFIG.tournament_size)
    toolbox.register('mate', _mate)
    toolbox.register('mutate', _mutate)

    # To speed things up with multi-threading
    p = Pool()
    toolbox.register("map", p.map)

    # 2. Calling the GA to run
    final_population = run_ga(toolbox)

    return final_population

# Final population includes list of individuals from each generation
# To access an individual from last gen:
# final_population[-1][0].fitness.values[0] Gives you fitness/error
# final_population[-1][0][0] Gives you dictionary with conductance values

#%%
def main():
    all_individuals = start_ga()

    plot_generation(all_individuals, gen=None, is_top_ten=False)

if __name__ == '__main__':
    main()

# %%