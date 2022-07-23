import re   
import streamlit as st
import base64

def head():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: -35px;'>
        Train of Sardines \U0001F41F
        </h1>
    """, unsafe_allow_html=True
                )

    st.caption("""
        <p style='text-align: center'>
        For my daughter and people who commute by trains
        </p>
    """, unsafe_allow_html=True
               )
    # U0001F41F
    st.write("""
        <p style="font-size:25px";'text-align: center'>
        How packed are the trains today?
        </p>
    """, unsafe_allow_html=True
             )

    

@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def body(sample):
    name = sample.iloc[0, 0]
    link = sample.iloc[0, 1]
    prob = sample.iloc[0, 2]
    st.info(f'### {name}')
    st.write(prob)
    st.caption(f'[source]({link})')
    st.markdown('---')

def findkey(data):
    c = [list(item.values())[0] for item in data]
    clist = [re.split(r'(\d+)', item) for item in c]
    sortlist = [int(item[1]) for item in clist]
    return sortlist

def sortkey(data):
    sortlist = findkey(data)
    size = len(sortlist)
    for i in range(size):
        status = True
        for j in range(size - i - 1):
            if sortlist[j] > sortlist[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                sortlist[j], sortlist[j+1] = sortlist[j+1], sortlist[j]
            status = False
        if status:
            break
    return data



