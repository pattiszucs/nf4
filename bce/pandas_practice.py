import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.DataFrame(columns=['num','fib'])

#append, pd.concat, pd.merge, pd.join

#df=df.append({'num':1,'fib':1},ignore_index=True)

row1={'num':1,'fib':1}
row2={'num':2,'fib':1}

new_df=pd.DataFrame([row1,row2])
df=pd.concat([df,new_df],axis=0,ignore_index=True)

df2=pd.DataFrame(range(1,21),columns=['n'])
df2['fib']=np.nan

for ix, row in df2.iterrows():
    if ix in [0,1]:
        df2.loc[ix,'fib']=1
    else:
        df2.loc[ix,'fib']=df2.loc[ix-1,'fib']+df2.loc[ix-2,'fib']

#print(df2)

class VelSzamok():

    def __init__(self,n_rows, n_cols):
        self.n_rows=n_rows
        self.n_cols=n_cols
        self.value=np.random.random((self.n_rows, self.n_cols))

    def plot_column_averages(self,show=True):
        averages=self.value.mean(axis=0)
        plt.plot(averages)
        if show:
            plt.show()

a1=VelSzamok(6000,3)
print(a1.value)
a1.plot_column_averages()