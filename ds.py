import streamlit as st
import pandas as pd
import numpy as np 
import re

df = pd.read_csv("py4ai-score.csv", low_memory=False)
df['BONUS'].fillna(0, inplace = True)
for i in range(1, 11):
 df[f"S{i}"].fillna(0, inplace = True)
df['REG-MC4AI'].fillna("N", inplace = True)


def class_group(row):
 p = row['CLASS'] 
 if re.search('^..CT.$', p):
    return 'Chuyên Toán'
 elif re.search('^..CV.$', p):
    return 'Chuyên Văn'
 elif re.search('^..CL.$', p):
    return 'Chuyên Lý'
 elif re.search('^..CH.$', p):
    return 'Chuyên Hóa'
 elif re.search('^..CA.$', p):
    return 'Chuyên Anh'
 elif re.search('^..CSD$', p):
    return 'Sử Địa'
 elif re.search('^..CTIN$', p):
    return 'Chuyên Tin'
 elif re.search('^..CTRN$', p):
    return 'Trung Nhật'
 elif re.search('^..TH$', p):
    return 'Tích Hợp/Song Ngữ'
 elif re.search('^..SN$', p):
    return 'Tích Hợp/Song Ngữ'
 else: return 'Khác'


df['CLASS-GROUP'] = df.apply(class_group, axis=1)
print(df['CLASS-GROUP'])

col1, col2, col3, col4 = st.columns(4)

with col1:
    gender = st.write('Giới tính')
    male = st.checkbox('Nam')
    fem = st.checkbox('Nữ')
    if male and fem: 
        dfg = df
    elif male:
        dfg = df[df['GENDER']=='M']
    elif fem:
        dfg = df[df['GENDER']=='F']
    else:
        dfg = df

with col2: 
    khoi = st.radio('Khối lớp', ('Tất cả', 'Lớp 10', 'Lớp 11', "Lớp 12"), horizontal=True)
    if khoi == 'Lớp 10':
     dfk = dfg[dfg['CLASS'].str.startswith('10')]
    elif khoi == 'Lớp 11':
     dfk = dfg[dfg['CLASS'].str.startswith('11')]
    elif khoi == 'Lớp 12':
     dfk = dfg[dfg['CLASS'].str.startswith('12')]
    else: 
     dfk = dfg

with col3: 
    AI_class = st.selectbox('Phòng', ('Tất cả','A114', 'A115'))
    if AI_class == 'A114':
     dfai = dfk[dfk['PYTHON-CLASS'].str.startswith('114')]
    elif AI_class == 'A115':
     dfai = dfk[dfk['PYTHON-CLASS'].str.startswith('115')]
    else: 
     dfai = dfk
with col4: 
    times = st.multiselect('Buổi', ['Sáng','Chiều'])
    if times == ['Sáng']:
     dft = dfai[dfai['PYTHON-CLASS'].str.endswith('S')] 
    elif times == ['Chiều']:
     dft = dfai[dfai['PYTHON-CLASS'].str.endswith('C')]
    else: dft = dfai
st.write(dft)
data = {'NAME' : [], 
        'GENDER': [],
        'CLASS': [],
        'PYTHON-CLASS': [],
        'S1': [],
        'S2': [],
        'S3': [],
        'S4': [],
        'S5': [],
        'S6': [],
        'S7': [],
        'S8': [],
        'S9': [],
        'S10': [],
        'BONUS': [],
        'GPA': [],
        'REG-MC4AI': [],
        'CLASS-GROUP': []}
dfr = pd.DataFrame(data)
lc = st.write('Lớp chuyên')
cola, colb, colc, cold, cole = st.columns(5)
with cola:
    math = st.checkbox('Toán')
    lit = st.checkbox('Văn')
   
    if math:
     dfto = dft[dft['CLASS-GROUP'].isin(['Chuyên Toán'])]
    else: dfto = pd.DataFrame()
    if lit:
     dfv = dft[dft['CLASS-GROUP'].isin(['Chuyên Văn'])]
    else: dfv = pd.DataFrame()
    
with colb:
    ly = st.checkbox('Lý')
    hoa = st.checkbox('Hóa')
    if ly:
     dfl = dft[dft['CLASS-GROUP'].isin(['Chuyên Lý'])]
    else: dfl = pd.DataFrame()
    if hoa:
     dfh = dft[dft['CLASS-GROUP'].isin(['Chuyên Hóa'])]
    else: dfh = pd.DataFrame()
with colc:
    eng = st.checkbox('Anh')
    tin = st.checkbox('Tin')
    if eng:
     dfa = dft[dft['CLASS-GROUP'].isin(['Chuyên Anh'])]
    else: dfa = pd.DataFrame()
    if tin:
     dfti = dft[dft['CLASS-GROUP'].isin(['Chuyên Tin'])]
    else: dfti = pd.DataFrame()
with cold:
    sd = st.checkbox('Sử Địa')
    tn = st.checkbox('Trung Nhật')
    if sd:
     dfsd = dft[dft['CLASS-GROUP'].isin(['Sử Địa'])]
    else: dfsd = pd.DataFrame()
    if tn:
     dftn = dft[dft['CLASS-GROUP'].isin(['Trung Nhật'])]
    else: dftn = pd.DataFrame()
with cole:
    ts = st.checkbox('TH/SN')
    k = st.checkbox('Khác')
    if ts:
     dfts = dft[dft['CLASS-GROUP'].isin(['Tích Hợp/Song Ngữ'])]
    else: dfts = pd.DataFrame()
    if k:
     dfk = dfk[dft['CLASS-GROUP'].isin(['Khác'])]
    else: dfk = pd.DataFrame()
for i in dfto.index:
     dfr.loc[i] = list(dfto.loc[i])
for i in dfv.index:
     dfr.loc[i] = list(dfv.loc[i])
for i in dfl.index:
     dfr.loc[i] = list(dfl.loc[i])
for i in dfh.index:
     dfr.loc[i] = list(dfh.loc[i])
for i in dfa.index:
     dfr.loc[i] = list(dfa.loc[i])
for i in dfti.index:
     dfr.loc[i] = list(dfti.loc[i])
for i in dfsd.index:
     dfr.loc[i] = list(dfsd.loc[i])
for i in dftn.index:
     dfr.loc[i] = list(dftn.loc[i])
for i in dfts.index:
     dfr.loc[i] = list(dfts.loc[i])
for i in dfk.index:
     dfr.loc[i] = list(dfk.loc[i])
st.write(dfr)
