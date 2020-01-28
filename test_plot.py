from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x, y = np.loadtxt('1.csv',
                unpack=True,
                delimiter=',')


plt.plot(x, y)

plt.title('lasertag_three_opponents_small')

plt.ylabel('Return')

plt.xlabel('Environment Frames')

plt.savefig('123.eps', format='eps')
# plt.show()