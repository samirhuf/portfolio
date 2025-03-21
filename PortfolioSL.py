import streamlit as st
import numpy as np
import pandas as pd
import datetime
path_string_1='./'
st.title('Portfolio Summary-Samir Shah')
file_1=path_string_1+'MobileDisplayEquityInventory.csv'
file_time=path_string_1+'current_time.csv'
df_inventory=pd.read_csv(file_1)
total_gain_today=df_inventory['Today Gain'].sum()
total_gain=df_inventory['Total Gain'].sum()
current_investment=df_inventory['Current Investment'].sum()
df_time=pd.read_csv(file_time)
st.header('Time Updated Till: '+str(df_time['Time'].iloc[0]))
styled_df = df_inventory.style.set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#f0f2f6'), ('font-weight', 'bold')]},
        {'selector': 'td', 'props': [('text-align', 'left')]},
        {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('width', '100%')]},
        {'selector': 'th, td', 'props': [('border', '1px solid #ddd'), ('padding', '8px')]}
    ])
st.dataframe(styled_df)
st.markdown('<style>body{background-color: #f0f2f6;}</style>', unsafe_allow_html=True)
st.subheader('Total Gain Today: ' + str(total_gain_today))
st.subheader('Total Gain: ' + str(total_gain))