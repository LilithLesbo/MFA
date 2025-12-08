

Dependencies originating from freeflux:
numpy
scipy


Installation method (macbook, apple sillicon)
Create a conda virtual environment running osx-64 to gain python 3.7 (last good build for the modules I'm using).
/Users/lilithflint/miniconda3/envs/py37
glpk has a stupid error that results in the program always timing out.
/Users/lilithflint/miniconda3/envs/py37/lib/python3.7/site-packages/pyomo/solvers/plugins/solvers/GLPK.py
line 140; replace 1 second timeout with 10 second. little guy just takes a while!

to install local freeflux, run
pip install /Users/lilithflint/Desktop/freeflux_bonus-optimizers/freeflux