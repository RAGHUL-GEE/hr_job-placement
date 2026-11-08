import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configure page settings
st.set_page_config(
    page_title="Executive KPI Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom Styling to mimic sleek dark UI
st.markdown("""
    <style>
    .stMetric {
        background-color: #1E222D;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #2D323F;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("📊 Key Performance Indicators (KPIs)")
st.markdown("High-level overview of placement analytics, candidate evaluation, and offer acceptance trends.")
st.markdown("---")

# ---------------------------------------------------------
# ROW 1: PRIMARY KPI METRICS
# ---------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Candidates", "51,500", "+1,200 this month")
c2.metric("Placement Rate", "64.96%", "+1.2%")
c3.metric("Job Acceptance Rate", "64.96%", "+0.8%")
c4.metric("Offers Accepted", "33,456", "+450")

st.markdown(" ")

c5, c6, c7, c8 = st.columns(4)
c5.metric("Avg Interview Score", "66.05", "-0.4")
c6.metric("Avg Skills Match", "73.94%", "+2.1%")
c7.metric("Offer Dropout Rate", "23.13%", "-1.5%", delta_color="inverse")
c8.metric("High-Risk Candidates", "26.72%", "-2.0%", delta_color="inverse")

st.markdown("---")

# ---------------------------------------------------------
# ROW 2: VISUAL CHARTS & DASHBOARD OVERVIEW
# ---------------------------------------------------------
col_left, col_right = st.columns(2)

# Chart 1: Donut Chart for Placement Outcome Distribution
with col_left:
    st.subheader("Placement Outcome Distribution")
    
    placement_df = pd.DataFrame({
        "Status": ["Matched", "Not Matched"],
        "Percentage": [73.7, 26.3]
    })
    
    fig_donut = px.pie(
        placement_df,
        names="Status",
        values="Percentage",
        hole=0.6,
        color="Status",
        color_discrete_map={"Matched": "#2ECC71", "Not Matched": "#E74C3C"}
    )
    
    fig_donut.update_traces(
        textposition="inside",
        textinfo="percent+label",
        marker=dict(line=dict(color="#000000", width=2))
    )
    fig_donut.update_layout(
        showlegend=True,
        margin=dict(t=30, b=0, l=0, r=0),
        height=380
    )
    
    st.plotly_chart(fig_donut, use_container_width=True)

# Chart 2: Bar Chart for Acceptance Rate by Company Tier
with col_right:
    st.subheader("Acceptance Rate by Company Tier")
    
    tier_df = pd.DataFrame({
        "Company Tier": ["Tier 1", "Tier 2", "Tier 3"],
        "Acceptance Rate (%)": [73.6, 75.3, 73.7]
    })
    
    fig_bar = px.bar(
        tier_df,
        x="Company Tier",
        y="Acceptance Rate (%)",
        color="Company Tier",
        text_auto=".1f",
        color_discrete_sequence=["#00C9A7", "#845EC2", "#FFC75F"]
    )
    
    fig_bar.update_traces(
        textposition="outside",
        cliponaxis=False
    )
    fig_bar.update_layout(
        yaxis_range=[0, 100],
        showlegend=False,
        margin=dict(t=30, b=0, l=0, r=0),
        height=380
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)