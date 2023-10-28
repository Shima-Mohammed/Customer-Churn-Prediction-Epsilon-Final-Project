import streamlit as st

st.set_page_config(
    page_title="Telecom Customer Churn Prediction",
    page_icon="📡",
)

st.markdown(" <div style='text-align:center'><img style='  max-width: 100%;height: auto;' src='https://cdn.vectorstock.com/i/preview-1x/16/01/people-use-wireless-5g-transmitter-tower-vector-41701601.jpg'/></div>",unsafe_allow_html=True)
st.markdown(" <h1 style='text-align:center;margin-bottom:20px'>Telecom Customer Churn Prediction</h1> " , unsafe_allow_html=True) #
st.markdown(" <p style='text-align:center;margin-bottom:20px; text-wrap: pretty;'>This is our telecommunication company's web page, where you can add new customers and predict their behavior. </p> " , unsafe_allow_html=True)
st.sidebar.success("Select a page above.")