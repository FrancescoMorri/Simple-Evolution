import random
import numpy as np

def central_column(n_food, tp):
    '''
    tp = 0 -> Array
    tp = 1 -> coordinates
    '''
    if (tp == 0):
        foody = []
        for i in range(n_food):
            x = float(random.randint(100, 300)/100)
            y = float(random.randint(0, 400)/100)
            foody.append((x, y))
        return foody
    elif (tp == 1):
        x = float(random.randint(100, 300)/100)
        y = float(random.randint(0, 400)/100)
        return (x, y)


def islands(n_food, tp):
    '''
    tp = 0 -> Array
    tp = 1 -> coordinates
    '''
    if (tp == 0):   
        foody = []
        for i in range(int(n_food/2)):
            x = float(random.randint(0, 200)/100)
            y = float(random.randint(0, 200)/100)
            foody.append((x, y))
        for i in range(int(n_food/2)):
            x = float(random.randint(200, 400)/100)
            y = float(random.randint(200, 400)/100)
            foody.append((x, y))
        return foody
    elif (tp == 1):
        p = random.randint(0, 100)
        if (p <= 50):
            x = float(random.randint(0, 200)/100)
            y = float(random.randint(0, 200)/100)
        elif (p > 50):
            x = float(random.randint(200, 400)/100)
            y = float(random.randint(200, 400)/100)
        return (x, y)                       


def food_rand(n_food, tp):
    '''
    tp = 0 -> Array
    tp = 1 -> coordinates
    '''
    if (tp == 0):
        foody = []
        for i in range(n_food):
            x = float(random.randint(0, 400)/100)
            y = float(random.randint(0, 400)/100)
            foody.append((x, y))
        return foody
    elif (tp == 1):
        x = float(random.randint(0, 400)/100)
        y = float(random.randint(0, 400)/100)
        return (x, y)
