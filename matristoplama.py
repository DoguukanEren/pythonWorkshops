# -*- coding: utf-8 -*-

x = [[1,3,5],[2,4,1],[1,5,7]]
y = [[3,3,4],[2,4,1],[3,5,4]]


snc = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    
    for k in range(len(y)):
        
        snc[i][k] = x[i][k] + y[i][k]
        
print(snc)
        