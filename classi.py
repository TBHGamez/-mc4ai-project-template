from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np 
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse

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

def classi():
    st.write('Đặc trưng')
    S6 = st.checkbox('Midterm (S6)')
    S_AVG = st.checkbox('Trung bình homework (S-AVG)')
    GPA = st.checkbox('GPA')
    if S6 and S_AVG:
     def mhpf():
      Xmhpf = df[['S6','S-AVG']].values.copy()
      ymhpf = []
      for i in range(len(df[['NAME']])):
        if Xmhpf[i][0] >= 6 and Xmhpf[i][1] >= 6:
          ymhpf.append(1)
        else:
          ymhpf.append(0)
      ymhpf = np.array(ymhpf)
      model = LogisticRegression()
      model.fit(Xmhpf, ymhpf)
      weightsmhpf = model.coef_[0]
      biasmhpf = model.intercept_[0]
      w1mhpf, w2mhpf = weightsmhpf[0], weightsmhpf[1]
      st.write('DỰ ĐOÁN HS ĐẬU/RỚT (PASS/FAIL) DỰA TRÊN MIDTERM & ĐIỂM TRUNG BÌNH HOMEWORK')
      plt.scatter(Xmhpf[ymhpf==0,0], Xmhpf[ymhpf==0,1])
      plt.scatter(Xmhpf[ymhpf==1,0], Xmhpf[ymhpf==1,1])
      plt.legend(['S6', 'S-AVG', 'Decision Boundary'])
      plt.xlabel('S-AVG')
      plt.ylabel('S6')
      x1mhpf = np.linspace(0, 10, 1000)
      x2mhpf = -(w1mhpf*x1mhpf + biasmhpf) / w2mhpf
      plt.plot(x1mhpf,x2mhpf)
      st.pyplot(fig=None)
      st.set_option('deprecation.showPyplotGlobalUse', False)
     mhpf()
     def mhf():
      xmhf = df['S6'].values
      ymhf = df['S-AVG'].values
      x_train, x_test, y_train, y_test = train_test_split(xmhf, ymhf, test_size=.2, random_state=42)
      x_train = x_train.reshape(-1,1)
      x_test = x_test.reshape(-1,1)
      model = LinearRegression()
      model.fit(x_train, y_train)
      weightsmhf = model.coef_[0]
      biasmhf = model.intercept_
      y_test_pred = model.predict(x_test)
#       mae(y_test, y_test_pred), mse(y_test, y_test_pred), model.score(x_test, y_test)
      st.write('DỰ ĐOÁN ĐIỂM FINAL DỰA TRÊN MIDTERM & ĐIỂM TRUNG BÌNH HOMEWORK')
      plt.scatter(xmhf, ymhf)
      plt.plot(xmhf, model.predict(xmhf.reshape(-1,1)), c='y')
      plt.xlabel('S-AVG')
      plt.ylabel('S6')
      st.pyplot(fig=None)
      st.set_option('deprecation.showPyplotGlobalUse', False)
     mhf()
    elif S6 and GPA:
     def mgpf():
      Xmgpf = df[['S6','GPA']].values.copy()
      ymgpf = []
      for i in range(len(df[['NAME']])):
        if Xmgpf[i][0] >= 6 and Xmgpf[i][1] >= 6:
           ymgpf.append(1)
        else:
           ymgpf.append(0)
      ymgpf = np.array(ymgpf)
      model = LogisticRegression()
      model.fit(Xmgpf, ymgpf)
      weightsmgpf = model.coef_[0]
      biasmgpf = model.intercept_[0]
      w1mgpf, w2mgpf = weightsmgpf[0], weightsmgpf[1]
      st.write('DỰ ĐOÁN HS ĐẬU/RỚT (PASS/FAIL) DỰA TRÊN MIDTERM & GPA')
      plt.scatter(Xmgpf[ymgpf==0,0], Xmgpf[ymgpf==0,1])
      plt.scatter(Xmgpf[ymgpf==1,0], Xmgpf[ymgpf==1,1])
      plt.legend(['S6', 'S-AVG', 'Decision Boundary'])
      plt.xlabel('S-AVG')
      plt.ylabel('S6')
      x1mgpf = np.linspace(0,10,1000)
      x2mgpf = -(w1mgpf*x1mgpf + biasmgpf) / w2mgpf
      plt.plot(x1mgpf,x2mgpf)
      st.pyplot(fig=None)
      st.set_option('deprecation.showPyplotGlobalUse', False)
     mgpf()
     def mgf():
      xmgf = df['S6'].values
      ymgf = df['GPA'].values
      x_train, x_test, y_train, y_test = train_test_split(xmgf, ymgf, test_size=.2, random_state=42)
      x_train = x_train.reshape(-1,1)
      x_test = x_test.reshape(-1,1)
      model = LinearRegression()
      model.fit(x_train, y_train)
      weightsmgf = model.coef_[0]
      biasmgf = model.intercept_
      y_test_pred = model.predict(x_test)
#       mae(y_test, y_test_pred), mse(y_test, y_test_pred), model.score(x_test, y_test)
      st.write('DỰ ĐOÁN ĐIỂM FINAL DỰA TRÊN MIDTERM & GPA')
      plt.scatter(xmgf, ymgf)
      plt.plot(xmgf, model.predict(xmgf.reshape(-1,1)), c='y')
      plt.xlabel('GPA')
      plt.ylabel('S6')
      st.pyplot(fig=None)
      st.set_option('deprecation.showPyplotGlobalUse', False)
     mgf()
    elif S6 and GPA and S_AVG:
     def barD():
      st.write('PHÂN LOẠI HS ĐẬU/RỚT (PASS/FAIL) DỰA TRÊN MIDTERM, ĐIỂM TRUNG BÌNH HOMEWORK, GPA')
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
      XbarD = df[['S6','S-AVG','GPA']].values
      ybarD = df['PASS/FAIL_ID'].values
      model = LogisticRegression()
      model.fit(XbarD, ybarD)
      print('score:', round(model.score(XbarD, ybarD), 2))
      w1barD, w2barD, w3barD = model.coef_[0]
      bbarD = model.intercept_[0]
      xbound = np.array([XbarD[:,0].min(), XbarD[:,0].max()])
      ybound = np.array([XbarD[:,1].min(), XbarD[:,1].max()])
      xx, yy = np.meshgrid(xbound, ybound)
      xy = np.c_[xx.ravel(), yy.ravel()]
      zbound = -(w1barD*xy[:,0]+w2barD*xy[:,1]+bbarD)/w3barD
      zbound = zbound.reshape(xx.shape)
      df1 = df[['S6','S-AVG','GPA','PASS/FAIL','PASS/FAIL_ID']]
      df2 = df1[df1['PASS/FAIL_ID'] == '1']
      df3 = df1[df1['PASS/FAIL_ID'] == '0']
      figb = go.Figure(data=[go.Surface(x=xbound, y=ybound, z=zbound), 
                          go.Scatter3d(x=df2['S6'], y=df2['S-AVG'], z=df2['GPA'], mode='markers'),
                          go.Scatter3d(x=df3['S6'], y=df3['S-AVG'], z=df3['GPA'], mode='markers')])
      st.pyplot(figb)
      st.set_option('deprecation.showPyplotGlobalUse', False)
     barD()
classi()
