from neuron import h
from neuron.units import ms, mV, µm
import matplotlib.pyplot as plt

x = plt.scatter([1,2,3],[1,2,3])
plt.show()

h.load_file('stdrun.hoc')

class BallAndStick:
    def __init__(self, gid):
        self._gid = gid
        self.soma = h.Section(name="soma", cell=self)
        self.dend = h.Section(name="dend", cell=self)
        self.dend.connect(self.soma)
        self.soma.L = self.soma.diam = 12.6157 * µm
        self.dend.L = 200 * µm
        self.dend.diam = 1 * µm
    def __repr__(self):
        return "BallAndStick[{}]".format(self._gid)


# my_cell = BallAndStick(0)

# my_cell = BallAndStick(0)
my_cell = BallAndStick(0)
my_cell.soma(0.5).area()
# my_other_cell = BallAndStick(1)
h.topology()

# del my_other_cell

h.PlotShape(False).plot(plt)


print(h.units('gnabar_hh'))
h.PlotShape(False).plot()

h.PlotShape(True).plot(plt)