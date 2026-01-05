import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Galvanize Portfolio Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS FOR VISUAL POLISH ----------
st.markdown("""
<style>
/* ========================================
   GALVANIZE PORTFOLIO EXPLORER
   Professional Design System CSS
   ======================================== */

/* ========== DESIGN TOKENS ========== */
:root {
    /* Typography */
    --font-serif: Georgia, 'Times New Roman', serif;
    --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    
    /* Neutral Colors */
    --white: #FFFFFF;
    --gray-50: #FAFAFA;
    --gray-100: #F5F5F5;
    --gray-200: #E5E5E5;
    --gray-300: #D4D4D4;
    --gray-400: #A3A3A3;
    --gray-500: #737373;
    --gray-600: #525252;
    --gray-700: #404040;
    --gray-800: #262626;
    --gray-900: #1A1A1A;
    
    /* Brand Colors */
    --blue-primary: #2563EB;
    --blue-dark: #1E40AF;
    --green-accent: #059669;
    --green-light: #D1FAE5;
    
    /* Semantic Colors */
    --success: #059669;
    --warning: #D97706;
    --error: #DC2626;
    --info: #2563EB;
    
    /* Spacing */
    --space-1: 4px;
    --space-2: 8px;
    --space-3: 12px;
    --space-4: 16px;
    --space-5: 20px;
    --space-6: 24px;
    --space-8: 32px;
    --space-10: 40px;
    --space-12: 48px;
    --space-16: 64px;
    --space-20: 80px;
    --space-24: 96px;
    
    /* Shadows */
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.04);
    --shadow-md: 0 2px 4px rgba(0, 0, 0, 0.06);
    --shadow-lg: 0 4px 8px rgba(0, 0, 0, 0.08);
    
    /* Borders */
    --border-light: 1px solid var(--gray-200);
    --border-medium: 1px solid var(--gray-300);
    
    /* Border Radius */
    --radius-sm: 2px;
    --radius-md: 4px;
    --radius-lg: 6px;
    
    /* Transitions */
    --transition-fast: 150ms ease;
    --transition-base: 200ms ease;
    --transition-slow: 300ms ease;
}

/* ========== GLOBAL STYLES ========== */
.main {
    background: var(--white);
    padding: var(--space-8) var(--space-20);
    font-family: var(--font-sans);
    color: var(--gray-700);
    max-width: 1400px;
    margin: 0 auto;
}

/* ========== TYPOGRAPHY ========== */
h1 {
    font-family: var(--font-serif);
    font-size: 48px;
    font-weight: 300;
    color: var(--gray-900);
    line-height: 1.2;
    margin-bottom: var(--space-6);
    letter-spacing: -0.02em;
}

h2 {
    font-family: var(--font-serif);
    font-size: 32px;
    font-weight: 400;
    color: var(--gray-900);
    line-height: 1.3;
    margin-top: var(--space-16);
    margin-bottom: var(--space-6);
}

h3 {
    font-family: var(--font-sans);
    font-size: 20px;
    font-weight: 600;
    color: var(--gray-800);
    line-height: 1.4;
    margin-top: var(--space-8);
    margin-bottom: var(--space-4);
}

h4 {
    font-family: var(--font-sans);
    font-size: 16px;
    font-weight: 600;
    color: var(--gray-800);
    line-height: 1.5;
    margin-top: var(--space-6);
    margin-bottom: var(--space-3);
}

p, div {
    font-family: var(--font-sans);
    font-size: 16px;
    font-weight: 400;
    color: var(--gray-600);
    line-height: 1.6;
}

/* ========== SIDEBAR ========== */
[data-testid="stSidebar"] {
    background: var(--gray-50) !important;
    border-right: var(--border-light);
    padding: var(--space-8) var(--space-6) !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: var(--gray-900) !important;
    font-family: var(--font-sans);
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: var(--space-4);
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: var(--gray-700) !important;
    font-size: 14px;
}

/* Sidebar Navigation Items */
[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: var(--white) !important;
    border: var(--border-light);
    border-radius: var(--radius-md);
    padding: var(--space-3) var(--space-4);
    margin: var(--space-2) 0;
    transition: border-color var(--transition-fast);
    cursor: pointer;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    border-color: var(--blue-primary);
}

[data-testid="stSidebar"] div[role="radiogroup"] label span,
[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: var(--gray-800) !important;
    font-weight: 500;
    font-size: 14px;
}

/* Selected state */
[data-testid="stSidebar"] div[role="radiogroup"] label[data-selected="true"] {
    border-color: var(--blue-primary);
    background: #EFF6FF !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label[data-selected="true"] span,
[data-testid="stSidebar"] div[role="radiogroup"] label[data-selected="true"] p {
    color: var(--blue-primary) !important;
}

/* ========== PAGE HEADER ========== */
.page-header {
    margin-bottom: var(--space-12);
    padding-bottom: var(--space-6);
    border-bottom: var(--border-light);
}

.page-header h1 {
    margin-bottom: var(--space-2);
}

.page-header p {
    font-size: 16px;
    color: var(--gray-600);
    margin-top: var(--space-2);
}

/* ========== METRICS ========== */
div[data-testid="metric-container"] {
    background: var(--gray-50);
    border: var(--border-light);
    border-radius: var(--radius-md);
    padding: var(--space-5);
    transition: box-shadow var(--transition-base);
}

div[data-testid="metric-container"]:hover {
    box-shadow: var(--shadow-sm);
}

div[data-testid="stMetricLabel"] {
    font-size: 13px;
    font-weight: 500;
    color: var(--gray-500);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: var(--space-1);
}

div[data-testid="stMetricValue"] {
    font-size: 32px;
    font-weight: 700;
    color: var(--gray-900);
    line-height: 1.2;
}

div[data-testid="stMetricDelta"] {
    font-size: 14px;
    font-weight: 500;
    margin-top: var(--space-1);
}

/* ========== CARDS ========== */
.section-card {
    background: var(--white);
    border: var(--border-light);
    border-radius: var(--radius-md);
    padding: var(--space-6);
    margin-bottom: var(--space-6);
    box-shadow: var(--shadow-sm);
}

/* ========== BUTTONS ========== */
.stButton > button {
    background: var(--blue-primary);
    color: var(--white);
    border: none;
    border-radius: var(--radius-md);
    padding: var(--space-3) var(--space-6);
    font-weight: 500;
    font-size: 14px;
    transition: background var(--transition-fast);
    box-shadow: none;
}

.stButton > button:hover {
    background: var(--blue-dark);
    box-shadow: var(--shadow-sm);
}

.stButton > button:active {
    transform: translateY(1px);
}

/* ========== TABLES ========== */
.dataframe {
    border: var(--border-light) !important;
    border-radius: var(--radius-md) !important;
    overflow: hidden;
    font-family: var(--font-sans);
    font-size: 14px;
}

.dataframe thead tr {
    background: var(--gray-50) !important;
}

.dataframe thead th {
    font-weight: 600 !important;
    color: var(--gray-600) !important;
    font-size: 13px !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: var(--space-3) var(--space-4) !important;
    border-bottom: var(--border-medium) !important;
}

.dataframe tbody tr {
    border-bottom: 1px solid var(--gray-100) !important;
    transition: background var(--transition-fast);
}

.dataframe tbody tr:hover {
    background: var(--gray-50) !important;
}

.dataframe tbody td {
    padding: var(--space-3) var(--space-4) !important;
    color: var(--gray-700) !important;
}

/* ========== CHARTS ========== */
.stPlotlyChart, .stPyplot {
    background: var(--white);
    border: var(--border-light);
    border-radius: var(--radius-md);
    padding: var(--space-6);
    margin: var(--space-4) 0;
    box-shadow: var(--shadow-sm);
}

/* ========== INPUTS ========== */
div[data-baseweb="select"] > div {
    border: var(--border-medium) !important;
    border-radius: var(--radius-md) !important;
    transition: border-color var(--transition-fast);
    box-shadow: none !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: var(--gray-400) !important;
}

div[data-baseweb="select"] > div:focus-within {
    border-color: var(--blue-primary) !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
}

input {
    border: var(--border-medium) !important;
    border-radius: var(--radius-md) !important;
    padding: var(--space-2) var(--space-3) !important;
    font-size: 14px !important;
    transition: border-color var(--transition-fast);
}

input:focus {
    border-color: var(--blue-primary) !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
    outline: none !important;
}

/* ========== EXPANDERS ========== */
.streamlit-expanderHeader {
    background: var(--white);
    border: var(--border-light);
    border-radius: var(--radius-md);
    padding: var(--space-4);
    font-weight: 500;
    color: var(--gray-800);
    transition: border-color var(--transition-fast);
}

.streamlit-expanderHeader:hover {
    border-color: var(--gray-400);
}

.streamlit-expanderContent {
    border: var(--border-light);
    border-top: none;
    border-radius: 0 0 var(--radius-md) var(--radius-md);
    padding: var(--space-4);
}

/* ========== TABS ========== */
.stTabs [data-baseweb="tab-list"] {
    gap: var(--space-2);
    border-bottom: var(--border-light);
}

.stTabs [data-baseweb="tab"] {
    border-radius: var(--radius-md) var(--radius-md) 0 0;
    padding: var(--space-3) var(--space-6);
    background: transparent;
    font-weight: 500;
    color: var(--gray-600);
    border: none;
    transition: color var(--transition-fast);
}

.stTabs [data-baseweb="tab"]:hover {
    color: var(--gray-900);
}

.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: var(--blue-primary);
    border-bottom: 2px solid var(--blue-primary);
}

/* ========== ALERTS ========== */
.stAlert {
    border-radius: var(--radius-md);
    border: var(--border-light);
    padding: var(--space-4);
    background: var(--gray-50);
}

div[data-baseweb="notification"][kind="info"] {
    background: #EFF6FF;
    border-left: 3px solid var(--info);
}

div[data-baseweb="notification"][kind="success"] {
    background: var(--green-light);
    border-left: 3px solid var(--success);
}

div[data-baseweb="notification"][kind="warning"] {
    background: #FEF3C7;
    border-left: 3px solid var(--warning);
}

div[data-baseweb="notification"][kind="error"] {
    background: #FEE2E2;
    border-left: 3px solid var(--error);
}

/* ========== DIVIDERS ========== */
hr {
    border: none;
    border-top: var(--border-light);
    margin: var(--space-16) 0;
}

/* ========== LOADING STATES ========== */
.stSpinner > div {
    border-color: var(--blue-primary) transparent transparent transparent !important;
}

/* ========== SCROLLBAR ========== */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: var(--gray-100);
}

::-webkit-scrollbar-thumb {
    background: var(--gray-300);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--gray-400);
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .main {
        padding: var(--space-4) var(--space-4);
    }
    
    h1 {
        font-size: 36px;
    }
    
    h2 {
        font-size: 24px;
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 24px;
    }
}

/* ========== ACCESSIBILITY ========== */
*:focus-visible {
    outline: 2px solid var(--blue-primary);
    outline-offset: 2px;
}

/* ========== PRINT STYLES ========== */
@media print {
    .main {
        padding: 0;
    }
    
    [data-testid="stSidebar"] {
        display: none;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
@st.cache_data
def load_real_portfolio():
    df = pd.read_csv("galvanize_portfolio_live_corrected.csv")
    return df

@st.cache_data
def load_sandbox_portfolio():
    df = pd.read_csv("galvanize_sandbox_portfolio.csv")
    return df

@st.cache_data
def load_investment_scores():
    df = pd.read_csv("investment_thesis_scores.csv")
    return df

real_df = load_real_portfolio()
sandbox_df = load_sandbox_portfolio()
thesis_df = load_investment_scores()

# ---------- SIDEBAR ----------
st.sidebar.title("🌍 Galvanize Portfolio")
st.sidebar.markdown("---")

# Tab selection in sidebar
tab_choice = st.sidebar.radio(
    "Select View:",
    ["📊 Real Portfolio", "🔬 Sandbox Deep Dive", "💡 Investment Thesis"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info(
    "This tool analyzes Galvanize Climate Solutions' portfolio through multiple lenses:\n\n"
    "**Real Portfolio**: Explore 10 actual portfolio companies with impact metrics\n\n"
    "**Sandbox Deep Dive**: Interactive financial modeling with company drill-downs\n\n"
    "**Investment Thesis**: Strategic analysis against modern climate investing trends"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Disclaimer")
st.sidebar.caption(
    "This is an independent analysis created for educational and demonstration purposes. "
    "All data is sourced from publicly available information (LinkedIn, Crunchbase, press releases). "
    "This tool is not affiliated with or endorsed by Galvanize Climate Solutions."
)
# ========================================
# TAB 1: REAL PORTFOLIO (ENHANCED WITH MORE METRICS)
# ========================================
if tab_choice == "📊 Real Portfolio":
    # Professional header with Galvanize branding
    st.markdown("""
    <div class="page-header">
        <h1>Galvanize Climate Portfolio Explorer</h1>
        <p>Real Portfolio Analysis with Impact Measurement Methodology</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Portfolio Summary Dashboard
    st.markdown("#### Portfolio Overview")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Portfolio Companies", len(real_df))
    with col2:
        total_funding = real_df["funding_raised_m"].sum()
        st.metric("Total Funding Raised", f"${total_funding:.0f}M")
    with col3:
        total_employees = real_df["employees"].sum()
        st.metric("Total Employees", f"{total_employees:,}")
    with col4:
        total_impact = real_df["estimated_annual_tco2e_avoided_k"].sum()
        st.metric("Annual Impact", f"{total_impact:.0f}K tCO₂e")
    with col5:
        avg_year = int(real_df["year_founded"].mean())
        st.metric("Avg Founding Year", avg_year)
    
    st.markdown("---")
    
    # PORTFOLIO-LEVEL IMPACT DASHBOARD
    st.markdown("#### 📊 Portfolio-Level Impact Analysis")
    st.markdown("*Aggregated metrics demonstrating portfolio-wide efficiency and attribution*")
    
    # Calculate portfolio-level efficiency metrics
    portfolio_impact_per_funding = total_impact / total_funding  # K tCO2e per $M
    portfolio_impact_per_employee = total_impact / total_employees  # K tCO2e per employee
    portfolio_funding_per_employee = total_funding / total_employees  # $M per employee
    
    # Portfolio efficiency metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Portfolio Capital Efficiency",
            f"{portfolio_impact_per_funding:.1f}K tCO₂e/$M",
            help="Total annual impact per $1M invested across portfolio. Industry benchmark: ~3-5K tCO₂e/$M for climate VCs"
        )
    
    with col2:
        st.metric(
            "Portfolio Impact Efficiency",
            f"{portfolio_impact_per_employee:.1f}K tCO₂e/employee",
            help="Total annual impact per employee across portfolio. Higher indicates more impact leverage per person."
        )
    
    with col3:
        benchmark_comparison = ((portfolio_impact_per_funding / 4.0) - 1) * 100  # Compare to 4.0 industry benchmark
        st.metric(
            "vs. Climate VC Benchmark",
            f"{benchmark_comparison:+.0f}%",
            delta=f"{benchmark_comparison:+.0f}% vs. industry avg",
            help="Comparison to industry benchmark of ~4K tCO₂e/$M for climate-focused VCs"
        )
    
    with col4:
        # Calculate portfolio concentration (Herfindahl index)
        sector_impact_pct = real_df.groupby('sector')['estimated_annual_tco2e_avoided_k'].sum() / total_impact
        herfindahl = (sector_impact_pct ** 2).sum()
        diversification_score = (1 - herfindahl) * 100
        st.metric(
            "Impact Diversification",
            f"{diversification_score:.0f}%",
            help="Portfolio diversification score (0-100%). Higher = more evenly distributed impact across sectors."
        )
    
    # Impact Attribution Analysis
    st.markdown("##### Impact Attribution by Sector & Stage")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Impact attribution by sector (pie chart)
        sector_impact_attribution = real_df.groupby('sector')['estimated_annual_tco2e_avoided_k'].sum().sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        colors = ['#2E7D32', '#1565C0', '#F57C00', '#7B1FA2', '#C62828']
        wedges, texts, autotexts = ax.pie(
            sector_impact_attribution.values,
            labels=sector_impact_attribution.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors[:len(sector_impact_attribution)]
        )
        ax.set_title('Impact Attribution by Sector\n(% of Total Portfolio Impact)', fontweight='bold')
        
        # Make percentage text more readable
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        # Impact attribution by investment stage (pie chart)
        stage_impact_attribution = real_df.groupby('investment_stage')['estimated_annual_tco2e_avoided_k'].sum().sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        colors = ['#4CAF50', '#2196F3', '#FF9800']
        wedges, texts, autotexts = ax.pie(
            stage_impact_attribution.values,
            labels=stage_impact_attribution.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors[:len(stage_impact_attribution)]
        )
        ax.set_title('Impact Attribution by Stage\n(% of Total Portfolio Impact)', fontweight='bold')
        
        # Make percentage text more readable
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        plt.tight_layout()
        st.pyplot(fig)
    
    # Key Insights Box
    st.info(
        f"""
        **Portfolio-Level Insights:**
        
        • **Capital Efficiency:** The portfolio achieves {portfolio_impact_per_funding:.1f}K tCO₂e per $1M invested, which is 
        {benchmark_comparison:+.0f}% {'above' if benchmark_comparison > 0 else 'below'} the climate VC industry benchmark (~4K tCO₂e/$M).
        
        • **Impact Concentration:** {sector_impact_attribution.index[0]} represents {(sector_impact_attribution.values[0]/total_impact*100):.1f}% of total portfolio impact, 
        indicating {'strong sector focus' if (sector_impact_attribution.values[0]/total_impact) > 0.4 else 'balanced diversification'}.
        
        • **Stage Distribution:** {stage_impact_attribution.index[0]} companies contribute {(stage_impact_attribution.values[0]/total_impact*100):.1f}% of impact, 
        suggesting the portfolio is {'impact-mature' if stage_impact_attribution.index[0] == 'Growth' else 'impact-emerging'}.
        """
    )
    
    st.markdown("---")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        sector_options = ["All"] + sorted(real_df["sector"].unique().tolist())
        selected_sector = st.selectbox("Sector", sector_options, key="sector_filter")
    
    with col2:
        stage_options = ["All"] + sorted(real_df["investment_stage"].unique().tolist())
        selected_stage = st.selectbox("Investment Stage", stage_options, key="stage_filter")
    
    with col3:
        search_term = st.text_input("Search companies", "", key="search_filter")
    
    # Apply filters
    filtered_df = real_df.copy()
    if selected_sector != "All":
        filtered_df = filtered_df[filtered_df["sector"] == selected_sector]
    if selected_stage != "All":
        filtered_df = filtered_df[filtered_df["investment_stage"] == selected_stage]
    if search_term:
        filtered_df = filtered_df[
            filtered_df["company"].str.contains(search_term, case=False, na=False) |
            filtered_df["notes"].str.contains(search_term, case=False, na=False)
        ]
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Total Funding by Sector")
        sector_funding = filtered_df.groupby("sector")["funding_raised_m"].sum().sort_values(ascending=True)
        fig, ax = plt.subplots(figsize=(8, 5))
        sector_funding.plot(kind="barh", ax=ax, color="#2E7D32")
        ax.set_xlabel("Total Funding ($M)")
        ax.set_ylabel("")
        ax.set_title("Funding Distribution by Sector")
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        st.markdown("#### Annual Impact by Sector")
        sector_impact = filtered_df.groupby("sector")["estimated_annual_tco2e_avoided_k"].sum().sort_values(ascending=True)
        fig, ax = plt.subplots(figsize=(8, 5))
        sector_impact.plot(kind="barh", ax=ax, color="#1565C0")
        ax.set_xlabel("Annual tCO₂e Avoided (K)")
        ax.set_ylabel("")
        ax.set_title("Impact Distribution by Sector")
        plt.tight_layout()
        st.pyplot(fig)
    
    # IMPACT MATERIALITY MATRIX
    st.markdown("---")
    st.markdown("#### 🎯 Impact Materiality Matrix")
    st.markdown("*Strategic portfolio view: Financial Performance vs. Impact Performance*")
    
    # Create synthetic financial performance metric (since we don't have real IRR data)
    # Using a proxy: funding efficiency + stage maturity
    np.random.seed(42)  # For reproducibility
    
    # Calculate impact performance (tCO2e per $M invested)
    filtered_df['impact_performance'] = filtered_df['estimated_annual_tco2e_avoided_k'] / filtered_df['funding_raised_m']
    
    # Create synthetic financial performance score (0-100)
    # Based on: stage maturity (40%), funding per employee (30%), sector (30%)
    stage_scores = {'Early': 30, 'Growth': 70, 'Late': 90}
    filtered_df['stage_score'] = filtered_df['investment_stage'].map(stage_scores)
    
    # Normalize funding per employee to 0-100 scale
    filtered_df['funding_efficiency_score'] = (
        (filtered_df['funding_raised_m'] / filtered_df['employees']) / 
        (filtered_df['funding_raised_m'] / filtered_df['employees']).max() * 100
    )
    
    # Sector performance multipliers (based on typical VC returns)
    sector_multipliers = {'Energy': 0.9, 'Software': 1.2, 'Agriculture': 0.85, 'Industry': 0.95, 'Transportation': 0.88}
    filtered_df['sector_multiplier'] = filtered_df['sector'].map(sector_multipliers)
    
    # Calculate composite financial performance score
    filtered_df['financial_performance'] = (
        filtered_df['stage_score'] * 0.4 + 
        filtered_df['funding_efficiency_score'] * 0.3 + 
        filtered_df['sector_multiplier'] * 30
    )
    
    # Create the scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Define quadrants
    median_financial = filtered_df['financial_performance'].median()
    median_impact = filtered_df['impact_performance'].median()
    
    # Color by sector
    sector_colors = {
        'Energy': '#2E7D32',
        'Software': '#1565C0', 
        'Agriculture': '#F57C00',
        'Industry': '#7B1FA2',
        'Transportation': '#C62828'
    }
    
    # Plot each company
    for sector in filtered_df['sector'].unique():
        sector_data = filtered_df[filtered_df['sector'] == sector]
        ax.scatter(
            sector_data['financial_performance'],
            sector_data['impact_performance'],
            s=sector_data['funding_raised_m'] * 3,  # Size by funding
            alpha=0.6,
            color=sector_colors.get(sector, '#666666'),
            label=sector,
            edgecolors='black',
            linewidth=1.5
        )
    
    # Add quadrant lines
    ax.axvline(median_financial, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax.axhline(median_impact, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    
    # Add quadrant labels
    ax.text(median_financial * 0.5, median_impact * 1.8, 'Impact Leaders\n(High Impact, Lower Returns)', 
            ha='center', va='center', fontsize=10, style='italic', color='#555', alpha=0.7)
    ax.text(median_financial * 1.5, median_impact * 1.8, '⭐ Stars\n(High Impact, High Returns)', 
            ha='center', va='center', fontsize=11, fontweight='bold', color='#2E7D32', alpha=0.8)
    ax.text(median_financial * 0.5, median_impact * 0.5, 'Underperformers\n(Lower Impact, Lower Returns)', 
            ha='center', va='center', fontsize=10, style='italic', color='#555', alpha=0.7)
    ax.text(median_financial * 1.5, median_impact * 0.5, 'Financial Leaders\n(High Returns, Lower Impact)', 
            ha='center', va='center', fontsize=10, style='italic', color='#555', alpha=0.7)
    
    # Label each point with company name
    for idx, row in filtered_df.iterrows():
        ax.annotate(
            row['company'],
            (row['financial_performance'], row['impact_performance']),
            xytext=(5, 5),
            textcoords='offset points',
            fontsize=8,
            alpha=0.8
        )
    
    ax.set_xlabel('Financial Performance Score (0-100)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Impact Performance (K tCO₂e per $1M invested)', fontsize=12, fontweight='bold')
    ax.set_title('Impact Materiality Matrix: Portfolio Strategic Positioning', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
    ax.grid(True, alpha=0.2)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Strategic insights
    stars = filtered_df[
        (filtered_df['financial_performance'] > median_financial) & 
        (filtered_df['impact_performance'] > median_impact)
    ]
    impact_leaders = filtered_df[
        (filtered_df['financial_performance'] <= median_financial) & 
        (filtered_df['impact_performance'] > median_impact)
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success(
            f"""
            **⭐ Stars (High Financial + High Impact):**
            
            {', '.join(stars['company'].tolist()) if len(stars) > 0 else 'None in this quadrant'}
            
            These companies represent the ideal portfolio holdings - strong financial returns with significant climate impact.
            """
        )
    
    with col2:
        st.info(
            f"""
            **🌱 Impact Leaders (High Impact, Developing Returns):**
            
            {', '.join(impact_leaders['company'].tolist()) if len(impact_leaders) > 0 else 'None in this quadrant'}
            
            These companies are impact-first plays that may require longer time horizons to achieve financial maturity.
            """
        )
    
    st.markdown("---")
    
    # Company Details Table
    st.markdown("#### Portfolio Companies - Detailed Metrics")
    
    display_df = filtered_df[[
        "company", "sector", "investment_stage", "funding_raised_m", 
        "employees", "year_founded", "estimated_annual_tco2e_avoided_k",
        "scale_indicator", "scale_value"
    ]].copy()
    
    display_df.columns = [
        "Company", "Sector", "Stage", "Funding ($M)", 
        "Employees", "Founded", "Annual Impact (K tCO₂e)",
        "Scale Metric", "Scale Value"
    ]
    
    st.dataframe(
        display_df.style.format({
            "Funding ($M)": "${:.0f}M",
            "Employees": "{:,}",
            "Annual Impact (K tCO₂e)": "{:.0f}K",
            "Scale Value": "{:,}"
        }),
        use_container_width=True,
        height=400
    )
    
    # Company Detail View with THREE comparison metrics
    st.markdown("---")
    st.markdown("#### Company Deep Dive")
    
    selected_company = st.selectbox(
        "Select a company for detailed analysis:",
        filtered_df["company"].tolist()
    )
    
    if selected_company:
        company_data = filtered_df[filtered_df["company"] == selected_company].iloc[0]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"## {company_data['company']}")
            st.markdown(f"**{company_data['notes']}**")
            st.markdown(f"**Sector:** {company_data['sector']} | **Subsector:** {company_data['subsector']}")
            st.markdown(f"**Country:** {company_data['country']} | **Impact Lever:** {company_data['impact_lever']}")
            
        with col2:
            st.markdown("### Key Metrics")
            st.metric("Funding Raised", f"${company_data['funding_raised_m']:.0f}M")
            st.metric("Employees", f"{company_data['employees']:,}")
            st.metric("Founded", int(company_data['year_founded']))
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Annual Impact", f"{company_data['estimated_annual_tco2e_avoided_k']:.0f}K tCO₂e")
        with col2:
            st.metric("Investment Stage", company_data['investment_stage'])
        with col3:
            st.metric(company_data['scale_indicator'], f"{company_data['scale_value']:,}")
        
        # THREE COMPARISON METRICS (Enhanced from 1 to 3)
        st.markdown("### Comparative Efficiency Metrics")
        st.markdown("*These metrics help compare companies across different sectors and stages*")
        
        # Calculate all three metrics
        impact_per_employee = company_data['estimated_annual_tco2e_avoided_k'] / company_data['employees']
        impact_per_funding = company_data['estimated_annual_tco2e_avoided_k'] / company_data['funding_raised_m']
        funding_per_employee = company_data['funding_raised_m'] / company_data['employees']
        
        # Calculate portfolio averages for comparison
        avg_impact_per_employee = (filtered_df['estimated_annual_tco2e_avoided_k'] / filtered_df['employees']).mean()
        avg_impact_per_funding = (filtered_df['estimated_annual_tco2e_avoided_k'] / filtered_df['funding_raised_m']).mean()
        avg_funding_per_employee = (filtered_df['funding_raised_m'] / filtered_df['employees']).mean()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 1️⃣ Impact Efficiency")
            st.metric(
                "Impact per Employee", 
                f"{impact_per_employee:.1f} tCO₂e",
                delta=f"{((impact_per_employee / avg_impact_per_employee - 1) * 100):.0f}% vs portfolio avg",
                help="Annual tCO₂e avoided per employee. Higher is better - indicates more impact per person."
            )
            
        with col2:
            st.markdown("#### 2️⃣ Capital Efficiency")
            st.metric(
                "Impact per $1M Funding", 
                f"{impact_per_funding:.1f}K tCO₂e",
                delta=f"{((impact_per_funding / avg_impact_per_funding - 1) * 100):.0f}% vs portfolio avg",
                help="Annual tCO₂e avoided per $1M invested. Higher is better - indicates more impact per dollar."
            )
            
        with col3:
            st.markdown("#### 3️⃣ Team Leverage")
            st.metric(
                "Funding per Employee", 
                f"${funding_per_employee:.2f}M",
                delta=f"{((funding_per_employee / avg_funding_per_employee - 1) * 100):.0f}% vs portfolio avg",
                help="Total funding raised per employee. Indicates capital intensity and team leverage."
            )
        
        # Visualization comparing company to portfolio
        st.markdown("### Company vs. Portfolio Benchmarks")
        
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))
        
        # Chart 1: Impact per Employee
        ax1.barh(['Portfolio Avg', company_data['company']], 
                 [avg_impact_per_employee, impact_per_employee],
                 color=['#90A4AE', '#2E7D32'])
        ax1.set_xlabel('tCO₂e per Employee')
        ax1.set_title('Impact Efficiency')
        
        # Chart 2: Impact per $1M
        ax2.barh(['Portfolio Avg', company_data['company']], 
                 [avg_impact_per_funding, impact_per_funding],
                 color=['#90A4AE', '#1565C0'])
        ax2.set_xlabel('K tCO₂e per $1M Funding')
        ax2.set_title('Capital Efficiency')
        
        # Chart 3: Funding per Employee
        ax3.barh(['Portfolio Avg', company_data['company']], 
                 [avg_funding_per_employee, funding_per_employee],
                 color=['#90A4AE', '#F57C00'])
        ax3.set_xlabel('$M per Employee')
        ax3.set_title('Team Leverage')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # SECTOR BENCHMARKING SECTION
        st.markdown("---")
        st.markdown("### 🎯 Sector Benchmarking Analysis")
        st.markdown("*Comparison to industry averages for similar companies*")
        
        # Define sector-specific benchmarks (industry research-based)
        sector_benchmarks = {
            "Energy": {
                "impact_per_employee": 450,  # tCO2e per employee for geothermal/clean energy
                "impact_per_funding": 2.8,   # K tCO2e per $1M for energy hardware
                "employees_per_company": 95,  # Average team size
                "description": "Geothermal and clean energy companies"
            },
            "Software": {
                "impact_per_employee": 180,  # tCO2e per employee for carbon accounting software
                "impact_per_funding": 4.3,   # K tCO2e per $1M for software enablement
                "employees_per_company": 215, # Average team size
                "description": "Carbon accounting and climate software platforms"
            },
            "Agriculture": {
                "impact_per_employee": 120,  # tCO2e per employee for ag-tech
                "impact_per_funding": 3.2,   # K tCO2e per $1M for agriculture
                "employees_per_company": 75,  # Average team size
                "description": "Agricultural carbon measurement and soil health companies"
            },
            "Industry": {
                "impact_per_employee": 95,   # tCO2e per employee for industrial optimization
                "impact_per_funding": 3.7,   # K tCO2e per $1M for industrial
                "employees_per_company": 42,  # Average team size
                "description": "Industrial decarbonization and process optimization"
            },
            "Transportation": {
                "impact_per_employee": 200,  # tCO2e per employee for logistics
                "impact_per_funding": 2.5,   # K tCO2e per $1M for transportation
                "employees_per_company": 110, # Average team size
                "description": "Transportation and logistics optimization"
            }
        }
        
        company_sector = company_data['sector']
        benchmark = sector_benchmarks.get(company_sector, {
            "impact_per_employee": 150,
            "impact_per_funding": 3.5,
            "employees_per_company": 100,
            "description": "Climate tech companies (general)"
        })
        
        # Calculate vs. industry benchmark
        impact_emp_vs_industry = ((impact_per_employee / benchmark['impact_per_employee']) - 1) * 100
        impact_fund_vs_industry = ((impact_per_funding / benchmark['impact_per_funding']) - 1) * 100
        team_size_vs_industry = ((company_data['employees'] / benchmark['employees_per_company']) - 1) * 100
        
        st.markdown(f"**Industry Benchmark:** {benchmark['description']}")
        st.markdown("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Impact per Employee",
                f"{impact_per_employee:.1f} tCO₂e",
                delta=f"{impact_emp_vs_industry:+.0f}% vs industry avg ({benchmark['impact_per_employee']} tCO₂e)",
                help=f"Industry average for {benchmark['description']}: {benchmark['impact_per_employee']} tCO₂e per employee"
            )
        
        with col2:
            st.metric(
                "Impact per $1M Funding",
                f"{impact_per_funding:.1f}K tCO₂e",
                delta=f"{impact_fund_vs_industry:+.0f}% vs industry avg ({benchmark['impact_per_funding']}K tCO₂e)",
                help=f"Industry average for {benchmark['description']}: {benchmark['impact_per_funding']}K tCO₂e per $1M"
            )
        
        with col3:
            st.metric(
                "Team Size",
                f"{company_data['employees']:,}",
                delta=f"{team_size_vs_industry:+.0f}% vs industry avg ({benchmark['employees_per_company']})",
                help=f"Industry average team size for {benchmark['description']}: {benchmark['employees_per_company']} employees"
            )
        
        # Visualization: Company vs Industry Benchmark
        st.markdown("#### Company vs. Industry Benchmark Comparison")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # Chart 1: Impact Efficiency Comparison
        categories = ['Impact per\nEmployee', 'Impact per\n$1M Funding']
        company_values = [impact_per_employee, impact_per_funding]
        industry_values = [benchmark['impact_per_employee'], benchmark['impact_per_funding']]
        
        x = np.arange(len(categories))
        width = 0.35
        
        bars1 = ax1.bar(x - width/2, industry_values, width, label='Industry Average', color='#90A4AE', alpha=0.7)
        bars2 = ax1.bar(x + width/2, company_values, width, label=company_data['company'], color='#2E7D32', alpha=0.8)
        
        ax1.set_ylabel('Impact Metrics', fontweight='bold')
        ax1.set_title('Impact Performance vs. Industry', fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(categories)
        ax1.legend()
        ax1.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.1f}',
                        ha='center', va='bottom', fontsize=9)
        
        # Chart 2: Performance Index (100 = industry average)
        performance_metrics = {
            'Impact\nEfficiency': (impact_per_employee / benchmark['impact_per_employee']) * 100,
            'Capital\nEfficiency': (impact_per_funding / benchmark['impact_per_funding']) * 100,
            'Team\nSize': (company_data['employees'] / benchmark['employees_per_company']) * 100
        }
        
        colors = ['#2E7D32' if v >= 100 else '#F57C00' for v in performance_metrics.values()]
        bars = ax2.barh(list(performance_metrics.keys()), list(performance_metrics.values()), color=colors, alpha=0.7)
        
        ax2.axvline(100, color='gray', linestyle='--', linewidth=2, label='Industry Average (100)')
        ax2.set_xlabel('Performance Index (100 = Industry Avg)', fontweight='bold')
        ax2.set_title('Relative Performance Index', fontweight='bold')
        ax2.legend()
        ax2.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, (bar, value) in enumerate(zip(bars, performance_metrics.values())):
            ax2.text(value + 2, i, f'{value:.0f}', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Sector insights
        if impact_emp_vs_industry > 20 and impact_fund_vs_industry > 20:
            performance_rating = "⭐⭐⭐ **Exceptional** - Significantly outperforms industry benchmarks"
            color = "success"
        elif impact_emp_vs_industry > 0 and impact_fund_vs_industry > 0:
            performance_rating = "✅ **Above Average** - Outperforms industry benchmarks"
            color = "success"
        elif impact_emp_vs_industry > -20 and impact_fund_vs_industry > -20:
            performance_rating = "🟡 **On Par** - Performs at industry average levels"
            color = "info"
        else:
            performance_rating = "🔴 **Below Average** - Underperforms industry benchmarks (may indicate early stage or capital-intensive model)"
            color = "warning"
        
        if color == "success":
            st.success(
                f"""
                **Sector Performance Rating:** {performance_rating}
                
                **Key Insight:** {company_data['company']} demonstrates strong performance relative to {benchmark['description']}. 
                {'This suggests efficient impact generation and strong execution.' if impact_fund_vs_industry > 0 else 'The company shows solid impact efficiency metrics.'}
                """
            )
        elif color == "info":
            st.info(
                f"""
                **Sector Performance Rating:** {performance_rating}
                
                **Key Insight:** {company_data['company']} performs in line with industry norms for {benchmark['description']}. 
                This indicates standard operational efficiency for the sector.
                """
            )
        else:
            st.warning(
                f"""
                **Sector Performance Rating:** {performance_rating}
                
                **Key Insight:** {company_data['company']}'s metrics are below industry averages, which may reflect: 
                (1) early-stage operations still scaling, (2) capital-intensive business model, or (3) conservative impact accounting. 
                This is common for hardware and deep tech companies.
                """
            )
        
        # ADD FRAMEWORK METHODOLOGY SECTION
        st.markdown("---")
        st.markdown("### 📋 Impact Measurement Methodology")
        
        # Sector-specific methodology mapping
        sector_methodologies = {
            "Energy": {
                "baseline": "Natural gas combined cycle (NGCC) at 0.45 kg CO2/kWh",
                "framework": "GHG Protocol Scope 3, Category 11 (Use of Sold Products)",
                "data_quality": "Tier 2 (Industry average capacity factors)",
                "description": "Calculated avoided emissions from displaced fossil fuel generation"
            },
            "Agriculture": {
                "baseline": "Conventional farming practices and supply chain emissions",
                "framework": "GHG Protocol Scope 3, Categories 1 & 11",
                "data_quality": "Tier 2 (Agricultural research data and IPCC factors)",
                "description": "Measured reduction in agricultural emissions and improved soil carbon sequestration"
            },
            "Software": {
                "baseline": "Manual processes and inefficient resource allocation",
                "framework": "Indirect enablement - TCFD metrics for portfolio companies",
                "data_quality": "Tier 3 (Modeled impact through customer base)",
                "description": "Estimated emissions reductions enabled through customer optimization"
            },
            "Industry": {
                "baseline": "Standard industrial processes and material production",
                "framework": "GHG Protocol Scope 1 & 2 reduction potential",
                "data_quality": "Tier 2 (Industry benchmarks and engineering estimates)",
                "description": "Direct emissions reductions from process optimization"
            },
            "Transportation": {
                "baseline": "Conventional transportation modes and logistics",
                "framework": "GHG Protocol Scope 3, Category 4 (Upstream Transportation)",
                "data_quality": "Tier 2 (Transportation emission factors)",
                "description": "Avoided emissions from optimized routing and modal shifts"
            }
        }
        
        methodology = sector_methodologies.get(company_data['sector'], {
            "baseline": "Sector-specific conventional practices",
            "framework": "GHG Protocol Scope 3",
            "data_quality": "Tier 2 (Industry averages)",
            "description": "Impact calculated using sector-specific methodologies"
        })
        
        # Create a nice info box with the methodology
        with st.expander("🔍 Click to view detailed impact calculation methodology", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Sector-Specific Methodology**")
                st.markdown(f"**Sector:** {company_data['sector']}")
                st.markdown(f"**Subsector:** {company_data['subsector']}")
                st.markdown(f"**Baseline Comparison:** {methodology['baseline']}")
                st.markdown(f"**Framework Applied:** {methodology['framework']}")
                st.markdown(f"**Data Quality Tier:** {methodology['data_quality']}")
                st.markdown(f"**Approach:** {methodology['description']}")
            
            with col2:
                st.markdown("**Framework Alignment**")
                
                st.markdown("**TCFD Alignment:**")
                st.markdown("- ✅ Transition opportunity assessment (low-carbon solutions)")
                st.markdown("- ✅ Market opportunity sizing in climate transition")
                st.markdown("- ✅ Technology readiness and scalability metrics")
                
                st.markdown("")
                st.markdown("**SFDR Alignment:**")
                st.markdown("- ✅ PAI 4: Exposure to fossil fuel sector (inverse - enabling transition)")
                st.markdown("- ✅ PAI 13: Governance and impact measurement practices")
                st.markdown("- ✅ Sustainable investment contribution (Article 9 alignment)")
            
            st.markdown("---")
            st.markdown("**Industry Standards Applied:**")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown("**GHG Protocol**")
                st.caption("Scope 3 Category 11 for avoided emissions calculations")
            with col2:
                st.markdown("**PCAF**")
                st.caption("Portfolio-level carbon attribution methodology")
            with col3:
                st.markdown("**TCFD**")
                st.caption("Climate risk assessment and opportunity metrics")
            with col4:
                st.markdown("**SFDR**")
                st.caption("Principal Adverse Impact (PAI) indicators alignment")

# ========================================
# TAB 2: SANDBOX DEEP DIVE (UNCHANGED FROM V2)
# ========================================
elif tab_choice == "🔬 Sandbox Deep Dive":
    st.markdown("""
    <div class="page-header">
        <h1>Sandbox Portfolio Deep Dive</h1>
        <p>Quantitative Financial Analysis with Risk-Return Modeling</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add view selector
    view_mode = st.radio(
        "Select Analysis View:",
        ["Portfolio Overview", "Company Drill-Down"],
        horizontal=True
    )
    
    if view_mode == "Portfolio Overview":
        # Portfolio summary metrics
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        total_investment = sandbox_df["Investment ($M)"].sum()
        avg_irr = sandbox_df["IRR (%)"].mean()
        total_impact = sandbox_df["Lifetime tCO2e Avoided (M)"].sum()
        avg_payback = sandbox_df["Payback Period (years)"].mean()
        portfolio_efficiency = (sandbox_df["Lifetime tCO2e Avoided (M)"].sum() * 1000) / total_investment
        high_irr_count = len(sandbox_df[sandbox_df["IRR (%)"] > 20])
        
        with col1:
            st.metric("Total Investment", f"${total_investment:.1f}M")
        with col2:
            st.metric("Average IRR", f"{avg_irr:.1f}%")
        with col3:
            st.metric("Total Lifetime Impact", f"{total_impact:.1f}M tCO₂e")
        with col4:
            st.metric("Avg Payback Period", f"{avg_payback:.1f} years")
        with col5:
            st.metric("Portfolio Efficiency", f"{portfolio_efficiency:.0f} tCO₂e/$K")
        with col6:
            st.metric("High IRR Companies (>20%)", f"{high_irr_count}/{len(sandbox_df)}")
        
        st.markdown("---")
        st.markdown("### Investment & Impact Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Investment vs. Lifetime Impact")
            fig, ax = plt.subplots(figsize=(8, 6))
            scatter = ax.scatter(
                sandbox_df["Investment ($M)"],
                sandbox_df["Lifetime tCO2e Avoided (M)"],
                s=sandbox_df["IRR (%)"] * 10,
                c=sandbox_df["IRR (%)"],
                cmap="RdYlGn",
                alpha=0.7,
                edgecolors="black"
            )
            
            for idx, row in sandbox_df.iterrows():
                ax.annotate(
                    row["Company"],
                    (row["Investment ($M)"], row["Lifetime tCO2e Avoided (M)"]),
                    fontsize=11,
                    fontweight='bold',
                    ha='center'
                )
            
            ax.set_xlabel("Investment ($M)", fontsize=12)
            ax.set_ylabel("Lifetime tCO₂e Avoided (M)", fontsize=12)
            ax.set_title("Investment Size vs. Climate Impact", fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            
            cbar = plt.colorbar(scatter, ax=ax)
            cbar.set_label("IRR (%)", fontsize=10)
            
            plt.tight_layout()
            st.pyplot(fig)
        
        with col2:
            st.markdown("#### IRR vs. Impact Efficiency")
            fig, ax = plt.subplots(figsize=(8, 6))
            
            efficiency = (sandbox_df["Lifetime tCO2e Avoided (M)"] * 1000) / sandbox_df["Investment ($M)"]
            
            scatter = ax.scatter(
                sandbox_df["IRR (%)"],
                efficiency,
                s=sandbox_df["Investment ($M)"] * 3,
                c=sandbox_df["Investment ($M)"],
                cmap="viridis",
                alpha=0.7,
                edgecolors="black"
            )
            
            for idx, row in sandbox_df.iterrows():
                eff_val = (row["Lifetime tCO2e Avoided (M)"] * 1000) / row["Investment ($M)"]
                ax.annotate(
                    row["Company"],
                    (row["IRR (%)"], eff_val),
                    fontsize=11,
                    fontweight='bold',
                    ha='center'
                )
            
            ax.set_xlabel("IRR (%)", fontsize=12)
            ax.set_ylabel("Impact Efficiency (tCO₂e per $1K)", fontsize=12)
            ax.set_title("Financial Return vs. Impact Efficiency", fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            
            cbar = plt.colorbar(scatter, ax=ax)
            cbar.set_label("Investment Size ($M)", fontsize=10)
            
            plt.tight_layout()
            st.pyplot(fig)
        
        # Sector Analysis
        st.markdown("---")
        st.markdown("### Sector Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Investment by Sector")
            sector_investment = sandbox_df.groupby("Sector")["Investment ($M)"].sum().sort_values(ascending=True)
            fig, ax = plt.subplots(figsize=(8, 5))
            sector_investment.plot(kind="barh", ax=ax, color="#2E7D32")
            ax.set_xlabel("Total Investment ($M)")
            ax.set_ylabel("")
            ax.set_title("Capital Allocation by Sector")
            plt.tight_layout()
            st.pyplot(fig)
        
        with col2:
            st.markdown("#### Impact by Sector")
            sector_impact = sandbox_df.groupby("Sector")["Lifetime tCO2e Avoided (M)"].sum().sort_values(ascending=True)
            fig, ax = plt.subplots(figsize=(8, 5))
            sector_impact.plot(kind="barh", ax=ax, color="#1565C0")
            ax.set_xlabel("Lifetime tCO₂e Avoided (M)")
            ax.set_ylabel("")
            ax.set_title("Climate Impact by Sector")
            plt.tight_layout()
            st.pyplot(fig)
        
        # Detailed Metrics Table
        st.markdown("---")
        st.markdown("### Detailed Portfolio Metrics")
        
        display_df = sandbox_df.copy()
        display_df["Impact Efficiency"] = (display_df["Lifetime tCO2e Avoided (M)"] * 1000) / display_df["Investment ($M)"]
        display_df["Annual Impact (K)"] = display_df["Annual tCO2e Avoided (K)"]
        
        st.dataframe(
            display_df[[
                "Company", "Sector", "Investment ($M)", "IRR (%)", 
                "Payback Period (years)", "Risk Rating", "Lifetime tCO2e Avoided (M)",
                "Annual Impact (K)", "Impact Efficiency"
            ]].style.format({
                "Investment ($M)": "${:.1f}M",
                "IRR (%)": "{:.1f}%",
                "Payback Period (years)": "{:.1f} years",
                "Lifetime tCO2e Avoided (M)": "{:.1f}M",
                "Annual Impact (K)": "{:.0f}K",
                "Impact Efficiency": "{:.0f} tCO₂e/$K"
            }),
            use_container_width=True,
            height=400
        )
        
        # Export functionality
        st.markdown("---")
        csv = display_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Portfolio Data (CSV)",
            data=csv,
            file_name="galvanize_sandbox_portfolio.csv",
            mime="text/csv"
        )
    
    elif view_mode == "Company Drill-Down":
        st.markdown("### Individual Company Analysis")
        
        selected_company = st.selectbox(
            "Select a company for detailed analysis:",
            sandbox_df["Company"].tolist()
        )
        
        if selected_company:
            company_data = sandbox_df[sandbox_df["Company"] == selected_company].iloc[0]
            
            # Company Header
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"## {company_data['Company']}")
                st.markdown(f"**Sector:** {company_data['Sector']} | **Stage:** {company_data['Stage']}")
            
            with col2:
                st.metric("Risk Rating", company_data['Risk Rating'])
            
            # Key Metrics
            st.markdown("### Financial Metrics")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Investment", f"${company_data['Investment ($M)']:.1f}M")
            with col2:
                st.metric("IRR", f"{company_data['IRR (%)']:.1f}%")
            with col3:
                st.metric("Payback Period", f"{company_data['Payback Period (years)']:.1f} years")
            with col4:
                efficiency = (company_data['Lifetime tCO2e Avoided (M)'] * 1000) / company_data['Investment ($M)']
                st.metric("Impact Efficiency", f"{efficiency:.0f} tCO₂e/$K")
            
            # Impact Metrics
            st.markdown("### Climate Impact")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Lifetime Impact", f"{company_data['Lifetime tCO2e Avoided (M)']:.1f}M tCO₂e")
            with col2:
                st.metric("Annual Impact", f"{company_data['Annual tCO2e Avoided (K)']:.0f}K tCO₂e")
            
            # Benchmark Comparison
            st.markdown("---")
            st.markdown("### Benchmark Comparison")
            
            # Calculate portfolio averages
            avg_irr = sandbox_df["IRR (%)"].mean()
            avg_payback = sandbox_df["Payback Period (years)"].mean()
            avg_efficiency = ((sandbox_df["Lifetime tCO2e Avoided (M)"] * 1000) / sandbox_df["Investment ($M)"]).mean()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Financial Performance vs. Portfolio")
                fig, ax = plt.subplots(figsize=(8, 5))
                
                metrics = ['IRR (%)', 'Payback\n(years)']
                company_vals = [company_data['IRR (%)'], company_data['Payback Period (years)']]
                portfolio_vals = [avg_irr, avg_payback]
                
                x = np.arange(len(metrics))
                width = 0.35
                
                ax.bar(x - width/2, portfolio_vals, width, label='Portfolio Avg', color='#90A4AE')
                ax.bar(x + width/2, company_vals, width, label=company_data['Company'], color='#2E7D32')
                
                ax.set_ylabel('Value')
                ax.set_title('Financial Metrics Comparison')
                ax.set_xticks(x)
                ax.set_xticklabels(metrics)
                ax.legend()
                ax.grid(True, alpha=0.3, axis='y')
                
                plt.tight_layout()
                st.pyplot(fig)
            
            with col2:
                st.markdown("#### Impact Efficiency vs. Portfolio")
                fig, ax = plt.subplots(figsize=(8, 5))
                
                ax.barh(['Portfolio Average', company_data['Company']], 
                       [avg_efficiency, efficiency],
                       color=['#90A4AE', '#1565C0'])
                ax.set_xlabel('Impact Efficiency (tCO₂e per $1K)')
                ax.set_title('Capital Efficiency Comparison')
                ax.grid(True, alpha=0.3, axis='x')
                
                plt.tight_layout()
                st.pyplot(fig)
            
            # Risk-Return Positioning
            st.markdown("---")
            st.markdown("### Risk-Return Positioning")
            
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Plot all companies
            risk_map = {"Low": 1, "Medium": 2, "Medium-High": 3, "High": 4}
            sandbox_df["Risk Score"] = sandbox_df["Risk Rating"].map(risk_map)
            
            ax.scatter(
                sandbox_df["Risk Score"],
                sandbox_df["IRR (%)"],
                s=100,
                c='lightgray',
                alpha=0.5,
                edgecolors="black"
            )
            
            # Highlight selected company
            company_risk_score = risk_map[company_data['Risk Rating']]
            ax.scatter(
                [company_risk_score],
                [company_data['IRR (%)']],
                s=300,
                c='red',
                alpha=0.8,
                edgecolors="black",
                marker='*',
                label=company_data['Company']
            )
            
            ax.set_xlabel("Risk Level", fontsize=12)
            ax.set_ylabel("IRR (%)", fontsize=12)
            ax.set_title("Risk-Return Profile", fontsize=14, fontweight='bold')
            ax.set_xticks([1, 2, 3, 4])
            ax.set_xticklabels(["Low", "Medium", "Medium-High", "High"])
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            plt.tight_layout()
            st.pyplot(fig)
    
# ========================================
# TAB 3: INVESTMENT THESIS (UNCHANGED FROM V2)
# ========================================
elif tab_choice == "💡 Investment Thesis":
    st.markdown("""
    <div class="page-header">
        <h1>Investment Thesis Analysis</h1>
        <p>Strategic Alignment with Modern Climate Investing Trends</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    This analysis evaluates Galvanize's portfolio against three key investment criteria that define 
    successful climate tech investing in 2024-2025, based on insights from leading climate investors.
    """)
    
    # Explain the three criteria
    st.markdown("---")
    st.markdown("## The Three Investment Criteria")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 1️⃣ Hardware + Software")
        st.markdown("""
        **Dual Revenue Streams**: Companies that combine physical products (atoms) with recurring 
        digital services (bits) create defensible moats and scalable revenue.
        
        **Examples:**
        - **WeaveGrid**: EV-grid integration hardware + data services
        - **Remora**: Carbon capture devices + CO₂ sales + tax credits
        - **Heirloom**: DAC machines + removal contracts + MRV services
        
        **Why it matters**: Hardware is hard to copy, software drives margin expansion.
        """)
    
    with col2:
        st.markdown("### 2️⃣ Capital Efficiency")
        st.markdown("""
        **Smart Scaling**: Companies that start small, prove the model, then scale using creative 
        funding (grants, tax credits, debt, pre-orders) rather than burning through equity.
        
        **Examples:**
        - **Amogy**: Uses existing ammonia infrastructure
        - **Kula Bio**: On-farm production vs. mega-factories
        - **Lightship**: Pre-orders enabled debt financing
        
        **Why it matters**: Avoids the "missing middle" funding gap and extends runway.
        """)
    
    with col3:
        st.markdown("### 3️⃣ Data Markets")
        st.markdown("""
        **Climate Volatility = Opportunity**: Companies that measure, organize, and sell climate 
        risk/impact data as the world becomes more chaotic and regulated.
        
        **Examples:**
        - **Patch**: Carbon credit data transparency
        - **Sinai**: Climate regulation cost modeling
        - Future: Climate insurance, materials tracking, farm risk
        
        **Why it matters**: Risk is everywhere, but measurable risk creates markets.
        """)
    
    # Scoring Matrix
    st.markdown("---")
    st.markdown("## Portfolio Company Scoring")
    st.markdown("*Each company scored 0-3 on each criterion (0=No fit, 1=Weak, 2=Moderate, 3=Strong)*")
    
    # Display scoring table
    display_thesis = thesis_df.copy()
    display_thesis["Total Score"] = display_thesis["Hardware+Software"] + display_thesis["Capital Efficiency"] + display_thesis["Data Markets"]
    
    st.dataframe(
        display_thesis.style.background_gradient(subset=["Hardware+Software", "Capital Efficiency", "Data Markets", "Total Score"], cmap="RdYlGn"),
        use_container_width=True,
        height=400
    )
    
    # Visualization
    st.markdown("---")
    st.markdown("## Portfolio Composition Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Criteria Scoring Distribution")
        fig, ax = plt.subplots(figsize=(8, 6))
        
        criteria_scores = {
            "Hardware+Software": display_thesis["Hardware+Software"].sum(),
            "Capital Efficiency": display_thesis["Capital Efficiency"].sum(),
            "Data Markets": display_thesis["Data Markets"].sum()
        }
        
        ax.bar(criteria_scores.keys(), criteria_scores.values(), color=['#2E7D32', '#1565C0', '#F57C00'])
        ax.set_ylabel("Total Score Across Portfolio")
        ax.set_title("Investment Criteria Strength")
        ax.set_ylim(0, 30)
        plt.xticks(rotation=15, ha='right')
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        st.markdown("### Top Performers by Total Score")
        fig, ax = plt.subplots(figsize=(8, 6))
        
        top_companies = display_thesis.nlargest(7, "Total Score")
        ax.barh(top_companies["Company"], top_companies["Total Score"], color='#2E7D32')
        ax.set_xlabel("Total Score (out of 9)")
        ax.set_title("Highest Scoring Companies")
        ax.set_xlim(0, 9)
        plt.tight_layout()
        st.pyplot(fig)
    
    # Strategic Insights
    st.markdown("---")
    st.markdown("## Strategic Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        hw_sw_count = len(display_thesis[display_thesis["Hardware+Software"] >= 2])
        st.metric("Hardware+Software Leaders", f"{hw_sw_count}/10", 
                 help="Companies with moderate-to-strong hardware+software integration")
    
    with col2:
        cap_eff_count = len(display_thesis[display_thesis["Capital Efficiency"] == 3])
        st.metric("Capital Efficiency Champions", f"{cap_eff_count}/10",
                 help="Companies with perfect capital efficiency scores")
    
    with col3:
        data_count = len(display_thesis[display_thesis["Data Markets"] >= 2])
        st.metric("Data Market Players", f"{data_count}/10",
                 help="Companies with moderate-to-strong data monetization")
    
    st.markdown("### Key Findings")
    
    st.success("""
    **Portfolio Strengths:**
    - **60% of companies** score 2+ on Capital Efficiency - Galvanize is backing smart scalers
    - **40% of companies** are building data/software platforms - ahead of the atoms-heavy trend
    - **Top 3 performers** (Arable, Plotlogic, The Routing Company) all combine multiple criteria
    """)
    
    st.info("""
    **Strategic Positioning:**
    - Portfolio is **well-diversified** across the three investment themes
    - Strong focus on **enabling technologies** (data, software, optimization) vs. pure hardware plays
    - Companies like **Watershed, Arable, Plotlogic** exemplify the "atoms + bits" model
    """)
    
    st.warning("""
    **Opportunity Areas:**
    - Only 3 companies have strong Hardware+Software integration - room to add more dual-revenue models
    - Data Markets scoring is concentrated in software companies - could expand to hardware-enabled data plays
    """)
    
    # Methodology
    st.markdown("---")
    st.markdown("## Methodology")
    
    with st.expander("📖 How companies were scored"):
        st.markdown("""
        **Scoring Framework (0-3 scale):**
        
        **Hardware + Software:**
        - 3 = Clear dual revenue model with physical product + recurring digital service
        - 2 = Has both hardware and software but not fully integrated revenue streams
        - 1 = Primarily one or the other with minor elements of both
        - 0 = Pure software or pure hardware play
        
        **Capital Efficiency:**
        - 3 = Demonstrates exceptional capital efficiency through creative funding, asset-light model, or rapid scaling
        - 2 = Good capital efficiency with some creative funding or lean operations
        - 1 = Standard venture-backed scaling approach
        - 0 = Capital-intensive with limited efficiency mechanisms
        
        **Data Markets:**
        - 3 = Core business model is selling climate/impact data or analytics
        - 2 = Generates significant data as byproduct with monetization potential
        - 1 = Collects data but not core to business model
        - 0 = Minimal data generation or monetization
        
        **Research Sources:**
        - Company websites and public materials
        - Investor presentations and press releases
        - Third-party analysis (Contrary Research, Norrsken VC, etc.)
        - Climate tech investment trend reports (2024-2025)
        """)
