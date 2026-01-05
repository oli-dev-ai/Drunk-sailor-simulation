import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()

#Array of sailor steps
sailor_steps = rng.standard_normal((1000,10))

#Cumulative steps
position = np.cumsum(sailor_steps, axis=0)

mean_pos = np.mean(position[-1])
print(mean_pos)

#Chart
plt.plot(position, label='sailor')
plt.axhline(y=0, color='k', linestyle='--')
plt.xlabel('steps')
plt.ylabel('position')
plt.title('10 Drunk sailors simulation - Gauss')
plt.show()


#print