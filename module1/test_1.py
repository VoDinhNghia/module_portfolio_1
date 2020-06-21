import numpy as np 
import matplotlib.pyplot as plt
import module_portfolio_new_1
from module_portfolio_new_1 import portfolio, portfolio_n_assets, computation_mean

a = [[1,6,2],[4,7,16],[7,2,9]]
n, mean_exp, std_exp, corr, cov = computation_mean(a).compu_mean()

print(corr)

ar_std, ar_mean, w = computation_mean(a).compu_port()
std_mini, mean_mini = computation_mean(a).minimum_std()
M = computation_mean(a).market_port()
std_cml, mean_cml = computation_mean(a).CML_port()

plt.figure(figsize=(10, 5))
plt.scatter(ar_std, ar_mean, c=ar_mean / ar_std, marker='o')
plt.plot(std_mini, mean_mini, 'r*',markersize=20, label='minimum')
plt.plot(M[0],M[1],'g*',markersize=20, label='Market portfolio')
plt.plot(std_cml, mean_cml, 'y-', markersize=2, label='CML')
plt.plot(std_exp[0],mean_exp[0],'g*', markersize=15, label='asset 1')
plt.plot(std_exp[1],mean_exp[1],'b*', markersize=15, label='asset 2')
plt.plot(std_exp[2],mean_exp[2],'r*', markersize=15, label='asset 3')
plt.grid(True)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='ratio mean/stdev') 
plt.legend(loc='best')#phải plt.legend có label mới hiển thị
plt.show()
