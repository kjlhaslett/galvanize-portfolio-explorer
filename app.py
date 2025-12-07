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
    /* Main app styling */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Card-like containers for metrics */
    div[data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: 700;
        color: #1e3c72;
    }
    
    div[data-testid="stMetricLabel"] {
        font-size: 14px;
        font-weight: 500;
        color: #5a6c7d;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Rounded containers */
    div.stMarkdown, div[data-testid="stHorizontalBlock"] {
        border-radius: 12px;
    }
    
    /* Headers with better styling */
    h1 {
        color: #1e3c72;
        font-weight: 700;
        padding-bottom: 10px;
        border-bottom: 3px solid #4CAF50;
        margin-bottom: 20px;
    }
    
    h2 {
        color: #2a5298;
        font-weight: 600;
        margin-top: 30px;
    }
    
    h3 {
        color: #34495e;
        font-weight: 600;
    }
    
    /* Info boxes with rounded edges and shadows */
    .stAlert {
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #4CAF50;
    }
    
    /* Selectbox and input styling */
    div[data-baseweb="select"] > div {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    input {
        border-radius: 8px !important;
        border: 2px solid #e0e0e0 !important;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 8px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 10px 24px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* Radio buttons - MUST override sidebar white color */
    [data-testid="stSidebar"] div[role="radiogroup"] label {
        background: white;
        padding: 12px 20px;
        border-radius: 8px;
        margin: 4px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        transition: all 0.2s ease;
        color: #10b981 !important;
    }
    
    [data-testid="stSidebar"] div[role="radiogroup"] label span {
        color: #10b981 !important;
    }
    
    [data-testid="stSidebar"] div[role="radiogroup"] label p {
        color: #10b981 !important;
    }
    
    div[role="radiogroup"] label:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transform: translateY(-1px);
    }
    
    /* DataFrame styling */
    .dataframe {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Chart containers */
    .stPlotlyChart, .stPyplot {
        background: white;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        margin: 10px 0;
    }
    
    /* Dividers */
    hr {
        margin: 30px 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #4CAF50, transparent);
    }
    
    /* Metric containers */
    div[data-testid="metric-container"] {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #4CAF50;
    }
    
    /* Success/info messages */
    .stSuccess {
        background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);
        border-radius: 12px;
        padding: 15px;
        border-left: 4px solid #4CAF50;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 12px 24px;
        background: white;
        font-weight: 600;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: white;
        border-radius: 8px;
        font-weight: 600;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
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
    st.title("📊 Galvanize Climate Portfolio Explorer")
    st.markdown("### Real Portfolio Analysis with Impact Metrics")
    st.markdown("*Data verified against public sources as of December 2024*")
    
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

# ========================================
# TAB 2: SANDBOX DEEP DIVE (UNCHANGED FROM V2)
# ========================================
elif tab_choice == "🔬 Sandbox Deep Dive":
    st.title("🔬 Sandbox Portfolio Deep Dive")
    st.markdown("### Quantitative Financial Analysis (Synthetic Data)")
    
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
    st.title("💡 Investment Thesis Analysis")
    st.markdown("### Strategic Alignment with Modern Climate Investing Trends")
    
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
