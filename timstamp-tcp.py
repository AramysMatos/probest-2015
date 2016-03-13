#!/usr/bin/python             
# ­*­ coding: utf­8 ­*   
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import numpy as np
import pandas as pd
import math
                

tcp = open("lbl-pkt-4.tcp.txt",'r')
l_tcp = tcp.readlines()
tcp.close()
timestamp=[]
tam_dados = []
for i in xrange(len(l_tcp)):
	l_tcp[i] = l_tcp[i].rstrip('\n')
        l_tcp[i] = l_tcp[i].split()
        for j in xrange(len(l_tcp[i])):
            if j == 0:
                l_tcp[i][j] = float(l_tcp[i][j])
		
            else:
                l_tcp[i][j] = int(l_tcp[i][j])

l_tcp[0][0]=0
print len(l_tcp)

for j in xrange(len(l_tcp)):
	timestamp.append(l_tcp[j][0])
x = np.array(timestamp)
media = np.mean(x)
variance = np.var(x)

print media
print variance 
bins= (variance**0.5)*3.49*(len(l_tcp)**(-1/3.0))
print bins
m=1+(3.3*math.log(len(l_tcp)))
print m

df4 = pd.DataFrame(timestamp, columns=['Timestamp-TCP'])
plt.figure();
df4.plot.hist(stacked=True, bins=int(m))
plt.show()
