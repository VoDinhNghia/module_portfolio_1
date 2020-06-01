import numpy as np 

W = np.arange(0, 1.01, 0.01)

class portfolio:
    #n: số asset, mean: danh sách các mean (mean1, mean2, mean3....), stdev: (stdev1, stdev2, stdev3...), corr: (corr12, corr13, corr14, corr23, corr24, corr34...)
    def __init__(self, n, mean, stdev, corr):
        self.n = n
        self.mean = mean
        self.stdev = stdev
        self.corr = corr

    def compution_mean(self):
        mean = np.array(self.mean)
        def computation(x, y):
            mean_n = w*x + (1-w)*y
            return round(mean_n,2)     

        m12 = []
        m13 = []
        m14 = []
        m15 = []
        m16 = [] 
        m23 = []
        m24 = []
        m25 = []
        m26 = []
        m34 = [] 
        m35 = []
        m36 = []
        m45 = []
        m46 = []
        m56 = []
        m17 = []
        m27 = []
        m37 = []
        m47 = []
        m57 = []
        m67 = []
        m18 = []
        m28 = []
        m38 = []
        m48 = []
        m58 = []
        m68 = []
        m78 = []
        m19 = []
        m29 = []
        m39 = []
        m49 = []
        m59 = []
        m69 = []
        m79 = []
        m89 = []
        m110 = []
        m210 = []
        m310 = []
        m410 = []
        m510 = []
        m610 = []
        m710 = []
        m810 = []
        m910 = []
        for w in W:
            mean12 = 0 
            mean13 = 0
            mean14 = 0
            mean15 = 0
            mean16 = 0
            mean17 = 0
            mean18 = 0
            mean19 = 0
            mean110 = 0
            mean23 = 0
            mean24 = 0
            mean25 = 0
            mean26 = 0
            mean27 = 0
            mean28 = 0
            mean29 = 0
            mean210 = 0
            mean34 = 0
            mean35 = 0
            mean36 = 0
            mean37 = 0
            mean38 = 0
            mean39 = 0
            mean310 = 0
            mean45 = 0
            mean46 = 0
            mean47 = 0
            mean48 = 0
            mean49 = 0
            mean410 = 0
            mean56 = 0
            mean57 = 0
            mean58 = 0
            mean59 = 0
            mean510 = 0
            mean67 = 0
            mean68 = 0
            mean69 = 0
            mean610 = 0
            mean78 = 0
            mean79 = 0
            mean710 = 0
            mean89 = 0
            mean810 = 0
            mean910 = 0
            if(self.n == 2):
                mean12 = computation(mean[0],mean[1])
            if(self.n == 3):
                mean12 = computation(mean[0],mean[1])
                mean13 = computation(mean[0],mean[2])
                mean23 = computation(mean[1],mean[2])
            if(self.n == 4):
                mean12 = computation(mean[0],mean[1])
                mean13 = computation(mean[0],mean[2])
                mean14 = computation(mean[0],mean[3])
                mean23 = computation(mean[1],mean[2])
                mean24 = computation(mean[1],mean[3])
                mean34 = computation(mean[2],mean[3])

            if(self.n == 5):
                mean12 = computation(mean[0],mean[1])
                mean13 = computation(mean[0],mean[2])
                mean14 = computation(mean[0],mean[3])
                mean15 = computation(mean[0],mean[4])
                mean23 = computation(mean[1],mean[2])
                mean24 = computation(mean[1],mean[3])
                mean25 = computation(mean[1],mean[4])
                mean34 = computation(mean[2],mean[3])
                mean35 = computation(mean[2],mean[4])
                mean45 = computation(mean[3],mean[4])

            if(self.n == 6):
                mean12 = computation(mean[0],mean[1])
                mean13 = computation(mean[0],mean[2])
                mean14 = computation(mean[0],mean[3])
                mean15 = computation(mean[0],mean[4])
                mean16 = computation(mean[0],mean[5])
                mean23 = computation(mean[1],mean[2])
                mean24 = computation(mean[1],mean[3])
                mean25 = computation(mean[1],mean[4])
                mean26 = computation(mean[1],mean[5])
                mean34 = computation(mean[2],mean[3])
                mean35 = computation(mean[2],mean[4])
                mean36 = computation(mean[2],mean[5])
                mean45 = computation(mean[3],mean[4])
                mean46 = computation(mean[3],mean[5])
                mean56 = computation(mean[4],mean[5])

            if(self.n == 7):
                mean12 = computation(mean[0],mean[1])
                mean13 = computation(mean[0],mean[2])
                mean14 = computation(mean[0],mean[3])
                mean15 = computation(mean[0],mean[4])
                mean16 = computation(mean[0],mean[5])
                mean17 = computation(mean[0],mean[6])
                mean23 = computation(mean[1],mean[2])
                mean24 = computation(mean[1],mean[3])
                mean25 = computation(mean[1],mean[4])
                mean26 = computation(mean[1],mean[5])
                mean27 = computation(mean[1],mean[6])
                mean34 = computation(mean[2],mean[3])
                mean35 = computation(mean[2],mean[4])
                mean36 = computation(mean[2],mean[5])
                mean37 = computation(mean[2],mean[6])
                mean45 = computation(mean[3],mean[4])
                mean46 = computation(mean[3],mean[5])
                mean47 = computation(mean[3],mean[6])
                mean56 = computation(mean[4],mean[5])
                mean57 = computation(mean[4],mean[6])
                mean67 = computation(mean[5],mean[6])
            
            if(self.n == 8):
                mean12 = computation(mean[0],mean[1])
                mean13 = computation(mean[0],mean[2])
                mean14 = computation(mean[0],mean[3])
                mean15 = computation(mean[0],mean[4])
                mean16 = computation(mean[0],mean[5])
                mean17 = computation(mean[0],mean[6])
                mean18 = computation(mean[0],mean[7])
                mean23 = computation(mean[1],mean[2])
                mean24 = computation(mean[1],mean[3])
                mean25 = computation(mean[1],mean[4])
                mean26 = computation(mean[1],mean[5])
                mean27 = computation(mean[1],mean[6])
                mean28 = computation(mean[1],mean[7])
                mean34 = computation(mean[2],mean[3])
                mean35 = computation(mean[2],mean[4])
                mean36 = computation(mean[2],mean[5])
                mean37 = computation(mean[2],mean[6])
                mean38 = computation(mean[2],mean[7])
                mean45 = computation(mean[3],mean[4])
                mean46 = computation(mean[3],mean[5])
                mean47 = computation(mean[3],mean[6])
                mean48 = computation(mean[3],mean[7])
                mean56 = computation(mean[4],mean[5])
                mean57 = computation(mean[4],mean[6])
                mean58 = computation(mean[4],mean[7])
                mean67 = computation(mean[5],mean[6])
                mean68 = computation(mean[5],mean[7])
                mean78 = computation(mean[6],mean[7])
            
            if(self.n == 9):
                mean12 = computation(mean[0],mean[1])
                mean13 = computation(mean[0],mean[2])
                mean14 = computation(mean[0],mean[3])
                mean15 = computation(mean[0],mean[4])
                mean16 = computation(mean[0],mean[5])
                mean17 = computation(mean[0],mean[6])
                mean18 = computation(mean[0],mean[7])
                mean19 = computation(mean[0],mean[8])
                mean23 = computation(mean[1],mean[2])
                mean24 = computation(mean[1],mean[3])
                mean25 = computation(mean[1],mean[4])
                mean26 = computation(mean[1],mean[5])
                mean27 = computation(mean[1],mean[6])
                mean28 = computation(mean[1],mean[7])
                mean29 = computation(mean[1],mean[8])
                mean34 = computation(mean[2],mean[3])
                mean35 = computation(mean[2],mean[4])
                mean36 = computation(mean[2],mean[5])
                mean37 = computation(mean[2],mean[6])
                mean38 = computation(mean[2],mean[7])
                mean39 = computation(mean[2],mean[8])
                mean45 = computation(mean[3],mean[4])
                mean46 = computation(mean[3],mean[5])
                mean47 = computation(mean[3],mean[6])
                mean48 = computation(mean[3],mean[7])
                mean49 = computation(mean[3],mean[8])
                mean56 = computation(mean[4],mean[5])
                mean57 = computation(mean[4],mean[6])
                mean58 = computation(mean[4],mean[7])
                mean59 = computation(mean[4],mean[8])
                mean67 = computation(mean[5],mean[6])
                mean68 = computation(mean[5],mean[7])
                mean69 = computation(mean[5],mean[8])
                mean78 = computation(mean[6],mean[7])
                mean79 = computation(mean[6],mean[8])
                mean89 = computation(mean[7],mean[8])
            
            if(self.n == 10):
                mean12 = computation(mean[0],mean[1])
                mean13 = computation(mean[0],mean[2])
                mean14 = computation(mean[0],mean[3])
                mean15 = computation(mean[0],mean[4])
                mean16 = computation(mean[0],mean[5])
                mean17 = computation(mean[0],mean[6])
                mean18 = computation(mean[0],mean[7])
                mean19 = computation(mean[0],mean[8])
                mean110 = computation(mean[0],mean[9])
                mean23 = computation(mean[1],mean[2])
                mean24 = computation(mean[1],mean[3])
                mean25 = computation(mean[1],mean[4])
                mean26 = computation(mean[1],mean[5])
                mean27 = computation(mean[1],mean[6])
                mean28 = computation(mean[1],mean[7])
                mean29 = computation(mean[1],mean[8])
                mean210 = computation(mean[1],mean[9])
                mean34 = computation(mean[2],mean[3])
                mean35 = computation(mean[2],mean[4])
                mean36 = computation(mean[2],mean[5])
                mean37 = computation(mean[2],mean[6])
                mean38 = computation(mean[2],mean[7])
                mean39 = computation(mean[2],mean[8])
                mean310 = computation(mean[2],mean[9])
                mean45 = computation(mean[3],mean[4])
                mean46 = computation(mean[3],mean[5])
                mean47 = computation(mean[3],mean[6])
                mean48 = computation(mean[3],mean[7])
                mean49 = computation(mean[3],mean[8])
                mean410 = computation(mean[3],mean[9])
                mean56 = computation(mean[4],mean[5])
                mean57 = computation(mean[4],mean[6])
                mean58 = computation(mean[4],mean[7])
                mean59 = computation(mean[4],mean[8])
                mean510 = computation(mean[4],mean[9])
                mean67 = computation(mean[5],mean[6])
                mean68 = computation(mean[5],mean[7])
                mean69 = computation(mean[5],mean[8])
                mean610 = computation(mean[5],mean[9])
                mean78 = computation(mean[6],mean[7])
                mean79 = computation(mean[6],mean[8])
                mean710 = computation(mean[6],mean[9])
                mean89 = computation(mean[7],mean[8])
                mean810 = computation(mean[7],mean[9])
                mean910 = computation(mean[8],mean[9])
            
            m12.append(mean12)
            m13.append(mean13)
            m23.append(mean23)
            m14.append(mean14)
            m24.append(mean24)
            m34.append(mean34)
            m15.append(mean15)
            m25.append(mean25)
            m35.append(mean35)
            m45.append(mean45)
            m16.append(mean16)
            m26.append(mean26)
            m36.append(mean36)
            m46.append(mean46)
            m56.append(mean56)
            m17.append(mean17)
            m27.append(mean27)
            m37.append(mean37)
            m47.append(mean47)
            m57.append(mean57)
            m67.append(mean67)
            m18.append(mean18)
            m28.append(mean28)
            m38.append(mean38)
            m48.append(mean48)
            m58.append(mean58)
            m68.append(mean68)
            m78.append(mean78)
            m19.append(mean19)
            m29.append(mean29)
            m39.append(mean39)
            m49.append(mean49)
            m59.append(mean59)
            m69.append(mean69)
            m79.append(mean79)
            m89.append(mean89)
            m110.append(mean110)
            m210.append(mean210)
            m310.append(mean310)
            m410.append(mean410)
            m510.append(mean510)
            m610.append(mean610)
            m710.append(mean710)
            m810.append(mean810)
            m910.append(mean910)

        if(self.n == 2):
            return m12
        if(self.n == 3):
            return m12,m13,m23
        if(self.n == 4):
            return m12, m13, m14, m23, m24, m34
        if(self.n == 5):
            return m12,m13,m14,m15,m23,m24,m25,m34,m35,m45
        if(self.n == 6):
            return m12,m13,m14,m15,m16,m23,m24,m25,m26,m34,m35,m36,m45,m46,m56
        if(self.n == 7):
            return m12,m13,m14,m15,m16,m17,m23,m24,m25,m26,m27,m34,m35,m36,m37,m45,m46,m47,m56,m57,m67
        if(self.n == 8):
            return m12,m13,m14,m15,m16,m17,m18,m23,m24,m25,m26,m27,m28,m34,m35,m36,m37,m38,m45,m46,m47,m48,m56,m57,m58,m67,m68,m78
        if(self.n == 9):
            return m12,m13,m14,m15,m16,m17,m18,m19,m23,m24,m25,m26,m27,m28,m29,m34,m35,m36,m37,m38,m39,m45,m46,m47,m48,m49,m56,m57,m58,m59,m67,m68,m69,m78,m79,m89
        if(self.n == 10):
            return m12,m13,m14,m15,m16,m17,m18,m19,m110,m23,m24,m25,m26,m27,m28,m29,m210,m34,m35,m36,m37,m38,m39,m310,m45,m46,m47,m48,m49,m410,m56,m57,m58,m59,m510,m67,m68,m69,m610,m78,m79,m710,m89,m810,m910

    #hàm tính stdev
    def compution_stdev(self):
        stdev = np.array(self.stdev)
        corr = np.array(self.corr)
        def computation_std(x,y,z):
            cov = x*y*z
            return round(np.sqrt(pow(w,2)*pow(x,2) + 2*w*(1-w)*cov + pow((1-w),2)*pow(y,2)),2)
        
        s12 = []
        s13 = []
        s14 = []
        s15 = []
        s16 = []
        s17 = []
        s18 = []
        s23 = []
        s24 = []
        s25 = []
        s26 = []
        s27 = []
        s28 = []
        s34 = []
        s35 = []
        s36 = []
        s37 = []
        s38 = []
        s45 = []
        s46 = []
        s47 = []
        s48 = []
        s56 = []
        s57 = []
        s58 = []
        s67 = []
        s68 = []
        s78 = []
        s19 = []
        s29 = []
        s39 = []
        s49 = []
        s59 = []
        s69 = []
        s79 = []
        s89 = []
        s110 = []
        s210 = []
        s310 = []
        s410 = []
        s510 = []
        s610 = []
        s710 = []
        s810 = []
        s910 = []
        for w in W:
            var_p12 = 0
            var_p13 = 0
            var_p14 = 0
            var_p15 = 0
            var_p16 = 0
            var_p17 = 0
            var_p18 = 0
            var_p19 = 0
            var_p110 = 0
            var_p23 = 0
            var_p24 = 0
            var_p25 = 0
            var_p26 = 0
            var_p27 = 0
            var_p28 = 0
            var_p29 = 0
            var_p210 = 0
            var_p34 = 0
            var_p35 = 0
            var_p36 = 0
            var_p37 = 0
            var_p38 = 0
            var_p39 = 0
            var_p310 = 0
            var_p45 = 0
            var_p46 = 0
            var_p47 = 0
            var_p48 = 0
            var_p49 = 0
            var_p410 = 0
            var_p56 = 0
            var_p57 = 0
            var_p58 = 0
            var_p59 = 0
            var_p510 = 0
            var_p67 = 0
            var_p68 = 0
            var_p69 = 0
            var_p610 = 0
            var_p78 = 0
            var_p79 = 0
            var_p710 = 0
            var_p89 = 0
            var_p810 = 0
            var_p910 = 0
            if(self.n == 2):
                var_p12= computation_std(stdev[0],stdev[1], corr[0])
            if(self.n == 3):
                var_p12 = computation_std(stdev[0],stdev[1], corr[0])
                var_p13 = computation_std(stdev[0],stdev[2], corr[1])
                var_p23 = computation_std(stdev[1],stdev[2], corr[2])
            if(self.n == 4):
                var_p12 = computation_std(stdev[0],stdev[1], corr[0])
                var_p13 = computation_std(stdev[0],stdev[2], corr[1])
                var_p14 = computation_std(stdev[0],stdev[3], corr[2])
                var_p23 = computation_std(stdev[1],stdev[2], corr[3])
                var_p24 = computation_std(stdev[1],stdev[3], corr[4])
                var_p34 = computation_std(stdev[2],stdev[3], corr[5])
            if(self.n == 5):
                var_p12 = computation_std(stdev[0],stdev[1], corr[0])
                var_p13 = computation_std(stdev[0],stdev[2], corr[1])
                var_p14 = computation_std(stdev[0],stdev[3], corr[2])
                var_p15 = computation_std(stdev[0],stdev[4], corr[3])
                var_p23 = computation_std(stdev[1],stdev[2], corr[4])
                var_p24 = computation_std(stdev[1],stdev[3], corr[5])
                var_p25 = computation_std(stdev[1],stdev[4], corr[6])
                var_p34 = computation_std(stdev[2],stdev[3], corr[7])
                var_p35 = computation_std(stdev[2],stdev[4], corr[8])
                var_p45 = computation_std(stdev[3],stdev[4], corr[9])
            if(self.n == 6):
                var_p12 = computation_std(stdev[0],stdev[1], corr[0])
                var_p13 = computation_std(stdev[0],stdev[2], corr[1])
                var_p14 = computation_std(stdev[0],stdev[3], corr[2])
                var_p15 = computation_std(stdev[0],stdev[4], corr[3])
                var_p16 = computation_std(stdev[0],stdev[5], corr[4])
                var_p23 = computation_std(stdev[1],stdev[2], corr[5])
                var_p24 = computation_std(stdev[1],stdev[3], corr[6])
                var_p25 = computation_std(stdev[1],stdev[4], corr[7])
                var_p26 = computation_std(stdev[1],stdev[5], corr[8])
                var_p34 = computation_std(stdev[2],stdev[3], corr[9])
                var_p35 = computation_std(stdev[2],stdev[4], corr[10])
                var_p36 = computation_std(stdev[2],stdev[5], corr[11])
                var_p45 = computation_std(stdev[3],stdev[4], corr[12])
                var_p46 = computation_std(stdev[3],stdev[5], corr[13])
                var_p56 = computation_std(stdev[4],stdev[5], corr[14])
            if(self.n == 7):
                var_p12 = computation_std(stdev[0],stdev[1], corr[0])
                var_p13 = computation_std(stdev[0],stdev[2], corr[1])
                var_p14 = computation_std(stdev[0],stdev[3], corr[2])
                var_p15 = computation_std(stdev[0],stdev[4], corr[3])
                var_p16 = computation_std(stdev[0],stdev[5], corr[4])
                var_p17 = computation_std(stdev[0],stdev[6], corr[5])
                var_p23 = computation_std(stdev[1],stdev[2], corr[6])
                var_p24 = computation_std(stdev[1],stdev[3], corr[7])
                var_p25 = computation_std(stdev[1],stdev[4], corr[8])
                var_p26 = computation_std(stdev[1],stdev[5], corr[9])
                var_p27 = computation_std(stdev[1],stdev[6], corr[10])
                var_p34 = computation_std(stdev[2],stdev[3], corr[11])
                var_p35 = computation_std(stdev[2],stdev[4], corr[12])
                var_p36 = computation_std(stdev[2],stdev[5], corr[13])
                var_p37 = computation_std(stdev[2],stdev[6], corr[14])
                var_p45 = computation_std(stdev[3],stdev[4], corr[15])
                var_p46 = computation_std(stdev[3],stdev[5], corr[16])
                var_p47 = computation_std(stdev[3],stdev[6], corr[17])
                var_p56 = computation_std(stdev[4],stdev[5], corr[18])
                var_p57 = computation_std(stdev[4],stdev[6], corr[19])
                var_p67 = computation_std(stdev[5],stdev[6], corr[20])
            if(self.n == 8):
                var_p12 = computation_std(stdev[0],stdev[1], corr[0])
                var_p13 = computation_std(stdev[0],stdev[2], corr[1])
                var_p14 = computation_std(stdev[0],stdev[3], corr[2])
                var_p15 = computation_std(stdev[0],stdev[4], corr[3])
                var_p16 = computation_std(stdev[0],stdev[5], corr[4])
                var_p17 = computation_std(stdev[0],stdev[6], corr[5])
                var_p18 = computation_std(stdev[0],stdev[7], corr[6])
                var_p23 = computation_std(stdev[1],stdev[2], corr[7])
                var_p24 = computation_std(stdev[1],stdev[3], corr[8])
                var_p25 = computation_std(stdev[1],stdev[4], corr[9])
                var_p26 = computation_std(stdev[1],stdev[5], corr[10])
                var_p27 = computation_std(stdev[1],stdev[6], corr[11])
                var_p28 = computation_std(stdev[1],stdev[7], corr[12])
                var_p34 = computation_std(stdev[2],stdev[3], corr[13])
                var_p35 = computation_std(stdev[2],stdev[4], corr[14])
                var_p36 = computation_std(stdev[2],stdev[5], corr[15])
                var_p37 = computation_std(stdev[2],stdev[6], corr[16])
                var_p38 = computation_std(stdev[2],stdev[7], corr[17])
                var_p45 = computation_std(stdev[3],stdev[4], corr[18])
                var_p46 = computation_std(stdev[3],stdev[5], corr[19])
                var_p47 = computation_std(stdev[3],stdev[6], corr[20])
                var_p48 = computation_std(stdev[3],stdev[7], corr[21])
                var_p56 = computation_std(stdev[4],stdev[5], corr[22])
                var_p57 = computation_std(stdev[4],stdev[6], corr[23])
                var_p58 = computation_std(stdev[4],stdev[7], corr[24])
                var_p67 = computation_std(stdev[5],stdev[6], corr[25])
                var_p68 = computation_std(stdev[5],stdev[7], corr[26])
                var_p78 = computation_std(stdev[6],stdev[7], corr[27])
            if(self.n == 9):
                var_p12 = computation_std(stdev[0],stdev[1], corr[0])
                var_p13 = computation_std(stdev[0],stdev[2], corr[1])
                var_p14 = computation_std(stdev[0],stdev[3], corr[2])
                var_p15 = computation_std(stdev[0],stdev[4], corr[3])
                var_p16 = computation_std(stdev[0],stdev[5], corr[4])
                var_p17 = computation_std(stdev[0],stdev[6], corr[5])
                var_p18 = computation_std(stdev[0],stdev[7], corr[6])
                var_p19 = computation_std(stdev[0],stdev[8], corr[7])
                var_p23 = computation_std(stdev[1],stdev[2], corr[8])
                var_p24 = computation_std(stdev[1],stdev[3], corr[9])
                var_p25 = computation_std(stdev[1],stdev[4], corr[10])
                var_p26 = computation_std(stdev[1],stdev[5], corr[11])
                var_p27 = computation_std(stdev[1],stdev[6], corr[12])
                var_p28 = computation_std(stdev[1],stdev[7], corr[13])
                var_p29 = computation_std(stdev[1],stdev[8], corr[14])
                var_p34 = computation_std(stdev[2],stdev[3], corr[15])
                var_p35 = computation_std(stdev[2],stdev[4], corr[16])
                var_p36 = computation_std(stdev[2],stdev[5], corr[17])
                var_p37 = computation_std(stdev[2],stdev[6], corr[18])
                var_p38 = computation_std(stdev[2],stdev[7], corr[19])
                var_p39 = computation_std(stdev[2],stdev[8], corr[20])
                var_p45 = computation_std(stdev[3],stdev[4], corr[21])
                var_p46 = computation_std(stdev[3],stdev[5], corr[22])
                var_p47 = computation_std(stdev[3],stdev[6], corr[23])
                var_p48 = computation_std(stdev[3],stdev[7], corr[24])
                var_p49 = computation_std(stdev[3],stdev[8], corr[25])
                var_p56 = computation_std(stdev[4],stdev[5], corr[26])
                var_p57 = computation_std(stdev[4],stdev[6], corr[27])
                var_p58 = computation_std(stdev[4],stdev[7], corr[28])
                var_p59 = computation_std(stdev[4],stdev[8], corr[29])
                var_p67 = computation_std(stdev[5],stdev[6], corr[30])
                var_p68 = computation_std(stdev[5],stdev[7], corr[31])
                var_p69 = computation_std(stdev[5],stdev[8], corr[32])
                var_p78 = computation_std(stdev[6],stdev[7], corr[33])
                var_p79 = computation_std(stdev[6],stdev[8], corr[34])
                var_p89 = computation_std(stdev[7],stdev[8], corr[35])
            if(self.n == 10):
                var_p12 = computation_std(stdev[0],stdev[1], corr[0])
                var_p13 = computation_std(stdev[0],stdev[2], corr[1])
                var_p14 = computation_std(stdev[0],stdev[3], corr[2])
                var_p15 = computation_std(stdev[0],stdev[4], corr[3])
                var_p16 = computation_std(stdev[0],stdev[5], corr[4])
                var_p17 = computation_std(stdev[0],stdev[6], corr[5])
                var_p18 = computation_std(stdev[0],stdev[7], corr[6])
                var_p19 = computation_std(stdev[0],stdev[8], corr[7])
                var_p110 = computation_std(stdev[0],stdev[9], corr[8])
                var_p23 = computation_std(stdev[1],stdev[2], corr[9])
                var_p24 = computation_std(stdev[1],stdev[3], corr[10])
                var_p25 = computation_std(stdev[1],stdev[4], corr[11])
                var_p26 = computation_std(stdev[1],stdev[5], corr[12])
                var_p27 = computation_std(stdev[1],stdev[6], corr[13])
                var_p28 = computation_std(stdev[1],stdev[7], corr[14])
                var_p29 = computation_std(stdev[1],stdev[8], corr[15])
                var_p210 = computation_std(stdev[1],stdev[9], corr[16])
                var_p34 = computation_std(stdev[2],stdev[3], corr[17])
                var_p35 = computation_std(stdev[2],stdev[4], corr[18])
                var_p36 = computation_std(stdev[2],stdev[5], corr[19])
                var_p37 = computation_std(stdev[2],stdev[6], corr[20])
                var_p38 = computation_std(stdev[2],stdev[7], corr[21])
                var_p39 = computation_std(stdev[2],stdev[8], corr[22])
                var_p310 = computation_std(stdev[2],stdev[9], corr[23])
                var_p45 = computation_std(stdev[3],stdev[4], corr[24])
                var_p46 = computation_std(stdev[3],stdev[5], corr[25])
                var_p47 = computation_std(stdev[3],stdev[6], corr[26])
                var_p48 = computation_std(stdev[3],stdev[7], corr[27])
                var_p49 = computation_std(stdev[3],stdev[8], corr[28])
                var_p410 = computation_std(stdev[3],stdev[9], corr[29])
                var_p56 = computation_std(stdev[4],stdev[5], corr[30])
                var_p57 = computation_std(stdev[4],stdev[6], corr[31])
                var_p58 = computation_std(stdev[4],stdev[7], corr[32])
                var_p59 = computation_std(stdev[4],stdev[8], corr[33])
                var_p510 = computation_std(stdev[4],stdev[9], corr[34])
                var_p67 = computation_std(stdev[5],stdev[6], corr[35])
                var_p68 = computation_std(stdev[5],stdev[7], corr[36])
                var_p69 = computation_std(stdev[5],stdev[8], corr[37])
                var_p610 = computation_std(stdev[5],stdev[9], corr[38])
                var_p78 = computation_std(stdev[6],stdev[7], corr[39])
                var_p79 = computation_std(stdev[6],stdev[8], corr[40])
                var_p710 = computation_std(stdev[6],stdev[9], corr[41])
                var_p89 = computation_std(stdev[7],stdev[8], corr[42])
                var_p810 = computation_std(stdev[7],stdev[9], corr[43])
                var_p910 = computation_std(stdev[8],stdev[9], corr[44])
            s12.append(var_p12)
            s13.append(var_p13)
            s14.append(var_p14)
            s15.append(var_p15)
            s16.append(var_p16)
            s17.append(var_p17)
            s18.append(var_p18)
            s23.append(var_p23)
            s24.append(var_p24)
            s25.append(var_p25)
            s26.append(var_p26)
            s27.append(var_p27)
            s28.append(var_p28)
            s34.append(var_p34)
            s35.append(var_p35)
            s36.append(var_p36)
            s37.append(var_p37)
            s38.append(var_p38)
            s45.append(var_p45)
            s46.append(var_p46)
            s47.append(var_p47)
            s48.append(var_p48)
            s56.append(var_p56)
            s57.append(var_p57)
            s58.append(var_p58)
            s67.append(var_p67)
            s68.append(var_p68)
            s78.append(var_p78)
            s19.append(var_p19)
            s29.append(var_p29)
            s39.append(var_p39)
            s49.append(var_p49)
            s59.append(var_p59)
            s69.append(var_p69)
            s79.append(var_p79)
            s89.append(var_p89)
            s110.append(var_p110)
            s210.append(var_p210)
            s310.append(var_p310)
            s410.append(var_p410)
            s510.append(var_p510)
            s610.append(var_p610)
            s710.append(var_p710)
            s810.append(var_p810)
            s910.append(var_p910)
        if(self.n == 2):
            return s12
        if(self.n == 3):
            return s12,s13,s23
        if(self.n == 4):
            return s12, s13, s14, s23, s24, s34
        if(self.n == 5):
            return s12,s13,s14,s15,s23,s24,s25,s34,s35,s45
        if(self.n == 6):
            return s12,s13,s14,s15,s16,s23,s24,s25,s26,s34,s35,s36,s45,s46,s56
        if(self.n == 7):
            return s12,s13,s14,s15,s16,s17,s23,s24,s25,s26,s27,s34,s35,s36,s37,s45,s46,s47,s56,s57,s67
        if(self.n == 8):
            return s12,s13,s14,s15,s16,s17,s18,s23,s24,s25,s26,s27,s28,s34,s35,s36,s37,s38,s45,s46,s47,s48,s56,s57,s58,s67,s68,s78
        if(self.n == 9):
            return s12,s13,s14,s15,s16,s17,s18,s19,s23,s24,s25,s26,s27,s28,s29,s34,s35,s36,s37,s38,s39,s45,s46,s47,s48,s49,s56,s57,s58,s59,s67,s68,s69,s78,s79,s89
        if(self.n == 10):
            return s12,s13,s14,s15,s16,s17,s18,s19,s110,s23,s24,s25,s26,s27,s28,s29,s210,s34,s35,s36,s37,s38,s39,s310,s45,s46,s47,s48,s49,s410,s56,s57,s58,s59,s510,s67,s68,s69,s610,s78,s79,s710,s89,s810,s910
    # trả về giá trị minimum của stdev và giá trị của return tương ứng
    def minimum_risk(self):
        arr_mean = self.compution_mean()
        arr_stdev = self.compution_stdev() 
        if(self.n == 2):
            min_std = min(arr_stdev)
            value_mean = arr_mean[arr_stdev.index(min_std)]
            return min_std, value_mean
        else:
            arr_mini_std = []
            for i in arr_stdev:
                arr_mini_std.append(min(i))
            mini_risk = min(arr_mini_std)
            index_mini_arr_stdev = arr_mini_std.index(mini_risk)
            idex_mini_std = arr_stdev[index_mini_arr_stdev].index(mini_risk)
            arr_mean_mini = arr_mean[index_mini_arr_stdev]
            value_mean_mini = arr_mean_mini[idex_mini_std]
            return mini_risk, value_mean_mini
    # trả về list stdev và return để vẽ efficent frontier
    def frontier_eff(self):
        arr_mean = self.compution_mean()
        arr_stdev = self.compution_stdev() 
        mean = self.mean
        stdev = self.stdev
        max_mean = max(mean)
        index_max = mean.index(max_mean)
        value_max_std = stdev[index_max]
        minimun_std, mini_mean = self.minimum_risk()
        mean_frontier = []
        stdev_frontier = []
        if(self.n ==2):
            if(((mean.index(max(mean))==0) and (stdev.index(min(stdev))==0)) or ((mean.index(max(mean))==1) and (stdev.index(min(stdev))==1))):
                return arr_stdev[arr_stdev.index(minimun_std):-1], arr_mean[arr_mean.index(mini_mean):-1]
            else:
                return arr_stdev[0:arr_stdev.index(minimun_std)], arr_mean[0:arr_mean.index(mini_mean)]
        else:
            for w in W:
                mean_f = w*mini_mean + (1-w)*max_mean
                mean_frontier.append(mean_f)
                stdev_f = round(np.sqrt(pow(w,2)*pow(minimun_std,2) + 2*w*(1-w)*(0.7*minimun_std*value_max_std) + pow((1-w),2)*pow(value_max_std,2)),2)
                stdev_frontier.append(stdev_f)
            
        index_std_mini = stdev_frontier.index(min(stdev_frontier))
        return stdev_frontier[0:index_std_mini], mean_frontier[0:index_std_mini]
    def point_M(self):
        r_free = 18
        arr_mean = self.compution_mean()
        arr_stdev = self.compution_stdev() 
        mean_frontier = self.frontier_eff()[1]
        arr_ratio = []
        for m in mean_frontier:
            ratio = (m - r_free)/arr_stdev[arr_mean.index(m)]
            arr_ratio.append(ratio)
        max_ratio = max(arr_ratio)
        index_M = arr_ratio.index(max_ratio)
        value_M_mean = arr_mean[index_M]
        value_M_std = arr_stdev[index_M]
        return value_M_std, value_M_mean

    def CML(self):
        M_std, M_mean = self.point_M()
        r_free = 18  
        arr_mean_cml = []
        std_exp = np.arange(0, 8, 0.5)
        for x in std_exp:
            mean_exp = r_free + (x*(M_mean-r_free))/M_std
            arr_mean_cml.append(mean_exp)
        return std_exp, arr_mean_cml
