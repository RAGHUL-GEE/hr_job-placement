import streamlit as st


st.set_page_config(
    page_title="KPI Dashboard",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Executive Key Performance Indicators (KPIs)")
st.markdown("Overview of high-level placement, candidate evaluation, and offer acceptance metrics.")
st.markdown("---")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Candidates",
        value="51,500",
        delta="+1,200 this month"
    )

with col2:
    st.metric(
        label="Placement Rate (%)",
        value="64.96%",
        delta="+1.2%"
    )

with col3:
    st.metric(
        label="Job Acceptance Rate (%)",
        value="64.96%",
        delta="+0.8%"
    )

with col4:
    st.metric(
        label="Offers Accepted (Count)",
        value="33,456",
        delta="+450"
    )


col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric(
        label="Average Interview Score",
        value="66.05",
        delta="-0.4"
    )

with col6:
    st.metric(
        label="Average Skills Match %",
        value="73.94%",
        delta="+2.1%"
    )

with col7:
    st.metric(
        label="Offer Dropout Rate",
        value="23.13%",
        delta="-1.5%",
        delta_color="inverse"
    )

with col8:
    st.metric(
        label="High-Risk Candidate %",
        value="26.72%",
        delta="-2.0%",
        delta_color="inverse"
    )