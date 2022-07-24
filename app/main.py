
import streamlit as st
from utils import currentdate
from utils import head, body
from utils import set_bg
from train_info import *
from api import api_call

st.set_page_config(
    page_title='Train of Sardines',
    page_icon=':train:',
    menu_items={"About":"Data is updated on a 10 min interval"}
)

set_bg("assets/map2.png")
head()
st.write(f"Date and Time: {currentdate()}")

select = st.selectbox("CHECK IT OUT!", list(trainline.keys()))
if select in trainline.keys():
    with st.container():
        api_call(select)

st.text("Data is updated on a 10 min interval from https://datamall.lta.gov.sg")
