import module_new 
from module_new import computation_port
import numpy as np 
import matplotlib.pyplot as plt

cp = ['AAPL', 'MSFT', 'NFLX', 'AMZN', 'GOOG']
d_s = [1,1,2018]
d_e = [1,1,2019]
n, mean, corr, stdev = computation_port(cp,d_s,d_e).comp_port()
print(n,mean,corr, stdev)

ar_std, ar_mean = computation_port(cp,d_s,d_e).random()[0:2]
ar_mean = np.array(ar_mean)
#ar_std = np.array(ar_std)
std_mini, mean_mini =computation_port(cp,d_s,d_e).minimum()
M = computation_port(cp,d_s,d_e).Market_portfolio()
std_cml, mean_cml = computation_port(cp,d_s,d_e).capital_market_line()

plt.figure(figsize=(10, 5))
plt.scatter(ar_std, ar_mean, c=ar_mean / ar_std, marker='o')
plt.plot(std_mini, mean_mini, 'r*',markersize=20, label='minimum')
plt.plot(M[0],M[1],'g*',markersize=15, label='Market portfolio')
plt.plot(std_cml, mean_cml, 'y-', markersize=2, label='CML')
plt.plot(stdev[0],mean[0],'r*', markersize=10, label='asset 1')
plt.plot(stdev[1],mean[1],'b*',markersize=10, label='asset 2')
plt.plot(stdev[2],mean[2],'b*',markersize=10, label='asset 3')
plt.plot(stdev[3],mean[3],'y*',markersize=10, label='asset 4')
plt.plot(stdev[4],mean[4],'g*',markersize=10, label='asset 5')
plt.grid(True)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio') 
plt.legend(loc='best')
plt.show()