# -*- coding: utf-8 -*-

import streamlit as st

st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

def box(text: str, color="#f9fafb", text_color="#374151"):
    st.markdown(
        f"""
        <div style="
            text-align: center;
            background-color: {color};
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);   /* soft shadow – optional */
            margin: 1.5rem auto;
            max-width: 900px;
        ">
            <div style="font-size: 1.1rem; line-height: 1.6; color: {text_color}">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
        )
#Sidebar for navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Internships", "Learnership Program", "Contact"],
)

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    background_image_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=2000"  # Example: tech/science abstract (change this!)

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{background_image_url}");
        background-size: cover;          /* or contain / 100% 100% */
        background-position: center;     /* centers the image */
        background-repeat: no-repeat;
        }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);       /* Makes top header transparent so image shows through */
        }}
    [data-testid="stToolbar"] {{
        right: 2rem;                     /* Optional: moves menu button if it overlaps */
        }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)    

    # Collect basic information
    box(f"""
        Name: Izak van der Walt\n
        Field: Space Physics\n
        Instetution: North-West University\n
        """)

    # Display basic profile information
    box(f"""
        I am currently a Honours Student that strives to do space research.\n
        So far I have done some internships at Holland & Hausberger and a Learnership Program.\n
        """)
    

elif menu == "Internships":
    st.title("Internships")
    st.sidebar.header("Upload and Filter")
    
    st.image("IMG_2875.JPEG", 
         caption="FT reactor", 
         width=1000)
    
    box(
        f"""
        I spent two vacations with Holland & Hausberger doing various projects, of which 
        the biggest one was building and pressure testing the FT reactor seen in the image above.
        
        """
        )
    # Upload publications file
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

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "Learnership Program":
    st.title("Learnership Program")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "Physics Experiments":
        st.write("### Physics Experiment Data")
        st.dataframe(physics_data)
        # Add widget to filter by Energy levels
        energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        filtered_physics = physics_data[
            physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
        ]
        st.write(f"Filtered Results for Energy Range {energy_filter}:")
        st.dataframe(filtered_physics)

    elif data_option == "Astronomy Observations":
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)
        # Add widget to filter by Brightness
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)

    elif data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)
        # Add widgets to filter by temperature and humidity
        temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "jane.doe@example.com"
    st.write(f"You can reach me at {email}.")



