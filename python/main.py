import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib
from food_functions import food_rand, central_column, islands
from blob import Blob
import numpy as np
import random

#matplotlib.rcParams['animation.embed_limit'] = 2**128


def animate(i):
    global blobbi, food, info
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    data_in = []
    mean_life = 0
    ax1.clear()
    ax2.clear()
    ax1.set(xlim=(0, 4), ylim=(0, 4))
    ax2.set(xlim=(0.01, 0.6), ylim=(0.0001, 0.2))
    for f in food:
        square = patches.Rectangle(f, 0.018, 0.018, color='black')
        ax1.add_patch(square)

    for b in blobbi:
        b.color_change()
        mean_life += b.LIFE
        # if the blob is alive
        if (b.steps < b.LIFE):
            check = b.food_check(food)  # check for food near him
            if (check):
                b.move()  # if no food is found, next move
            circle = patches.Circle((b.x, b.y), b.r, color=b.color)
            ax1.add_patch(circle)
            #ax1.annotate(str(b.generation), xy=(b.x, b.y), fontsize=8, ha="center", va='center', color='black')

        # else, if the blob is death
        elif (b.steps >= b.LIFE):
            if (b.fed != 0):  # check if it has eaten
                b.fed = 0
                b.steps = 0
            else:  # else kill him
                blobbi.remove(b)

        # checking if the blob can make a babyblob
        if (b.fed >= 3):
            b.steps += 1  # maybe too harsh?
            b.fed = 0
            nx = b.x + float(random.randint(-50, 50)/100)
            ny = b.y + float(random.randint(-50, 50)/100)
            blobbi.append(Blob(nx, ny, 0.05, heir=True, vis=b.VISION, spe=b.SPEED, old_life=b.LIFE))
            continue

        data_in.append((b.VISION, b.SPEED, b.color[0], b.color[1], b.color[2]))

    if (len(blobbi) == 0):
        mean_life = 0
    else:
        mean_life /= len(blobbi)

    #constantly add food at a certain rate
    for f in range(REFRESH):
        food.append((food_rand(0, 1)))

    ax1.set_title('Step %.d (%.d blob left; %.d food left)' % (i, len(blobbi), len(food)))

    ax2.set_title('Population')
    ax2.set_xlabel('VISION')
    ax2.set_ylabel('SPEED')
    data_np = np.array(data_in)
    xs = data_np[:, 0]
    ys = data_np[:, 1]
    colors = [(d[2], d[3], d[4]) for d in data_np]
    V_x = [0.1, 0.1]
    V_y = [0, 3]
    S_x = [0, 3]
    S_y = [0.08, 0.08]
    ax2.grid()
    ax2.plot(V_x, V_y, color='black', alpha=0.5, label='Starting Vision')
    ax2.plot(S_x, S_y, color='black', alpha=0.5, label='Starting Speed')
    ax2.text(0.61, 0.83, "Mean Life: %.3f" % (mean_life), transform=ax2.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
    ax2.scatter(xs, ys, color=colors, label='blobs')
    ax2.legend()

    info.append((len(food), len(blobbi), np.mean(xs), np.mean(ys), mean_life))

def initialize():
    FOOD = 200
    BLOBS = 50
    REFRESH = 5
    blobbi = []
    food = []
    info = []
    print("Insert the starting value of FOOD, BLOBS and REFRESH:")
    print("----------------------")
    print("Food--> ", end="")
    FOOD = int(input())
    print("----------------------")
    print("Blobs--> ", end="")
    BLOBS = int(input())
    print("----------------------")
    print("Refresh--> ", end="")
    REFRESH = int(input())
    for i in range(BLOBS):
        x = float(random.randint(0, 400)/100)
        y = float(random.randint(0, 400)/100)
        blobbi.append(Blob(x, y, 0.05))

    food = food_rand(FOOD, tp=0)

    return blobbi, food, info, REFRESH



blobbi, food, info, REFRESH = initialize()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,8))

anim = animation.FuncAnimation(fig, animate, interval=100, frames=500, blit=False, repeat=False)

np_info = np.array(info)
np.savetxt("data.csv", np_info, delimiter=',')

plt.show()
