import streamlit as st

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

def main():
    st.title(" Prediction")
    
    menu = ["Home","Dataset"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home")
        
    elif choice == "Dataset":
        st.subheader("Dataset")
        
    return
    
if __name__ == '__main__':
    main()
