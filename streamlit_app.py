from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


def main():
    st.title(" Prediction")
    
    menu = ["Home","Dataset"]
    choice = st.sidebar.selectboc("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home")
        
    elif choice == "Dataset":
        st.subheader("Dataset")
        
    return
    
if __name__ == '__main__':
    choice == main()
    
if choice == "Home":
    """ asghgferghgfdsdfbdfg """
elif choice == "Dataset"
    st.subheader("Dataset")
    data_file = st.file_uploader(" Upload CSV ", type=["csv"])
    if data_file is not None:
        file_details = {"filename":data_file.name, "filetype":data_file.type,
                        "filesize":data_file.size}
        st.write(file_details)
        predict_app = pd.read_csv(data_file)
        st.dataframe(predict_app)
        Input_data = data_eda(predict_app)
