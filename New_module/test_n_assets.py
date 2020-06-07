import numpy as np 
import matplotlib.pyplot as plt 
import module_portfolio_new_1
from module_portfolio_new_1 import portfolio, portfolio_n_assets

n = 2
mean = [20,24]
stdev = [4,4]
corr = [[1, -0.1],
        [-0.1, 1]]
ar_std, ar_mean, w = portfolio_n_assets(n, mean, stdev, corr).random()
ar_mean = np.array(ar_mean)
std_mini, mean_mini = portfolio_n_assets(n, mean, stdev, corr).minimum()
M = portfolio_n_assets(n, mean, stdev, corr).Market_portfolio()
std_cml, mean_cml = portfolio_n_assets(n, mean, stdev, corr).capital_market_line()
#print(ar_mean)
#print(ar_std)
#print(w)
stdev = np.array(stdev)
a = ((stdev*corr).T*stdev).T
print(a)
plt.figure(figsize=(10, 5))
plt.scatter(ar_std, ar_mean, c=ar_mean / ar_std, marker='o')
plt.plot(stdev[0],mean[0],'r*', markersize=10, label='asset 1')
plt.plot(stdev[1],mean[1],'b*',markersize=10, label='asset 2')
plt.plot(std_mini, mean_mini, 'r*',markersize=20, label='minimum')
plt.plot(M[0],M[1],'g*',markersize=15, label='Market portfolio')
plt.plot(std_cml, mean_cml, 'y-', markersize=2, label='CML')
plt.grid(True)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio') 
plt.legend(loc='best')
plt.show()

#-----------------------------3 assets----------------------------------------
n = 3
mean = [20,22,24]
stdev = [4,5,4]
corr = [[1, 0.3, -0.1],
        [0.3, 1, 0.3],
        [-0.1, 0.3, 1]]
ar_std, ar_mean, w = portfolio_n_assets(n, mean, stdev, corr).random()
ar_std = np.array(ar_std)
ar_mean = np.array(ar_mean)
std_mini, mean_mini = portfolio_n_assets(n, mean, stdev, corr).minimum()
M = portfolio_n_assets(n, mean, stdev, corr).Market_portfolio()
std_cml, mean_cml = portfolio_n_assets(n, mean, stdev, corr).capital_market_line()
stdev = np.array(stdev)
a = ((stdev*corr).T*stdev).T
print(a)

plt.figure(figsize=(10, 5))
plt.scatter(ar_std, ar_mean, c=ar_mean / ar_std, marker='o')
plt.plot(std_mini, mean_mini, 'r*',markersize=20, label='minimum')
plt.plot(M[0],M[1],'g*',markersize=15, label='Market portfolio')
plt.plot(std_cml, mean_cml, 'y-', markersize=2, label='CML')
plt.plot(stdev[0],mean[0],'r*', markersize=10, label='asset 1')
plt.plot(stdev[1],mean[1],'b*',markersize=10, label='asset 2')
plt.plot(stdev[2],mean[2],'y*',markersize=10, label='asset 3')
plt.grid(True)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio') 
plt.legend(loc='best')
plt.show()
#------------------------------------4 assets----------------------------------
n = 4
mean = [20,22,24, 28]
stdev = [4, 5,4, 10]
corr = [[1, 0.3, -0.1, 0.5],
        [0.3, 1, 0.3, 0.3],
        [-0.1, 0.3, 1, 0.4],
        [0.5, 0.3, 0.4, 1]]
ar_std, ar_mean = portfolio_n_assets(n, mean, stdev, corr).random()[0:2]
ar_std = np.array(ar_std)
ar_mean = np.array(ar_mean)
std_mini, mean_mini = portfolio_n_assets(n, mean, stdev, corr).minimum()
M = portfolio_n_assets(n, mean, stdev, corr).Market_portfolio()
std_cml, mean_cml = portfolio_n_assets(n, mean, stdev, corr).capital_market_line()

stdev = np.array(stdev)
a = ((stdev*corr).T*stdev).T
print(a)

plt.figure(figsize=(10, 5))
plt.scatter(ar_std, ar_mean, c=ar_mean / ar_std, marker='o')
plt.plot(std_mini, mean_mini, 'r*',markersize=20, label='minimum')
plt.plot(M[0],M[1],'g*',markersize=15, label='Market portfolio')
plt.plot(std_cml, mean_cml, 'y-', markersize=2, label='CML')
plt.plot(stdev[0],mean[0],'r*', markersize=10, label='asset 1')
plt.plot(stdev[1],mean[1],'b*',markersize=10, label='asset 2')
plt.plot(stdev[2],mean[2],'y*',markersize=10, label='asset 3')
plt.plot(stdev[3],mean[3],'g*',markersize=10, label='asset 4')
plt.grid(True)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio') 
plt.legend(loc='best')
plt.show()
#------------------------------------5 assets----------------------------------
n = 5
mean = [-0.000129*252,0.000895*252,0.001568*252, 0.001194*252, 0.000045*252]
stdev = [0.018106*252, 0.017839*252,0.029161*252, 0.022768*252, 0.017724*252]
corr = [[1, 0.698181,  0.547637,  0.660381,  0.680853],
        [0.698181, 1, 0.667768,  0.774874,  0.824301],
        [0.547637, 0.667768, 1, 0.730339,  0.647231],
        [0.660381, 0.774874,  0.730339, 1, 0.750268],
        [0.680853, 0.824301, 0.647231, 0.750268, 1]]
ar_std, ar_mean = portfolio_n_assets(n, mean, stdev, corr).random()[0:2]
ar_std = np.array(ar_std)
ar_mean = np.array(ar_mean)
std_mini, mean_mini = portfolio_n_assets(n, mean, stdev, corr).minimum()
M = portfolio_n_assets(n, mean, stdev, corr).Market_portfolio()
std_cml, mean_cml = portfolio_n_assets(n, mean, stdev, corr).capital_market_line()

stdev = np.array(stdev)
a = ((stdev*corr).T*stdev).T
print(a)

plt.figure(figsize=(10, 5))
plt.scatter(ar_std, ar_mean, c=ar_mean / ar_std, marker='o')
plt.plot(std_mini, mean_mini, 'r*',markersize=20, label='minimum')
plt.plot(M[0],M[1],'g*',markersize=15, label='Market portfolio')
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
