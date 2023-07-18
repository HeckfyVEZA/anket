import streamlit as st
try:
    flag = st.session_state.flag
except:
    flag = False
st.session_state['stage'] = 0
if st.session_state['stage'] == 0:
    st.write('hui')
cb = st.checkbox('dfhgjdhfg')
if cb:
    st.session_state['stage'] = 2
    st.session_state.flag = True
else:
    st.session_state.flag = False
