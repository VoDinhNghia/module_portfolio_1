import numpy as np 
import matplotlib.pyplot as plt 
import module_portfolio_new
from module_portfolio_new import portfolio

n = 2
mean = [20, 22]
stdev = [4, 5]
corr = [0.3]
#trả về một list các array() mean12, mean13, mean14 , mean23, mean24, mean34
ar_mean = portfolio(n, mean, stdev, corr).compution_mean()
ar_stdev = portfolio(n, mean, stdev, corr).compution_stdev()
#xuất ra kết quả mean12
print(ar_mean)
print("-------stdev-------")
print(ar_stdev)
print("------------------------------------------------------")
print("------------------------------------3 assets-----------------------------------------------")
#trường hợp 3 assets
n = 3
mean = [20, 22, 24]
stdev = [4, 5, 4]
corr = [0.3, -0.1, 0.3]
ar_mean = portfolio(n, mean, stdev, corr).compution_mean()
ar_stdev = portfolio(n, mean, stdev, corr).compution_stdev()
plt.plot(ar_stdev[0], ar_mean[0], 'go', markersize=2)  
plt.plot(ar_stdev[1], ar_mean[1], 'ro', markersize=2) 
plt.plot(ar_stdev[2], ar_mean[2], 'bo', markersize=2) 
plt.plot(stdev[0],mean[0],'r*', markersize=10, label='asset 1')
plt.plot(stdev[1],mean[1],'b*',markersize=10, label='asset 2')
plt.plot(stdev[2], mean[2],'y*',markersize=10, label='asset 3')
plt.xlabel('stdev')  
plt.ylabel('Expected return')  
plt.title('returns portfolios') 
plt.legend(loc='best')#phải plt.legend có label mới hiển thị
plt.show()
""" print("------------------------------------4 assets-----------------------------------------------")
#trường hợp 4 assets
n = 4
mean = [20, 22, 24, 26]
stdev = [4, 5, 4, 6]
corr = [0.3, -0.1, 0.2, 0.3, 0.1, 0.2]
ar_mean = portfolio(n, mean, stdev, corr).compution_mean()
print(ar_mean) """