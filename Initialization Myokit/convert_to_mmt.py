#%% Converting from cellml to mmt

import myokit.formats
i = myokit.formats.importer('cellml')
mod= i.model('./kernik-2019.cellml')
myokit.save('kernik.mmt', mod)

# %%
