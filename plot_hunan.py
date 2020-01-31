import matplotlib.pyplot as plt
data=[]
for line in open("hunan","r",encoding="utf-8"):
    data.append(float(line.strip().split("\t")[-1]))
plt.plot(data)
plt.show()