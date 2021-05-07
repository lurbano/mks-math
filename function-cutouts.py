import matplotlib.pyplot as plt
import math
import numpy

def func(x):
    return x**2

fname = 'x2'
datfile = f'funcCut-{fname}.txt'
outfile = f'funcCut-{fname}.png'
svgfile = f'funcCut-{fname}.svg'

x = []
y = []


with open(datfile, "w") as f:
    for t in numpy.arange(-10,10,0.1):
        x.append(t)
        # print(t, func(t))
        y.append(func(t))
        f.write(f'{x[-1]}, {y[-1]}\n')

plt.plot(x,y, color="green", linewidth="3")
plt.xlabel('time (sec.)')
plt.ylabel('Concentration: [HCl]')
plt.xlim(xmin=-10, xmax=10)
plt.ylim(ymin=-10, ymax=10)
plt.minorticks_on()
plt.grid(True, which="both", axis="y")
plt.grid(True, which="both", axis="x")

plt.savefig(outfile)
plt.savefig(svgfile)
plt.show()
