import streamlit as st
a = 5
match a:
    case 5:
        st.write('yes')
    case _:
        st.write('no')
