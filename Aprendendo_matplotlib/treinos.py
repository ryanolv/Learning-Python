from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = (11,7)

x = [1,2,3,4,5,6,7,8,9,10]
y = [11,12,13,14,15,16,17,18,19,20]


fig, ax = plt.subplots()
ax.bar(x, y)
ax.annotate("Maior valor",
            xy=(10, 12),
            xycoords='data',
            xytext=(11, 10),
            textcoords='data',
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
plt.show()