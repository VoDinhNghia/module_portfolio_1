import numpy as np 
import matplotlib.pyplot as plt 
import module_portfolio_new
from module_portfolio_new import portfolio

n = 2
mean = [18, 24]
stdev = [3, 4.5]
corr = [0.5]
#trả về một list các array() mean12, mean13, mean14 , mean23, mean24, mean34
ar_mean = portfolio(n, mean, stdev, corr).compution_mean()
ar_stdev = portfolio(n, mean, stdev, corr).compution_stdev()
minimum_std, mean_mini_std = portfolio(n, mean, stdev, corr).minimum_risk()
std_f, mean_f = portfolio(n, mean, stdev, corr).frontier_eff()
print('minimum ',minimum_std)
plt.plot(ar_stdev, ar_mean, 'go', markersize=2)
plt.plot(std_f, mean_f, 'r-', markersize=10, label='frontier efficient') 
plt.plot(stdev[0],mean[0],'r*', markersize=10, label='asset 1')
plt.plot(stdev[1],mean[1],'b*',markersize=10, label='asset 2')
plt.plot(minimum_std, mean_mini_std, 'g*',markersize=15, label='minimun')
plt.xlabel('stdev')  
plt.ylabel('Expected return')  
plt.title('returns portfolios') 
plt.legend(loc='best')#phải plt.legend có label mới hiển thị
plt.show()
#xuất ra kết quả mean12

print("------------------------------------------------------")
print("------------------------------------3 assets-----------------------------------------------")
#trường hợp 3 assets
n = 3
mean = [20, 22, 24]
stdev = [4, 5, 4]
corr = [0.3, -0.1, 0.3]
ar_mean = portfolio(n, mean, stdev, corr).compution_mean()
ar_stdev = portfolio(n, mean, stdev, corr).compution_stdev()
minimum_std, mean_mini_std = portfolio(n, mean, stdev, corr).minimum_risk()
std_f, mean_f = portfolio(n, mean, stdev, corr).frontier_eff()
print('minimum ',minimum_std)


#print('mean_mini: ', min(ar_mean[ar_stdev.index(minimum_std)]))
plt.plot(ar_stdev[0], ar_mean[0], 'go', markersize=2)  
plt.plot(ar_stdev[1], ar_mean[1], 'go', markersize=2) 
plt.plot(ar_stdev[2], ar_mean[2], 'go', markersize=2) 
plt.plot(std_f, mean_f, 'r-', markersize=10, label='frontier efficient') 
plt.plot(stdev[0],mean[0],'r*', markersize=10, label='asset 1')
plt.plot(stdev[1],mean[1],'b*',markersize=10, label='asset 2')
plt.plot(stdev[2], mean[2],'y*',markersize=10, label='asset 3')
plt.plot(minimum_std, mean_mini_std, 'g*',markersize=15, label='minimun')
#plt.plot(min(minimum_std), min(ar_mean[ar_stdev.index(minimum_std)]),'r*',markersize=10, label='minimum')
plt.xlabel('stdev')  
plt.ylabel('Expected return')  
plt.title('returns portfolios') 
plt.legend(loc='best')#phải plt.legend có label mới hiển thị
plt.show()
print("------------------------------------4 assets-----------------------------------------------")
#trường hợp 4 assets
n = 4
mean = [20, 22, 24, 21]
stdev = [4, 3.5, 4, 6]
corr = [0.3, -0.1, 0.2, 0.3, 0.1, 0.2]
ar_mean = portfolio(n, mean, stdev, corr).compution_mean()
ar_stdev = portfolio(n, mean, stdev, corr).compution_stdev()
minimum_std, mean_mini_std = portfolio(n, mean, stdev, corr).minimum_risk()
std_f, mean_f = portfolio(n, mean, stdev, corr).frontier_eff()
print('minimum ',minimum_std)
plt.plot(ar_stdev[0], ar_mean[0], 'bo', markersize=2)  
plt.plot(ar_stdev[1], ar_mean[1], 'bo', markersize=2) 
plt.plot(ar_stdev[2], ar_mean[2], 'bo', markersize=2) 
plt.plot(ar_stdev[3], ar_mean[3], 'bo', markersize=2) 
plt.plot(ar_stdev[4], ar_mean[4], 'bo', markersize=2)
plt.plot(ar_stdev[5], ar_mean[5], 'bo', markersize=2)  
plt.plot(std_f, mean_f, 'r-', markersize=10, label='frontier efficient') 
plt.plot(stdev[0],mean[0],'r*', markersize=10, label='asset 1')
plt.plot(stdev[1],mean[1],'b*',markersize=10, label='asset 2')
plt.plot(stdev[2], mean[2],'y*',markersize=10, label='asset 3')
plt.plot(stdev[3], mean[3],'g*',markersize=10, label='asset 4')
plt.plot(minimum_std, mean_mini_std, 'g*',markersize=15, label='minimun')
#plt.plot(min(minimum_std), min(ar_mean[ar_stdev.index(minimum_std)]),'r*',markersize=10, label='minimum')
plt.xlabel('stdev')  
plt.ylabel('Expected return')  
plt.title('returns portfolios') 
plt.legend(loc='best')#phải plt.legend có label mới hiển thị
plt.show()
