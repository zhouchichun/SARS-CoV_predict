# SARS-CoV_predict
一个基于常微分方程组的感染者增长模型，没有估计参数
# 建模说明
- 状态和变量说明
    
     - t时刻状态为Xt
     - Xt=[infect,carry,health]，其中
      infect:感染发病人数；
      carry:携带但是不发病人数；
      health:健康人数；
     - VH：健康人群的病毒暴露程度；
     - rcarry：是携带者转为感染者的概率；
     - rdie：是感染者的死亡率；
     - rheal：是感染者治愈的概率；
     - rhealth：是健康人成为携带者的概率
     - 
   
- 状态转移情况和模型参数。
   
     - 

