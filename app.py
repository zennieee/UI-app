import streamlit as st
import pandas as pd
import datetime
import time

# --- 1. Page Config ---
st.set_page_config(page_title="Eep Tracker", page_icon="💤", layout="wide")


def tracker_page():

    # --- Title & Subheader ---
    st.title("EepTime: your personal eep tracker")
    st.subheader("Goodnight, sweet dreams.")

    # --- Sidebar ---
    with st.sidebar:
        st.header("User Settings")
        user_name = st.text_input("Username", "Rosjen")
        user_age = st.slider("Your Age", 17, 50, 20)
        app_color = st.color_picker("Personal UI color", "#fd90e7")
        st.write(f"Logged in as: {user_name}")

    # --- Tabs ---
    tab1, tab2, tab3 = st.tabs(["Sleep Log", "Insights", "Morning Check-ins"])

    # ---------------- TAB 1 ----------------
    with tab1:

        with st.form("entry_form"):
            st.write("### Log Last Night's Sleep")

            sleep_date = st.date_input("Date:", datetime.date.today())
            bedtime = st.time_input("What time did you sleep?", datetime.time(22, 0))
            waketime = st.time_input("What time did you wake up?", datetime.time(6, 30))

            quality = st.select_slider(
                "Sleep Quality Radar",
                options=["Poor", "Fair", "Good", "Great", "Splendid"]
            )

            dreams = st.text_area("Dream Journal")
            caffeine = st.checkbox("Had caffeine after 4 PM?")

            submitted = st.form_submit_button("Save to Log")

            if submitted:
                st.toast("Progress Saved!")
                st.success(f"Successfully recorded sleep for {sleep_date}")

    # ---------------- TAB 2 ----------------
    with tab2:

        m1, m2 = st.columns(2)

        m1.metric(label="Average Duration", value="7.2 hrs", delta="0.5 hrs")
        m2.metric(label="Consistency", value="85%", delta="-2%")

        st.write("#### 7-Day Sleep Tracking")

        data = pd.DataFrame(
            [6, 7.5, 5, 8, 7, 8.5],
            columns=["Hours"]
        )

        st.line_chart(data)

        with st.expander("View personalized sleep tip"):

            with st.spinner("Analyzing data..."):
                time.sleep(1)

            st.write(
                "Since you reported 'Fair' quality, try lowering your room "
                "temperature to 18°C tonight."
            )

    # ---------------- TAB 3 ----------------
    with tab3:
        st.write("Morning reflection feature coming soon!")


def about_page():

    st.title("About This Application")

    st.info("""
    - **Use case:** Digital sleep journal to track circadian health  
    - **Target User:** Students and night shift workers  
    - **Inputs:** Dates, times, sliders, checkboxes, text  
    - **Outputs:** Visualized trends, health metrics, and data summaries
    """)

    st.write("#### Why sleep matters")

    st.video("https://youtu.be/gedoSfZvBgE")


# --- Simple Navigation ---
page = st.sidebar.selectbox("Navigate", ["Dashboard", "About"])

if page == "Dashboard":
    tracker_page()
else:
    about_page()