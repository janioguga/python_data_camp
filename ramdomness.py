# criando um dado (dice)
import numpy as np
np.random.seed(123)
print(np.random.randint(1, 7))
print(np.random.randint(1, 7))
print(np.random.randint(1, 7))
print(np.random.randint(1, 7))
# rolando os dados
import numpy as np
np.random.seed(123)
random_walk = [0]
for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)
    random_walk.append(step)
print(random_walk)
import matplotlib.pyplot as plt
plt.plot(random_walk)
plt.show()
#Cara e coroa usando random walk
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')
    print('Seu resultado é: ', outcomes)
#loteria
np.random.seed(123)
loteria = []
for x in range(100):
    random_loteria = [0]
    jogo = np.random.randint(0, 60)
    if jogo < 60:
        loteria = jogo + 3
    else:
        loteria = jogo - 3
    print(jogo)

import numpy as np
np.random.seed(123)
final_tails = []
for tails in range(100):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)

    final_tails.append(tails[-1])
    print(final_tails)

# Numpy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for random_walk in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)
np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw)

# Print all_walks
print(all_walks)
import matplotlib.pyplot as plt
plt.plot(all_walks)
plt.show()
plt.clf()
plt.plot(np_aw_t)
plt.show()


