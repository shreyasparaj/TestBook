import streamlit as st
from datetime import datetime

# Title of the page
st.title("Admin - Create Question Paper Form")

# Form for creating a question paper
with st.form(key="question_paper_form"):
    # Input fields
    name_english = st.text_input("Name (English)")
    name_marathi = st.text_input("Name (Marathi)")
    exam_date = st.date_input("Exam Date/Created Date", value=datetime.today())
    description_m = st.text_area("Description (Marathi)")
    description_e = st.text_area("Description (English)")
    is_previous_year = st.checkbox("Is Previous Year Paper")

    # File uploads
    uploaded_pdf = st.file_uploader("Upload Paper (Scanned PDF)", type=["pdf"])
    uploaded_word_marathi = st.file_uploader("Upload Paper (Word Doc - Marathi)", type=["doc", "docx"])
    uploaded_word_english = st.file_uploader("Upload Paper (Word Doc - English)", type=["doc", "docx"])

    # Submit button
    submit_button = st.form_submit_button(label="Save")

# Handle form submission
if submit_button:
    # Input validation
    if not name_english or not name_marathi:
        st.error("Please fill in both Name fields.")
    elif uploaded_pdf is None and (uploaded_word_marathi is None and uploaded_word_english is None):
        st.error("Please upload at least one paper (PDF or Word Document).")
    else:
        st.success("Question paper details saved successfully!")
        # Add code here to process the form data (e.g., saving to a database)
