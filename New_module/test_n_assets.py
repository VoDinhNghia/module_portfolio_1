import numpy as np 
import matplotlib.pyplot as plt 
import module_portfolio_new_1
from module_portfolio_new_1 import portfolio, portfolio_n_assets

n = 2
mean = [25,22]
stdev = [4,5]
corr = [[1, 0.3],
        [0.3, 1]]
ar_std, ar_mean = portfolio_n_assets(n, mean, stdev, corr).random()
ar_std = np.array(ar_std)
ar_mean = np.array(ar_mean)
std_mini, mean_mini = portfolio_n_assets(n, mean, stdev, corr).minimum()
M = portfolio_n_assets(n, mean, stdev, corr).Market_portfolio()
std_cml, mean_cml = portfolio_n_assets(n, mean, stdev, corr).capital_market_line()

plt.figure(figsize=(10, 5))
plt.scatter(ar_std, ar_mean, c=ar_mean / ar_std, marker='o')
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
ar_std, ar_mean = portfolio_n_assets(n, mean, stdev, corr).random()
ar_std = np.array(ar_std)
ar_mean = np.array(ar_mean)
std_mini, mean_mini = portfolio_n_assets(n, mean, stdev, corr).minimum()
M = portfolio_n_assets(n, mean, stdev, corr).Market_portfolio()
std_cml, mean_cml = portfolio_n_assets(n, mean, stdev, corr).capital_market_line()

plt.figure(figsize=(10, 5))
plt.scatter(ar_std, ar_mean, c=ar_mean / ar_std, marker='o')
plt.plot(std_mini, mean_mini, 'r*',markersize=20, label='minimum')
plt.plot(M[0],M[1],'g*',markersize=15, label='Market portfolio')
plt.plot(std_cml, mean_cml, 'y-', markersize=2, label='CML')
plt.grid(True)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio') 
plt.legend(loc='best')
plt.show()
#------------------------------------4 assets----------------------------------
n = 4
mean = [20,22,24, 28]
stdev = [4,5,4, 6]
corr = [[1, 0.3, -0.1, 0.5],
        [0.3, 1, 0.3, 0.3],
        [-0.1, 0.3, 1, 0.4],
        [0.5, 0.3, 0.4, 1]]
ar_std, ar_mean = portfolio_n_assets(n, mean, stdev, corr).random()
ar_std = np.array(ar_std)
ar_mean = np.array(ar_mean)

plt.figure(figsize=(10, 5))
plt.scatter(ar_std, ar_mean, c=ar_mean / ar_std, marker='o')
plt.grid(True)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio') 
plt.legend(loc='best')
plt.show()