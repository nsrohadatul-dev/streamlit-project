import streamlit as st

st.title("Number of Books")

books = st.text_input("Enter number of books:")

if st.button("Submit"):
    try:
        books = int(books)
    except:
        st.write("Invalid Quantity")
    finally:
        st.write("Program Completed")