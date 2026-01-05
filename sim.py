import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()


#Array of sailor steps
sailor_steps = rng.integers(0, 2, size=1000)
sailor_steps[sailor_steps == 0] = -1

#Cumulative steps
position = np.cumsum(sailor_steps)
#Highest value
maximal_step = np.max(position)
#Lowest value
lowest_step = np.min(position)


#Chart
plt.plot(position, label='sailor')
plt.axhline(y=0, color='k', linestyle='--')
plt.xlabel('steps')
plt.ylabel('position')
plt.title('Drunk sailor simulation')
plt.show()

