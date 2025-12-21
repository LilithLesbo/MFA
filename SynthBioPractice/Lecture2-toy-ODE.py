
import matplotlib.pyplot as plt
from scipy import integrate

"""
Vaguely doing the michealis menten example scenario

S + E <-> ES -> P

No assumptions made!
"""
def ODE_function(t, y):
    """
    System of ODEs to be solved by another function.
    Representing y and dYdT as [S], [E], [ES], [P] vectors.
    """
    # set rate constants
    k1 = 4000
    k1rev = 25
    k2 = 15
    #shang
    # initialise output vector
    dYdT = [0, 0, 0, 0]

    # encode ODEs from law of mass action
    dYdT[0] = k1rev*y[2] - k1*y[0]*y[1] #[S]
    dYdT[1] = k2*y[2] + k1rev*y[2] - k1*y[0]*y[1] #[E]
    dYdT[2] = -k2*y[2] + -k1rev*y[2] + k1*y[0]*y[1] #[ES]
    dYdT[3] = k2*y[2] #[P]

    return dYdT



S0 = 0.01 # initial substrate concentration, M
E0 = 0.001 # initial enzyme concentration, M
tf = 10 # final time point, s
# rates will be in M/s

y0 = [S0, E0, 0, 0] #initial concentration vector

sol = integrate.solve_ivp(ODE_function, (0, tf), y0)

labels = ["S", "E", "ES", "P"]

for i in range(sol.y.shape[0]):
    plt.plot(sol.t, sol.y[i], label=f'${labels[i]}(t)$')

#plt.plot(sol.t, (sol.y[1]+sol.y[2]), label=f'$E0(t)$')

plt.xlabel('$t$') # the horizontal axis represents the time
plt.ylabel('$conc$') # vertical axis represents concentration
plt.legend() # show how the colors correspond to the components of X
plt.show()