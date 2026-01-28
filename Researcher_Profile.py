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
        
        # ── Helper to create top-view deviation plot (deviation vs distance) ──
        def create_top_view_plot(df, title_suffix):
            fig = go.Figure()
            
            # Individual runs (like your original)
            runs = [
                ('x111', 'y111', 'blue',   'Run 1 seam 0°'),
                ('x211', 'y211', 'green',  'Run 2 seam 0°'),
                ('x311', 'y311', 'orange', 'Run 3 seam 0°'),
                ('x112', 'y112', 'blue',   'Run 1 seam 30°'),
                ('x212', 'y212', 'green',  'Run 2 seam 30°'),
                ('x312', 'y312', 'orange', 'Run 3 seam 30°'),
                ('x113', 'y113', 'blue',   'Run 1 seam 60°'),
                ('x213', 'y213', 'green',  'Run 2 seam 60°'),
                ('x313', 'y313', 'orange', 'Run 3 seam 60°'),
                ('x114', 'y114', 'blue',   'Run 1 seam 90°'),
                ('x214', 'y214', 'green',  'Run 2 seam 90°'),
                ('x314', 'y314', 'orange', 'Run 3 seam 90°'),
            ]
            
            for x_col, y_col, color, label in runs:
                if x_col in df.columns and y_col in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df[x_col], y=df[y_col],
                        mode='lines+markers',
                        line=dict(color=color),
                        name=label,
                        marker=dict(size=6)
                    ))
            
            fig.add_hline(y=0, line_width=2, line_color="black")
            fig.add_vline(x=0, line_width=2, line_color="black")
            
            fig.update_layout(
                title=f'Ball Deviation w.r.t. Cricket Pole (Top View) – {title_suffix}',
                xaxis_title='Deviation from the cricket pole (m)',
                yaxis_title='Distance traveled (m)',
                xaxis_range=[-1, 1],
                yaxis_range=[-21, 1],
                yaxis_autorange="reversed",
                showlegend=True,
                xaxis_showgrid=True,
                yaxis_showgrid=True,
                height=500
            )
            return fig
        
        # ── Helper for average per seam angle (like your avg plot) ──
        def create_average_seam_plot(df, title_suffix):
            fig = go.Figure()
            
            # Averages per seam angle
            seams = [
                (['x121','x221','x321'], ['y121','y221','y321'], 'Seam 0°', 'blue'),
                (['x122','x222','x322'], ['y122','y222','y322'], 'Seam 30°', 'green'),
                (['x123','x223','x323'], ['y123','y223','y323'], 'Seam 60°', 'orange'),
                (['x124','x224','x324'], ['y124','y224','y324'], 'Seam 90°', 'purple'),
            ]
            
            for x_cols, y_cols, label, color in seams:
                if all(c in df.columns for c in x_cols + y_cols):
                    avg_x = df[x_cols].mean(axis=1)
                    avg_y = df[y_cols].mean(axis=1)
                    fig.add_trace(go.Scatter(
                        x=avg_x, y=avg_y,
                        mode='lines+markers',
                        name=label,
                        line=dict(color=color)
                    ))
            
            fig.add_hline(y=0, line_width=2, line_color="black")
            fig.add_vline(x=0, line_width=2, line_color="black")
            
            fig.update_layout(
                title=f'Average Deviation per Seam Angle – {title_suffix}',
                xaxis_title='Deviation from the cricket pole (m)',
                yaxis_title='Distance traveled (m)',
                xaxis_range=[-1, 1],
                yaxis_range=[-21, 1],
                yaxis_autorange="reversed",
                showlegend=True,
                xaxis_showgrid=True,
                yaxis_showgrid=True,
                height=500
            )
            return fig
        
        # ── Display plots ─────────────────────────────────────────────────────
        st.subheader("Deviation & Trajectory Plots")
        
        # Average seam angle plots (one per dataset)
        st.markdown("**Average Deviation per Seam Angle**")
        cols_avg = st.columns(3)
        with cols_avg[0]:
            st.plotly_chart(create_average_seam_plot(df_unorthodox, "Left-Arm Unorthodox"), use_container_width=True)
        with cols_avg[1]:
            st.plotly_chart(create_average_seam_plot(df_legspin, "Leg-Spin"), use_container_width=True)
        with cols_avg[2]:
            st.plotly_chart(create_average_seam_plot(df_offspin, "Off-Spin"), use_container_width=True)
        
        # Top view individual runs (one per dataset)
        st.markdown("**Individual Runs – Top View (Deviation vs Distance)**")
        cols_top = st.columns(3)
        with cols_top[0]:
            st.plotly_chart(create_top_view_plot(df_unorthodox, "Left-Arm Unorthodox"), use_container_width=True)
        with cols_top[1]:
            st.plotly_chart(create_top_view_plot(df_legspin, "Leg-Spin"), use_container_width=True)
        with cols_top[2]:
            st.plotly_chart(create_top_view_plot(df_offspin, "Off-Spin"), use_container_width=True)
        
        # Debug columns
        with st.expander("Debug: Column names"):
            st.write("Unorthodox:", df_unorthodox.columns.tolist())
            st.write("Leg-Spin:", df_legspin.columns.tolist())
            st.write("Off-Spin:", df_offspin.columns.tolist())
    
    except Exception as e:
        st.error(f"Error: {e}")
        import os
        st.write("Files in root:", os.listdir('.'))
        st.stop()
    
    # Your existing tabs (RPM etc.) can stay below
    # ...

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
