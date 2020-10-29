import numpy as np
import matplotlib.pyplot as plt

h = plt.figure()
ha = h.add_subplot(1, 1, 1)
x = np.arange(0, 20, 0.01)
y = np.sin(x) * np.exp(-x / 10)
hp, = ha.plot(x, y)
ha.set_xlabel("x")
ha.set_ylabel("y")
ht = ha.set_title("f($x$) = sin($x$)e$^{-x/10}$")

hp.set_linestyle("--")
hp.set_color("g")
hp.set_linewidth(3)
ha.set_ylim(ymin=-1.5, ymax=1.5)
ht.set_fontsize(15)
ha.set_axis_off()

hb, = ha.plot(x[0], y[0], "ko")
hb.set_markersize(8)
htxt = ha.text(x[0] + 0.05, y[0] + 0.05, str(round(y[0], 3)))
for i in range(1, len(x)):
    hb.set_xdata(x[i])
    hb.set_ydata(y[i])
    htxt.set_position([x[i] + 0.05, y[i] + 0.05])
    htxt.set_text(str(round(y[i], 3)))
    if y[i] >= 0:
        hb.set_markerfacecolor("b")
        hb.set_markeredgecolor("b")
        htxt.set_color("b")
    else:
        hb.set_markerfacecolor("r")
        hb.set_markeredgecolor("r")
        htxt.set_color("r")
    plt.pause(0)
