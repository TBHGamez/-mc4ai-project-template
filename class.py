from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np 
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("py4ai-score.csv", low_memory=False)
df['BONUS'].fillna(0, inplace = True)
for i in range(1, 11):
 df[f"S{i}"].fillna(0, inplace = True)
df['REG-MC4AI'].fillna("N", inplace = True)

avg = []
for i in df.index:
  r = df.loc[i][4:13]
  avg.append(r.mean())
df['S-AVG'] = avg

def mhpf():
  X = df[['S6','S-AVG']].values.copy()
  y = []
  for i in range(len(df[['NAME']])):
    if X[i][0] >= 6 and X[i][1] >= 6:
      y.append(1)
    else:
      y.append(0)
  y = np.array(y)


 model = LogisticRegression()
 model.fit(X, y)
 weights = model.coef_[0]
 bias = model.intercept_[0]
 weights, bias
 w1, w2 = weights[0], weights[1]
 plt.scatter(X[y==0,0], X[y==0,1])
 plt.scatter(X[y==1,0], X[y==1,1])
 plt.legend(['S6', 'S-AVG', 'Decision Boundary'])
 plt.xlabel('S-AVG')
 plt.ylabel('S6')
 x1 = np.linspace(0,10,1000)
 x2 = -(w1*x1+bias)/w2
 plt.plot(x1,x2)
 st.pyplot(fig=None)
 
mhpf()

def mgpf():
 X = df[['S6','GPA']].values.copy()
 y = []
 for i in range(len(df[['NAME']])):
  if X[i][0] >= 6 and X[i][1] >= 6:
   y.append(1)
  else:
   y.append(0)
 y = np.array(y)
 
 plt.scatter(X[y==0,0], X[y==0,1])
 plt.scatter(X[y==1,0], X[y==1,1])
 plt.legend(['S6', 'GPA'])
 plt.xlabel('GPA')
 plt.ylabel('S6')
 st.pyplot(fig=None)
 
 from sklearn.linear_model import LogisticRegression
 model = LogisticRegression()
 model.fit(X, y)
 print("weights", model.coef_)
 print("bias", model.intercept_)
 weights = model.coef_[0]
 bias = model.intercept_[0]
 weights, bias
 w1, w2 = weights[0], weights[1]
 plt.scatter(X[y==0,0], X[y==0,1])
 plt.scatter(X[y==1,0], X[y==1,1])
 plt.legend(['S6', 'S-AVG', 'Decision Boundary'])
 plt.xlabel('S-AVG')
 plt.ylabel('S6')
 x1 = np.linspace(0,10,1000)
 x2 = -(w1*x1+bias)/w2
 plt.plot(x1,x2)
 st.pyplot(fig=None)

mgpf()
 
def mhf():
 x = df['S6'].values
 y = df['S-AVG'].values
 plt.scatter(x, y)
 st.pyplot(fig=None)

 from sklearn.model_selection import train_test_split
 x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42)
 x_train.shape, x_test.shape, y_train.shape, y_test.shape
 plt.scatter(x_train, y_train)
 plt.scatter(x_test, y_test)
 st.pyplot(fig=None)

 from sklearn.linear_model import LinearRegression
 x_train = x_train.reshape(-1,1)
 x_test = x_test.reshape(-1,1)
 model = LinearRegression()
 model.fit(x_train, y_train)
 from sklearn.metrics import mean_absolute_error as mae
 from sklearn.metrics import mean_squared_error as mse
 y_test_pred = model.predict(x_test)
 mae(y_test, y_test_pred), mse(y_test, y_test_pred), model.score(x_test, y_test)
 import matplotlib.pyplot as plt
 plt.scatter(x, y)
 plt.plot(x, model.predict(x.reshape(-1,1)), c='y')
 plt.xlabel('S-AVG')
 plt.ylabel('S6')
 st.pyplot(fig=None)
 
mhf()
 
def mgf():
 x = df['S6'].values
 y = df['GPA'].values
 x.shape, y.shape

 x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42)
 x_train.shape, x_test.shape, y_train.shape, y_test.shape\

 plt.scatter(x_train, y_train)
 plt.scatter(x_test, y_test)
 st.pyplot(fig=None)

 x_train = x_train.reshape(-1,1)
 x_test = x_test.reshape(-1,1)

 model = LinearRegression()
 model.fit(x_train, y_train)

 print("weights", model.coef_)
 print("bias", model.intercept_)

 y_test_pred = model.predict(x_test)
 mae(y_test, y_test_pred), mse(y_test, y_test_pred), model.score(x_test, y_test)

 plt.scatter(x, y)
 plt.plot(x, model.predict(x.reshape(-1,1)), c='y')
 plt.xlabel('GPA')
 plt.ylabel('S6')
 st.pyplot(fig=None)

mgf()

def d3():
 def pf(c):
   if c['GPA'] <= 6.:
     return "F"
   else:
     return "P"

 def pf_id(c):
   if c['PASS/FAIL'] == 'P':
     return "1"
   else:
     return "0"

 df['PASS/FAIL'] = df.apply(pf, axis=1)
 df['PASS/FAIL_ID'] = df.apply(pf_id, axis=1)
 import plotly.graph_objects as go
 import plotly.express as px

 px.scatter_3d(df, x='S6', y='S-AVG', z='GPA', color='PASS/FAIL')
 X = df[['S6','S-AVG','GPA']].values
 y = df['PASS/FAIL_ID'].values
 from sklearn.linear_model import LogisticRegression
 from sklearn.metrics import accuracy_score

 model = LogisticRegression()
 model.fit(X, y)
 w1, w2, w3 = model.coef_[0]
 b = model.intercept_[0]
 import plotly.graph_objects as go

 xbound = np.array([X[:,0].min(), X[:,0].max()])
 ybound = np.array([X[:,1].min(), X[:,1].max()])

 xx, yy = np.meshgrid(xbound, ybound)
 xy = np.c_[xx.ravel(), yy.ravel()]

 zbound = -(w1*xy[:,0]+w2*xy[:,1]+b)/w3
 zbound = zbound.reshape(xx.shape)

 df1 = df[['S6','S-AVG','GPA','PASS/FAIL','PASS/FAIL_ID']]
 df2 = df1[df1['PASS/FAIL_ID'] == '1']
 df3 = df1[df1['PASS/FAIL_ID'] == '0']

 fig = go.Figure(data=[go.Surface(x=xbound, y=ybound, z=zbound), 
                       go.Scatter3d(x=df2['S6'], y=df2['S-AVG'], z=df2['GPA'], mode='markers'),
                       go.Scatter3d(x=df3['S6'], y=df3['S-AVG'], z=df3['GPA'], mode='markers')])
 fig.show()

d3()
