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
   
     - 方程建立说明
     
     ![avatar](https://github.com/zhouchichun/SARS-CoV_predict/blob/master/%E5%BB%BA%E6%A8%A1%E8%AF%B4%E6%98%8E.png)
     - 其中模型直观解释图像如下
     
     
     ![avatar](https://github.com/zhouchichun/SARS-CoV_predict/blob/master/simple_model_def.png)
     ![avatar](https://github.com/zhouchichun/SARS-CoV_predict/blob/master/simple_model_view1.png)

# 运行

  - 直接修改 main.py 中参数取值和常微分方程组
  
  -  运行 python3 main.py 得到感染者数量序列图像
# 参数估计
   目前只是自己手动估计参数，根据每个省市的实际感染者序列，可以估计出各个参数的值
