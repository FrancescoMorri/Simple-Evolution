import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

graph = np.loadtxt("data.csv", delimiter=',')

food = graph[:, 0]
population = graph[:, 1]
mean_vis = graph[:, 2]
mean_spe = graph[:, 3]
mean_life = graph[:, 4]

fig = plt.figure(figsize=(18,8))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

gs = GridSpec(2, 3, figure=fig)

ax1 = fig.add_subplot(gs[:, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 1])
ax4 = fig.add_subplot(gs[:, 2])

ax1.plot(population, color='yellow', label='population')
ax1.plot(food, color='blue', label='food')
ax1.set_title('Population over time')
ax1.set_xlabel('Time Steps')
# ax1.set_ylabel('Population')
ax1.grid()
ax1.legend()

ax2.plot(mean_vis, color='green', label='Mean Vision', markersize=1.5)
ax2.text(0.45, 0.3, "Mean vision: %.3e" % (np.mean(mean_vis)),
        transform=ax2.transAxes, fontsize=8.5,
        verticalalignment='top', bbox=props)
ax2.set_title('Evolution of mean Vision')

ax2.set_ylabel('Vision')
ax2.grid()
ax2.legend()

ax3.plot(mean_spe, color='orange', label='Mean Speed', markersize=1.5)
ax3.text(0.45, 0.8, "Mean speed: %.3e" % (np.mean(mean_spe)),
        transform=ax3.transAxes, fontsize=8.5,
        verticalalignment='top', bbox=props)
ax3.set_title('Evolution of mean Speed')
ax3.set_xlabel('Time Steps')
ax3.set_ylabel('Speed')
ax3.grid()
ax3.legend()

ax4.plot(mean_life, color='red', label="Mean Life over Time")
ax4.text(0.55, 0.5, "Mean Life: %.3e" % (np.mean(mean_life)),
        transform=ax4.transAxes, fontsize=8.5,
        verticalalignment='top', bbox=props)
ax4.set_title('Evolution of life value')
ax4.set_ylabel('Mean Life')
ax4.set_xlabel('Time Steps')
ax4.grid()
ax4.legend()

plt.show()