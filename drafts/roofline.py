#Matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = [0.03125,0.06250,0.08330,0.12500,0.14125,0.16625,0.25000,0.50000,0.54000,0.60000,1.00000,2.00000,4.00000,5.99000,7.63000,8.00000,16.00000];
y = [0.30215,0.60430,0.80541,1.20860,1.36572,1.60744,2.41720,4.83440,5.22115,5.80128,9.66880,11.20000,11.20000,11.20000,11.20000,11.20000,11.20000];
plt.xscale('log',basex=2)
plt.yscale('log',basey=2)
plt.plot(x, y)

data_x = [11.69,1.4983]
data_y = [1.30,1.42100]
plt.plot(data_x, data_y, 'or')

plt.xlabel("Arithmetic Intensity")
plt.ylabel("Attainable GFLOPS")
plt.title("Roofline - IcoFOAM Hotspots on Sandybridge/Ivy Bridge Host Processor")
#labels = ['point{0}'.format(i) for i in range(3)]
plt.annotate('Amul()', xy=(11.69,1.30), xytext=(-20, 15),
textcoords = 'offset points', ha = 'right', va = 'bottom',
bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
arrowprops=dict(arrowstyle='->'))
plt.annotate('precondition()', xy=(1.49,1.421), xytext=(-20, 20),
textcoords = 'offset points', ha = 'right', va = 'bottom',
bbox = dict(boxstyle = 'round,pad=0.5', fc = 'blue', alpha = 0.5),
arrowprops=dict(arrowstyle='->'))
#plt.annotate('divergence_sphere=5.2', xy=(0.23,5.2), xytext=(40, 15),
#textcoords = 'offset points', ha = 'left', va = 'bottom',
#bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
#arrowprops=dict(arrowstyle='->'))
#plt.annotate('divergence_sphere_with_unroll=6.07', xy=(0.23,6.94), xytext=(40, 20),
#textcoords = 'offset points', ha = 'left', va = 'bottom',
#bbox = dict(boxstyle = 'round,pad=0.5', fc = 'blue', alpha = 0.5),
#arrowprops=dict(arrowstyle='->'))
#plt.subplots_adjust(bottom = 0.1)


plt.show()


