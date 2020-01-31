
from scipy.integrate import odeint  
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


#first
rcarry=0.9  #病毒携带者致病率
rheal=0.10   #感染者的治愈率
aca=500     #携带者的活跃度
ain=300    #感染者的活跃度
rhealth=0.6 #正常人感染的概率
rdie=0.01    #死亡率
#rrecover=0.5
ini=(0,4,68000000)#湖南有68000000人，武汉涌入湖南约20万人，携带者4000
num=0
num1=300

def VH(carry,infect,H0,health,aca,ain):
    return (0.05*(carry*0.1/H0+infect*0.01/H0)+0.05*(1+(health/(carry*aca+infect*ain)))**(-1))

def equations(w, t, rcarry, rheal, aca,ain,rhealth,rdie):
    infect, carry, health = w.tolist()
    H0=ini[-1]
    vh=VH(carry,infect,ini[-1],health,aca,ain)
    #return carry*rcarry-infect*rheal-infect*rdie, health*(0.5*(carry/H0+infect/H0)+0.5*(1+(health/(carry*aca+infect*ain)))**(-1))*rhealth-carry*rcarry, -health*(0.5*(carry/H0+infect/H0)+0.5*(1+(health/(carry*aca+infect*ain)))**(-1))*rhealth+infect*rheal
    return carry*rcarry-infect*rheal-infect*rdie, health*vh*rhealth-carry*rcarry, -health*vh*rhealth+infect*rheal


t = np.arange(0, 200, 0.02)  # 时间点
track1 = odeint(equations, ini, t, args=(rcarry, rheal, aca,ain,rhealth,rdie))  # odeint,函数名后面的位置，是传入自定义函数的参数

inf_lst=track1[:,0]
car_lst=track1[:,1]
hea_lst=track1[:,2]
acc=0
for ind,h in enumerate(inf_lst):
    if h >=150:
        num=ind
        break

print(num)
inf_lst=list(inf_lst[:num])
car_lst=list(car_lst[:num])
hea_lst=list(hea_lst[:num])

#second
aca=aca/30
ain=0.01
ini=(inf_lst[-1],car_lst[-1],hea_lst[-1])


t=np.arange(0, 200, 0.02)  # 时间点
track2 = odeint(equations, ini, t, args=(rcarry, rheal, aca,ain,rhealth,rdie))  # o
inf_lst+=list(track2[:,0])
car_lst+=list(track2[:,1])
hea_lst+=list(track2[:,2])

inf=plt.plot(inf_lst[:num])
#car=plt.plot(car_lst[:num])
#hea=plt.plot(hea_lst[:num])
plt.legend(labels = ['infect'], loc = 'best')
#plt.legend(labels = ['infect',"carry"], loc = 'best')
plt.show()

inf=plt.plot(inf_lst[:5*num])
#car=plt.plot(car_lst[:500*num])
#hea=plt.plot(hea_lst[:5*num])
plt.legend(labels = ['infect'], loc = 'best')
#plt.legend(labels = ['infect',"carry"], loc = 'best')
plt.show()
