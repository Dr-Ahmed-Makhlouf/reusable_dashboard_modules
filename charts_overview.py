import streamlit as st
import pandas as pd
import numpy as np

def draw_overview_charts():
    st.subheader("📈 Key Metrics Overview")
    df = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
    st.line_chart(df)
