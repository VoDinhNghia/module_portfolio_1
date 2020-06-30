import pandas as pd  
from pandas_datareader import data, wb
import datetime
import numpy as np 

#list_cp là list tên các cổ phiếu
#day_start là ngày bắt đầu vd: day_start = [1,1,2018] tương tự cho day_end
class computation_port:
    def __init__(self, list_cp, day_start, day_end):
        self.list_cp = list_cp
        self.day_start = day_start
        self.day_end = day_end
    
    def comp_port(self):
        tickers = self.list_cp
        day_start = np.array(self.day_start, np.int)
        day_end = np.array(self.day_end, np.int)
        start = datetime.datetime(day_start[2],day_start[1],day_start[0])
        end = datetime.datetime(day_end[2],day_end[1],day_end[0])
        df = pd.DataFrame([data.DataReader(ticker, 'yahoo', start, end)['Adj Close'] for ticker in tickers]).T
        df.columns = tickers
        n = int(len(tickers))
        mean = df.pct_change().mean()*252
        corr = df.pct_change().corr()
        std = df.pct_change().std()*252
        #cov = df.pct_change().cov()*252
        
        return n, mean, corr, std
    
    def random(self):
        #n, mean, corr, stdev = self.comp_port()
        n = int(self.comp_port()[0])
        mean = np.array(self.comp_port()[1])
        corr = np.array(self.comp_port()[2])
        stdev = np.array(self.comp_port()[3])
        #cov = np.array(self.comp_port()[4])
        arr_mean_rd = []
        arr_std_rd = []
        weights = []
        for p in range (1500):
            w = np.random.random(n)
            w /= np.sum(w)
            arr_mean_rd.append(round(np.dot(mean ,w.T),2))
            #kq = np.sqrt(np.dot(w, np.dot(((stdev*corr).T*stdev),w.T)))
            kq = np.sqrt(np.dot(w*stdev, np.dot(corr,(stdev*w).T)))
            arr_std_rd.append(round(kq,2))
            weights.append(w)
        return arr_std_rd, arr_mean_rd, weights 
    
    def minimum(self):
        ar_std, ar_mean, w = self.random()
        std_minimum = min(ar_std)
        mean_minimum = ar_mean[ar_std.index(std_minimum)]
        return std_minimum, mean_minimum

    def Market_portfolio(self):
        ar_std, ar_mean = self.random()[0:2]
        risk_free = 0.05
        shape_ratio = []
        for m in ar_mean:
            shape_ratio.append(round((m - risk_free)/ar_std[ar_mean.index(m)],2))
        max_ratio = max(shape_ratio)
        index_M = shape_ratio.index(max_ratio)
        value_M_mean = ar_mean[index_M]
        value_M_std = ar_std[index_M]
        return value_M_std, value_M_mean

    def capital_market_line(self):
        M_std, M_mean = self.Market_portfolio()
        r_free = 0.05  
        arr_mean_cml = []
        #mean = self.comp_port()[1]
        
        std_exp = np.arange(0, 6.5, 1)

        for x in std_exp:
            mean_exp = round(r_free + (x*(M_mean-r_free))/M_std, 2)
            arr_mean_cml.append(mean_exp)
        return std_exp, arr_mean_cml

