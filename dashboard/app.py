import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Ethiopia FI Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/ethiopia_fi_enriched.csv')
    df['observation_date'] = pd.to_datetime(df['observation_date'])
    return df

df = load_data()

st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Select Page", ["Overview", "Trends", "Forecasts", "Inclusion Projections"])

if page == "Overview":
    st.title("📈 Ethiopia Financial Inclusion Overview")
    
    latest_ownership = df[(df['record_type'] == 'observation') & (df['indicator'] == 'Account Ownership Rate') & (df['gender'] == 'all')].sort_values('observation_date')['value_numeric'].iloc[-1]
    latest_mm = df[(df['record_type'] == 'observation') & (df['indicator'] == 'Mobile Money Account Rate')].sort_values('observation_date')['value_numeric'].iloc[-1]
    
    col1, col2 = st.columns(2)
    col1.metric("Account Ownership (2024)", f"{latest_ownership:.0f}%", "+3% since 2021")
    col2.metric("Mobile Money Users (2024)", f"{latest_mm:.1f}%", "+100% since 2021")
    
    ownership_data = df[(df['record_type'] == 'observation') & (df['indicator'] == 'Account Ownership Rate') & (df['gender'] == 'all')].sort_values('observation_date')
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(ownership_data['observation_date'], ownership_data['value_numeric'], 'o-', linewidth=3)
    ax.set_ylabel('% of Adults')
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

elif page == "Trends":
    st.title("📊 Indicator Trends")
    indicators = df[df['record_type'] == 'observation']['indicator'].unique()
    selected = st.multiselect("Select Indicators", indicators, default=['Account Ownership Rate', 'Mobile Money Account Rate'])
    if selected:
        trend_data = df[(df['record_type'] == 'observation') & (df['indicator'].isin(selected))]
        fig, ax = plt.subplots(figsize=(10, 5))
        for indicator in selected:
            data = trend_data[trend_data['indicator'] == indicator]
            ax.plot(data['observation_date'], data['value_numeric'], 'o-', label=indicator, linewidth=2)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

elif page == "Forecasts":
    st.title("🔮 Forecasts 2025-2027")
    scenario = st.selectbox("Select Scenario", ['Base', 'Optimistic', 'Pessimistic'])
    
    # Hardcoded from your notebook output
    forecast_data = {
        'Year': [2025, 2026, 2027],
        'Base Access': [55.4, 59.3, 63.2],
        'Optimistic Access': [55.8, 60.0, 64.2],
        'Pessimistic Access': [55.1, 58.6, 62.1]
    }
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(forecast_data['Year'], forecast_data[f'{scenario} Access'], 'o-', linewidth=3, color='#2ca02c')
    ax.axhline(y=60, color='red', linestyle='--', label='60% NFIS-II Target')
    ax.set_title(f'Account Ownership Forecast ({scenario} Scenario)')
    ax.set_ylabel('Adults with Account (%)')
    ax.set_xlabel('Year')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(45, 70)
    st.pyplot(fig)
    
    st.info(f"📌 2027 {scenario} Scenario: {forecast_data[f'{scenario} Access'][2]:.1f}%")

else:
    st.title("🎯 Progress Toward 60% Target")
    years = [2014, 2017, 2021, 2024, 2025, 2026, 2027]
    values = [22, 35, 46, 49, 55.4, 59.3, 63.2]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(years[:4], values[:4], 'o-', label='Historical', linewidth=3, color='#1f77b4')
    ax.plot(years[4:], values[4:], 'o--', label='Projected (Base)', linewidth=3, color='#ff7f0e')
    ax.axhline(y=60, color='green', linestyle='--', label='60% Target')
    ax.set_ylabel('Adults with Account (%)')
    ax.set_xlabel('Year')
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    st.success("✅ Ethiopia is projected to reach 63.2% by 2027, exceeding the 60% target!")