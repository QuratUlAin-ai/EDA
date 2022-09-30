import matplotlib.pyplot as plt
from rwak import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)
plt.plot(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

plt.show()
   