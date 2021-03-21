import matplotlib.pyplot as plt
import numpy as np

y1 = np.random.randn(100).cumsum()
y2= np.random.randn(100).cumsum()
fig,ax = plt.subplots(2,2,sharex = True, sharey=True)
ax[0,0].plot(y1)
ax[0,1].plot(y2)
plt.title("Datos random")
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")
fig = plt.figure()
ax = plt.axes()
plt.show()