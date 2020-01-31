
from scipy.integrate import odeint  
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

rcarry=0.6#病毒携带者致病率
rheal=0.1#感染者的治愈率
aca=0.9#携带者的活跃度
ain=0.3#感染者的活跃度
rhealth=0.4#正常人感染的概率
rdie=0.1#死亡率
init=[0,100,68000000]#初始条件
def VH(carry,infect,H0,H,aca,ain):
    return 0.5*(carry/H0+infect/H0)+0.5(1+(H/(carry*aca+infect*ain)))**(-1)

def equations(w, t, rcarry, rheal, aca,ain,rhealth,rdie):
    # w 是矢量，包含（infect, carry, health）, 五个参数 rcarry, rheal, aca,ain,rhealth
    # 计算微分量？
    infect, carry, health = w.tolist()
    # 返回量是lorenz的计算公式
    vh=VH(carry,infect,init[-1],health,aca,ain)
    return carry*rcarry-infect*rheal-infect*rdie, health*vh*rhealth-carry*rcarry, -health*vh*rhealth+infect*rheal


t = np.arange(0, 200, 0.02)  # 时间点
# 调用 ode 对 lorenz进行求解
track1 = odeint(equations, (0.2, 0.05, 0.75), t, args=(rcarry, rheal, aca,ain,rhealth,rdie))  # odeint,函数名后面的位置，是传入自定义函数的参数
#track2 = odeint(lorenz, (0.0, 1.01, 0.0), t, args=(10.0, 28.0, 3.0))
print(track1)
print(track1[:, 0])  # 取出第0列的意思，因为数组的每一行分别是 x,y,z; 取第0列就是把所有x取出来

# 画图
inf=plt.plot(track1[:,0])
car=plt.plot(track1[:,1])
hea=plt.plot(track1[:,2])

plt.legend(labels = ['infect',"carry",'health'], loc = 'best')

#fig = pl.figure()
#ax = Axes3D(fig)
#ax.plot(track1[:, 0], track1[:, 1], track1[:, 2], lw=1)
#ax.plot(track2[:, 0], track2[:, 1], track2[:, 2], lw=1)  # 用同一个ax,说明两幅图画在同一幅图
# 最后的show()不能忘
plt.show()
