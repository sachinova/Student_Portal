import streamlit as st

# Set page title
st.set_page_config(page_title="Student Portal", layout="wide")


L1 , L2 = st.columns([3,1])
# Title and intro
with L1:
    st.title("📘 First Year Student Portal")
    st.subheader("Welcome to the student hub for all academic essentials!")

with L2:
     st.image("images/community.jpg", width=200, caption="Join the community")


# Section: Images
st.markdown("### 🖼️ College Life Moments")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/2.jpg", caption="INFINITY CUP", use_container_width=True)

with col2:
    st.image("images/1.jpg", caption="💖", use_container_width=True)

with col3:
    st.image("images/3.jpg", caption="Supremum", use_container_width=True)

# Spacer
st.markdown("<br><br>", unsafe_allow_html=True)

# Section: Resources
st.markdown("### 📄 Academic Resources")

# Row 1: Syllabus & PYQs
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style='padding: 15px; background-color: #000000; border: 1px solid #ccc; border-radius: 10px; color: white;'>
            <h4>📚 Syllabus</h4>
            📄 <a href='https://maths.du.ac.in/NEP_Syllabi/BSc_(Hons)_Maths_UGCF2022_Sems(1-8)_Syllabus.pdf' target='_blank' style='color: white;'>
                Complete Syllabus (PDF)
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style='padding: 15px; background-color: #000000; border: 1px solid #ccc; border-radius: 10px;'>
            <h4>📝 Previous Year Question Papers (PYQs)</h4>
            📄 <a href='https://www.maitreyi.ac.in/library/resources/previous-years-question-papers' target='_blank'>
                Download PYQs PDF
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Spacer between rows
st.markdown("<br>", unsafe_allow_html=True)

# Row 2: Timetable & Assignment Templates
col3, col4 = st.columns(2)

with col3:
    st.markdown(
        """
        <div style='padding: 15px; background-color: #000000; border: 1px solid #ccc; border-radius: 10px; color: white;'>
            <h4>🕒 Timetable</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    div1, div2 = st.columns(2)
    # Button to show timetable image
    with div1:
        if st.button("📸 Show Section A Timetable Image"):
            st.image("images/1Y-TT/tt-B.png", caption="Section A Timetable", use_container_width=True)
    with div2:
        if st.button("📸 Show Section B Timetable Image"):
            st.image("images/1Y-TT/tt-B.png", caption="Section B Timetable", use_container_width=True)

with col4:
    st.markdown(
        """
        <div style='padding: 15px; background-color: #000000; border: 1px solid #ccc; border-radius: 10px;'>
            <h4>📑 Assignment Templates</h4>
            📄 <a href='docs/assignment_template.pdf' target='_blank'>View Assignment Format</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Spacer between rows
st.markdown("<br>", unsafe_allow_html=True)

# Row 3: Academic Calendar & Reference Books
col5, col6 = st.columns(2)

with col5:
    st.markdown(
        """
        <div style='padding: 15px; background-color: #000000; border: 1px solid #ccc; border-radius: 10px; color: white;'>
            <h4>📅 Academic Calendar</h4>
            📄 <a href='https://www.du.ac.in/uploads/new-web/04072025_Academic-Calendar.pdf' target='_blank' style='color: white;'>Check Academic Calendar</a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col6:
    st.markdown(
        """
        <div style='padding: 15px; background-color: #000000; border: 1px solid #ccc; border-radius: 10px;'>
            <h4>📂 Reference Books</h4>
            📄 <a href='docs/reference_books.pdf' target='_blank'>List of Recommended Books</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.caption("Designed for first-year students to make your academic journey smoother!")






