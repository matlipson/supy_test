#%%
import supy as sp
from pathlib import Path


#%%
path_runcontrol = Path('./run_preston') / 'RunControl_preston.nml'
df_state_init = sp.init_supy(path_runcontrol)
grid = df_state_init.index[0]
df_forcing = sp.load_forcing_grid(path_runcontrol, grid)


#%%
df_output, df_state_final = sp.run_supy(
            df_forcing, df_state_init,
            save_state=False)


df = df_output.loc[(98),'SUEWS']