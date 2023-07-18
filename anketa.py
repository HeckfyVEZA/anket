import streamlit as st
import sys
st.write(sys.version)
match sys.version:
  case 1:
    st.write('smth')
  case _:
    st.write('else')
