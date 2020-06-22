import numpy as np 
import matplotlib.pyplot as plt
import module_portfolio_new_1
from module_portfolio_new_1 import portfolio, portfolio_n_assets, computation_mean

a = [[10, 30, 68, 80],[56, 64, 73, 67],[100, 105, 115, 150]]
n, mean_exp, std_exp, corr, cov = computation_mean(a).compu_mean()

print(computation_mean(a).comp_list_price())

ar_std, ar_mean, w = computation_mean(a).compu_port()
std_mini, mean_mini = computation_mean(a).minimum_std()
M = computation_mean(a).market_port()
std_cml, mean_cml = computation_mean(a).CML_port()
