
import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Keldon Schroeder"
field = "Theoretical Chemistry"
institution = "University of Pretoria"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# additional fields
st.header("Additional info: ")
options = st.multiselect(" What are your favourite colors", ["Green", "Red", "Blue", "Purple","Yellow"])
st.write("You chose: ", options)

st.image("C:\Users\keldo\OneDrive\Documents\chpc_coding_course\day_three\day_three\app_image.PNG", "the sigma-centre MO of Cp")


# Add a contact section
st.header("Contact Information")
email = "u21436152@tuks.co.za"
st.write(f"You can reach {name} at {email}.")
