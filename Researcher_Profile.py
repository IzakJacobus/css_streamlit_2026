# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd               # ← ADD THIS LINE
import plotly.express as px       # ← ADD THIS too (for graphs)

background_image_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=2000"  # Example: tech/science abstract (change this!)

st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

def box(text: str, text_color="#f9fafb", color="#374151"):
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
    st.title("Learnership Program – Cricket Ball Spin Dynamics")
   
    st.markdown("""
    In 2025 I participated in a project investigating the **dynamic spin behaviour** of a cricket ball.
    We analysed three main delivery types:
    - Left-arm unorthodox (e.g. chinaman / googly style)
    - Right-arm wrist spin / leg-spin
    - Right-arm finger spin / off-spin
    """)
   
    # ── Load the three datasets ──────────────────────────────────────────────
    try:
        df_unorthodox = pd.read_csv("Left_Arm_Unorthodox.csv")  # exact name from GitHub
        df_legspin    = pd.read_csv("Leg_Spin.csv")
        df_offspin    = pd.read_csv("Right_Arm_Off_spin.csv")
    
        st.success("All three spin datasets loaded successfully!")
    
    except Exception as e:  # catch broader errors for better debug
        st.error(f"Error loading CSVs: {e}")
        st.info("Current files in root directory:")
        import os
        st.write(os.listdir('.'))
        # Optional: stop early if loading fails, so tabs don't crash
        st.stop()

    # ── Show overview in tabs ────────────────────────────────────────────────
    # (Everything below must be indented under the elif, after the try/except)
    tab1, tab2, tab3, tab4 = st.tabs([
        "Overview",
        "Left-Arm Unorthodox",
        "Right-Arm Leg-Spin",
        "Right-Arm Off-Spin"
    ])
   
    with tab1:
        st.subheader("Quick Comparison")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Left-Arm Unorthodox", f"{len(df_unorthodox)} rows")
        with col2:
            st.metric("Right-Arm Leg-Spin", f"{len(df_legspin)} rows")
        with col3:
            st.metric("Right-Arm Off-Spin", f"{len(df_offspin)} rows")
       
        st.markdown("Typical columns found (may vary): Time, RPM, Revs, Speed, Spin Axis, etc.")
   
    with tab2:
        st.subheader("Left-Arm Unorthodox Spin")
        st.dataframe(df_unorthodox.head(8), use_container_width=True)
       
        if 'Time' in df_unorthodox.columns and 'RPM' in df_unorthodox.columns:
            fig = px.line(df_unorthodox, x='Time', y='RPM',
                          title="Spin Rate (RPM) over Time – Left-Arm Unorthodox",
                          markers=True)
            st.plotly_chart(fig, use_container_width=True)
       
        if 'Speed' in df_unorthodox.columns and 'RPM' in df_unorthodox.columns:
            fig_scatter = px.scatter(df_unorthodox, x='Speed', y='RPM',
                                     title="Spin vs Speed – Left-Arm Unorthodox")
            st.plotly_chart(fig_scatter, use_container_width=True)
   
    with tab3:
        st.subheader("Right-Arm Leg-Spin")
        st.dataframe(df_legspin.head(8), use_container_width=True)
       
        if 'Time' in df_legspin.columns and 'RPM' in df_legspin.columns:
            fig = px.line(df_legspin, x='Time', y='RPM',
                          title="Spin Rate (RPM) over Time – Leg-Spin",
                          markers=True)
            st.plotly_chart(fig, use_container_width=True)
   
    with tab4:
        st.subheader("Right-Arm Off-Spin")
        st.dataframe(df_offspin.head(8), use_container_width=True)
       
        if 'Time' in df_offspin.columns and 'RPM' in df_offspin.columns:
            fig = px.line(df_offspin, x='Time', y='RPM',
                          title="Spin Rate (RPM) over Time – Off-Spin",
                          markers=True)
            st.plotly_chart(fig, use_container_width=True)

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
