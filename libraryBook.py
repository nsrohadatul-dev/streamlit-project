import streamlit as st

st.title("Library Book Type")
books = st.text_input("Enter number of books:")

if st.button("Display"):
    try:
        books = int(books)
        for i in range(1, books + 1):
            book_type = st.selectbox(
                "Select book type for Book " + str(i),
                ["Fiction", "Non-Fiction"]
            )
            if book_type:
                st.write("Book", i, "Type:", book_type)
            else:
                st.write("No book type selected")
    except:
        st.write("Invalid Number of Books")