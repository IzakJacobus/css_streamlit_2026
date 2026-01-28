# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go   # ← Added for more control over lines & layout

background_image_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=2000"

st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

def box(text: str, text_color="#f9fafb", color="#374151"):
    st.markdown(
        f"""
        <div style="
            text-align: center;
            background-color: {color};
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 1.5rem auto;
            max-width: 900px;
        ">
            <div style="font-size: 1.1rem; line-height: 1.6; color: {text_color}">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Sidebar for navigation
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
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    box(f"""
        Name: Izak van der Walt\n
        Field: Space Physics\n
        Institution: North-West University\n
    """)
    
    box(f"""
        I am currently a Honours Student that strives to do space research.\n
        So far I have done some internships at Holland & Hausberger and a Learnership Program.\n
    """)

elif menu == "Internships":
    st.title("Internships")
    st.sidebar.header("Upload and Filter")
    
    st.image("IMG_2875.JPEG", caption="FT reactor", width=1000)
    
    box(f"""
        I spent two vacations with Holland & Hausberger doing various projects, of which
        the biggest one was building and pressure testing the FT reactor seen in the image above.
    """)
    
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
        right: 2rem;
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
    
    try:
        df_unorthodox = pd.read_csv("Left_Arm_Unorthodox.csv")
        df_legspin    = pd.read_csv("Leg_Spin.csv")
        df_offspin    = pd.read_csv("Right_Arm_Off_Spin.csv")
        
        st.success("All three spin datasets loaded successfully!")
        
        # ── Function to create top-view deviation plot ────────────────────────
        def create_top_view_plot(df, title_suffix):
            fig = go.Figure()
            
            # Seam groups: (deviation columns, distance columns, colors, labels)
            seam_groups = [
                # Seam 0°
                (['x121', 'x221', 'x321'], ['x111', 'x211', 'x311'], 'Seam 0°'),
                # Seam 30°
                (['x122', 'x222', 'x322'], ['x112', 'x212', 'x312'], 'Seam 30°'),
                # Seam 60°
                (['x123', 'x223', 'x323'], ['x113', 'x213', 'x313'], 'Seam 60°'),
                # Seam 90°
                (['x124', 'x224', 'x324'], ['x114', 'x214', 'x314'], 'Seam 90°'),
            ]
            
            colors = ['blue', 'green', 'orange']
            
            for (dev_cols, dist_cols, seam_label) in seam_groups:
                for i, (dev_col, dist_col) in enumerate(zip(dev_cols, dist_cols)):
                    if dev_col in df.columns and dist_col in df.columns:
                        run_label = f'Run {i+1} {seam_label}'
                        fig.add_trace(go.Scatter(
                            x=df[dev_col],          # Deviation on x-axis
                            y=df[dist_col],         # Distance on y-axis
                            mode='lines+markers',
                            line=dict(color=colors[i]),
                            name=run_label,
                            marker=dict(size=6)
                        ))
            
            # Add zero lines (cricket pole reference)
            fig.add_hline(y=0, line_width=2, line_color="black")
            fig.add_vline(x=0, line_width=2, line_color="black")
            
            # Layout matching your original matplotlib top-view style
            fig.update_layout(
                title=f'Ball Deviation w.r.t. Cricket Pole (Top View) – {title_suffix}',
                xaxis_title='Deviation from the cricket pole (m)',
                yaxis_title='Distance traveled (m)',
                xaxis=dict(
                    range=[-0.5, 0.5],          # Zoomed to show small deviations clearly
                    dtick=0.1,
                    showgrid=True,
                    gridcolor='lightgray'
                ),
                yaxis=dict(
                    range=[-21, 1],
                    dtick=5,
                    autorange="reversed",       # Inverts y-axis (bowl → batsman direction)
                    showgrid=True,
                    gridcolor='lightgray'
                ),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                height=600,
                margin=dict(l=60, r=40, t=80, b=60)
            )
            
            return fig
        
        # ── Display the top-view plots ────────────────────────────────────────
        st.subheader("Ball Deviation Plots (Top View – Individual Runs per Seam Angle)")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Left-Arm Unorthodox**")
            fig_unorthodox = create_top_view_plot(df_unorthodox, "Left-Arm Unorthodox")
            st.plotly_chart(fig_unorthodox, use_container_width=True)
        
        with col2:
            st.markdown("**Leg-Spin**")
            fig_legspin = create_top_view_plot(df_legspin, "Leg-Spin")
            st.plotly_chart(fig_legspin, use_container_width=True)
        
        with col3:
            st.markdown("**Off-Spin**")
            fig_offspin = create_top_view_plot(df_offspin, "Off-Spin")
            st.plotly_chart(fig_offspin, use_container_width=True)
        
        # Debug: show actual columns so you can confirm names
        with st.expander("Debug: Column names (click to expand)"):
            st.write("Left-Arm Unorthodox:", df_unorthodox.columns.tolist())
            st.write("Leg-Spin:", df_legspin.columns.tolist())
            st.write("Off-Spin:", df_offspin.columns.tolist())
    
    except Exception as e:
        st.error(f"Error loading or processing CSVs: {e}")
        st.info("Current files in root directory:")
        import os
        st.write(os.listdir('.'))
        st.stop()
    
    # ── Your existing tabs (Overview + RPM plots) ────────────────────────────
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
    st.header("Contact Information")
    email = "izakjacobus@gmail.com"
    st.write(f"You can reach me at {email}.")
    
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
