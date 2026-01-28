# -*- coding: utf-8 -*-

import streamlit as st

background_image_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=2000"  # Example: tech/science abstract (change this!)

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

elif menu == "Learnership Program":
    st.title("Learnership Program")
    st.sidebar.header("Data Selection")
    
    box(
        f"""
        In 2025 I was part of a project where we looked at the dinamic spin of a cricket ball. We 
        looked at three different types of spins: , and 
        """
        )

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

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "izakjacobus@gmail.com"
    st.write(f"You can reach me at {email}.")

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



