import mazino as m
import matplotlib.pyplot as plt
import numpy as np


H,V,visit=m.make_maze(10)

m.plot_maze(H,V)

pathx,pathy,attempts=m.find_path(0,0,7,7,H,V)
print(pathx,pathy,'\n','num. of attempts:',attempts)

x,y=pathx,[-i for i in pathy]
n=len(H)

plt.plot(np.add(x,[0.5 for i in range(np.size(x))]),
np.subtract(y,[0.5 for i in range(np.size(y))])+n,
color="r", linewidth=4);

plt.show()