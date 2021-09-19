from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from src.data_processing.filewriter import voltagePositionFiltered

xList = []
yList = []
zList = []
voltage = []


with open(voltagePositionFiltered, "r") as f:
    data = f.readlines()
    for line in data:
        posList = (
            line.strip("\n").replace("[", "").replace("]", "").split(", ")[0].split()
        )
        voltageList = line.strip("\n").split(", ")
        xList.append(float(posList[0]))
        yList.append(float(posList[1]))
        zList.append(float(posList[2]))
        voltage.append(float(posList[1]))

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(xList, yList, zList, c=voltage, cmap="viridis", linewidth=0.5)
plt.show()
