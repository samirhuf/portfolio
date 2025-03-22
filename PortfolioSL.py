import streamlit as st
import numpy as np
import pandas as pd
import datetime
path_string_1='./'
st.title('Portfolio Summary-Samir Shah')
file_1=path_string_1+'TotalBatchInventory.csv'
file_time=path_string_1+'current_time.csv'
file_asset_types=path_string_1+'BatchAssetTypes.csv'
df_asset_types=pd.read_csv(file_asset_types)
asset_type = st.selectbox('Choose Type of Asset', df_asset_types, help = 'Filter report to show Only One Asset')
df_inventory=pd.read_csv(file_1)
df_inventory.rename(columns={'Today Gain': 'GainToday'}, inplace=True)
total_gain_today=round(df_inventory['GainToday'].sum()/100000,2)
total_gain=round(df_inventory['Total Gain'].sum()/100000,2)
total_current_investment=round(df_inventory['Current Investment'].sum()/100000)
df_time=pd.read_csv(file_time)
st.write('Time Updated Till: '+str(df_time['Time'].iloc[0]))
df_asset=df_inventory[df_inventory['Asset Type']==asset_type]
asset_gain_today=round(df_asset['GainToday'].sum()/100000,2)
asset_total_gain=round(df_asset['Total Gain'].sum()/100000,2)
asset_current_investment=round(df_asset['Current Investment'].sum()/100000)
m1,m2, m3, m4,m5  = st.columns((0.8,1.2,1.2,1.2,0.8))
m1.write('')
m2.metric('Asset Gain Today: ', value=str(asset_gain_today)+' Lakhs',border=True)
m3.metric('Asset Total Gain: ', value=str(asset_total_gain)+' Lakhs',border=True)
m4.metric('Asset Current Investment: ', value=str(asset_current_investment)+' Lakhs',border=True)
m5.write('')
def highlight_profit(s):
    return ['background-color: #ACD6A7']*len(s) if s.GainToday>0 else ['background-color: #DC6D6D']*len(s)
df_styled = (df_asset.style.
format(precision=2).
apply(highlight_profit, axis=1))
st.dataframe(df_styled)

m6,m7,m8,m9,m10=st.columns((0.8,1.2,1.2,1.2,0.8))
m6.write('')
m7.metric('Total Gain Today: ', value=str(total_gain_today)+' Lakhs',border=True)
m8.metric('Total Gain: ', value=str(total_gain)+' Lakhs',border=True)
m9.metric('Total Current Investment: ', value=str(total_current_investment)+' Lakhs',border=True)
# st.dataframe(df_inventory.style.apply(highlight_profit, axis=1))
# st.dataframe(df_inventory.style.format(precision=2))
#st.markdown('<style>body{background-color: #f0f2f6;}</style>', unsafe_allow_html=True)
# st.subheader('Total Gain Today: ' + str(total_gain_today)+' Lakhs')
# st.subheader('Total Gain: ' + str(total_gain)+ ' Lakhs')
# st.subheader('Current Investment: ' + str(current_investment)+ ' Lakhs')