import streamlit as st

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Update session state
st.session_state['key'] = 'value4'

# Read session state
st.write(st.session_state['key'])