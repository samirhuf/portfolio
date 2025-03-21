import streamlit as st
import numpy as np
import pandas as pd
import datetime
path_string_1='./'
st.title('Portfolio Summary-Samir Shah')
file_1=path_string_1+'MobileDisplayEquityInventory.csv'
file_time=path_string_1+'current_time.csv'
df_inventory=pd.read_csv(file_1)
df_inventory.rename(columns={'Today Gain': 'GainToday'}, inplace=True)
total_gain_today=round(df_inventory['GainToday'].sum())
total_gain=round(df_inventory['Total Gain'].sum())
current_investment=df_inventory['Current Investment'].sum()
df_time=pd.read_csv(file_time)
st.write('Time Updated Till: '+str(df_time['Time'].iloc[0]))
def highlight_profit(s):
    return ['background-color: #4BB735']*len(s) if s.GainToday>0 else ['background-color: #A02525']*len(s)
df_styled = (df_inventory.style.
format(precision=2).
apply(highlight_profit, axis=1))
st.dataframe(df_styled)
# st.dataframe(df_inventory.style.apply(highlight_profit, axis=1))
# st.dataframe(df_inventory.style.format(precision=2))
#st.markdown('<style>body{background-color: #f0f2f6;}</style>', unsafe_allow_html=True)
st.subheader('Total Gain Today: ' + str(total_gain_today))
st.subheader('Total Gain: ' + str(total_gain))