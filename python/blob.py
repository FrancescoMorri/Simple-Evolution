import random
import numpy as np

class Blob(object):

    VISION = 0.1 # starting vision
    SPEED = 0.08 # starting speed
    LIFE = 13 # starting life

    color = 'cyan'
    fed = 0  # will became true if it is fed
    steps = 0  # when it is == 9 the blob has finished its energy
    mov_prob = [0, 0, 0, 0]  # the prob with which the blob moves
    vision = 0

    def __init__(self, x, y, radius, heir=False, vis=0.1, spe=0.05, old_life=12):
        """
        Initialization of the blob:
        x = position x
        y = position y
        radius = radius
        It randomizes the probabilities of moving.
        If it is not the first generation the newborn will have a VISION and SPEED possibly different from the parent.
        """
        # self.generation = gen
        self.x = x
        self.y = y
        self.r = radius

        if heir:  # change in the heritage
            self.VISION = vis
            self.SPEED = spe

            # Change in SPEED
            p = random.randint(0, 100)
            if (p < 75):
                pass
            else:
                gen = float(random.randint(-250, 250)/10000.)  # 50% of the basic speed
                new_speed = self.SPEED + gen
                new_speed = max(0.0001, new_speed)
                self.SPEED = min(new_speed, 0.3)

            # Change in VISION
            p = random.randint(0, 100)
            if (p < 75):
                pass
            else:
                gen = float(random.randint(-500, 500)/10000.)  # 50% of the basic vision
                new_vision = self.VISION + gen
                new_vision = max(0.001, new_vision)
                self.VISION = min(new_vision, 0.6)

        # Moving Probabilities normalized
        for i in range(len(self.mov_prob)):
            self.mov_prob[i] = float(random.randint(0, 100)/100)
        s = sum(self.mov_prob)
        for i in range(len(self.mov_prob)):
            self.mov_prob[i] /= s

        # Life Calculator
        '''
        if (self.SPEED - spe > 0.005):
            self.LIFE = old_life - 1
        elif (self.SPEED - spe < -0.005):
            self.LIFE = old_life + 1

        if (self.VISION - vis > 0.025):
            self.LIFE = old_life - 1
        elif (self.VISION - vis < -0.025):
            self.LIFE = old_life + 1
        '''
        self.LIFE = 16 - (int((self.SPEED * 100)/2) + int(self.VISION * 10))


    def move(self):
        '''
        It just move the blob using its probabilities.
        '''
        p = float(random.randint(0, 100)/100)
        m = 0.05
        if (p < self.mov_prob[0]):  # moving right
            nx = (self.x + m) % 4.
            ny = self.y
        elif (p > self.mov_prob[0] and p < (self.mov_prob[0] + self.mov_prob[1])):  # moving left
            nx = (self.x - m) % 4.
            ny = self.y
        elif (p > (self.mov_prob[0] + self.mov_prob[1]) and p < (self.mov_prob[0] + self.mov_prob[1] + self.mov_prob[2])):  # moving up
            nx = self.x
            ny = (self.y + m) % 4.
        else:  # moving down
            nx = self.x
            ny = (self.y - m) % 4.
        self.x = nx
        self.y = ny
        self.steps += 1

    def food_check(self, food_map):
        '''
        Check in a circle of radius VISION if there is any food, if there is it moves there, else it just use its basic motion.
        '''
        for f in food_map:
            d = np.sqrt(((f[0]-self.x)**2 + (f[1]-self.y)**2))
            if (d <= self.VISION):
                self.x = f[0]
                self.y = f[1]
                self.steps += 1
                self.fed += 1
                food_map.remove(f)
                return False
        return True

    def color_change(self):
        '''
        The color of the blobs depends on their attributes.
        '''
        r = np.interp(self.VISION, [0.01, 0.6], [0, 1])
        b = np.interp(self.SPEED, [0.0001, 0.2], [0, 1])
        g = 0.
        self.color = (r, g, b)
