import matplotlib.pyplot as plt
import numpy as np
x_vals= np.linspace(0,6,100)
y1=11-2*x_vals
y2=(2*x_vals)/2
plt.plot(x_vals,y1,y2)
y3=np.minimum(y1,y2)
plt.xlim(0.5,5)
plt.fill_between(x_vals,0,y3,color="b")
plt.axvline(x=3,color="r")
plt.axhline(y=4,color="r")