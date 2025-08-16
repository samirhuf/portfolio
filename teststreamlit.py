import streamlit as st
import numpy as np
import pandas as pd
import datetime
st.title('Portfolio Summary-Samir Shah')
df_inventory=pd.read_csv('BatchInventory.csv')
#show dataframe
st.dataframe(df_inventory)