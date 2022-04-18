import streamlit as st
import pandas as pd
import numpy as np
from urllib.error import URLError
import plotly.graph_objects as go
import matplotlib.pyplot as plt
st.title('Calculate MRP')






freq_day = 0 
freq = st.sidebar.selectbox('Order Frequency', ['Any Day','Once a Week'])
if freq == 'Once a Week':
	freq_day = 7
if freq == 'Any Day':
	freq_day = 1


lead_time = 7 
lead_time = st.sidebar.slider('Lead Time (Days)', min_value=1, max_value=14, value=7)
 

toc = st.sidebar.slider('Target Order Cycle (Days)', min_value=0, max_value=30, value=0)


first_del = 1 + lead_time
second_del = first_del + freq_day + toc



x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]

fig, ax = plt.subplots()

time = ax.broken_barh([(1, lead_time), (1, lead_time)], (11,2), facecolors='tab:orange') #Lead Time
ax.broken_barh([(1, first_del), (1, second_del-1)], (15,3), facecolors='tab:blue') #MRP Period
ax.broken_barh([(first_del, 1), (first_del, 1)], (1,12), facecolors='tab:red') # First Del
ax.broken_barh([(second_del, 1), (second_del, 1)], (1,12), facecolors='tab:pink') # Second Del



ax.legend(['Lead Time', 'MRP Period', 'First Delivery', 'Second Delivery'])


#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




ax.get_yaxis().set_visible(False)


ax.set_xticks(x)
ax.set_yticks(x)
ax.set_xticklabels(x,rotation=45)
ax.tick_params(axis="both", direction="in", pad=3)

for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(5)


ax.set_xlabel('Days')
ax.grid(False)

st.pyplot(fig)





#ax.annotate('race interrupted', (61, 25),
#            xytext=(0.8, 0.9), textcoords='axes fraction',
#            arrowprops=dict(facecolor='black', shrink=0.05),
#            fontsize=16,
#            horizontalalignment='right', verticalalignment='top')


#ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
#               facecolors=('tab:orange', 'tab:green', 'tab:red'))











