import matplotlib 
matplotlib.use("TkAgg")
from matplotlib import pyplot

# 1: Prepare data
labels = ["iOS", "Android", "Web", "React Native"]
values = [150, 150, 400, 300]
colors = ["green", "red", "blue", "gold"]
explode = [0, 0, 0, 0.2]
# 2: plot
pyplot.pie(values, labels=labels, colors=colors, explode=explode)
pyplot.axis("equal")
# 3: Show
pyplot.show()

