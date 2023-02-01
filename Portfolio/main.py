import streamlit as st
from streamlit_timeline import timeline
import json
import requests
from PIL import Image
import streamlit.components.v1 as components


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sanyam Jain"
PAGE_ICON = ":wave:"
NAME = "Sanyam Jain :wave:"
DESCRIPTION = """
Student. Dual Degree Aspirant. Full Stack Data Scientist.
"""
EMAIL = "sanyam0605@gmail.com"

LinkedIn = "https://www.linkedin.com/in/sanyam-jain-a5a15a220/"
GitHub = "https://github.com/Sj0605-DataSci"



PROJECTS = {
    "🏆 Food Delivery Time Prediction - a simple web application that predicts the delivery time for food delivery based on various factors ": "https://foodeliveryprediction.streamlit.app/",
    "🏆 Movie Recommendation Engine  - ( Content Based )": "https://sj0605-datasci-movie-recommendation-enginer-app-pz6074.streamlit.app/",
    "🏆 GeoSpatial Analysis using Python - use geospatial analysis to make decisions about opening up new restaurants(or retail stores, bank branches, airports, etc)": "https://github.com/Sj0605-DataSci/GeoSpatial-Analysis",
    "🏆 Voice bot with GUI - simple to use voice assistant which greets you according to your local time and I have tried my best to automate everything via it by using selenium": "https://github.com/Sj0605-DataSci/Jarvis-Voice-Assistant",
    "🏆 Auto EDA and ML App - simple app in which one can upload data and app will do EDA and will provide best model based on the task":"https://sj065-automation.streamlit.app/"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
















def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Portfolio/style/style.css")

profile_pic = Image.open("Portfolio/Images/profilephoto.jpeg")


# Create a function for the home page
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_tfb3estd.json")


pdfFileObj = open('Portfolio/pdfs/SanyamCV.pdf', 'rb')

def home():
    col1, col2 = st.columns(2)
    with col1:
        st.image(profile_pic, width=150)


    with col2:
        st.header(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=pdfFileObj,
            file_name='SanyamCV.pdf',
            mime='pdf',
        )
        st.write("📫", EMAIL)
        st.write("🔗 LinkedIn: [linkedin Profile](https://www.linkedin.com/in/sanyam-jain-a5a15a220/)")
        st.write("🧑‍💻 Github: [Github](https://github.com/Sj0605-DataSci)")
            # st_lottie(lottie_coding)

st.write('\n')







def about_me():
    st.title("About Me")

    # --- Education ---
    st.write('\n')
    st.subheader("Education")
    st.write(
        """
    - 🎓 IIT Madras : BS in Data Science and its Applications                   (2021 - 2025)
    - 🎓 Manipal University : BTech in Computer Science and Engineering         (2020 - 2024)
    """
    )





    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write(
        """
    - ✔️ 2 Years expereince extracting actionable insights from data
    - ✔️ Strong hands on experience and knowledge in Python and Machine Learning
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )

    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python (Coding, Development), SQL
    - 👩‍💻 Libraries & Frameworks & API: Pandas,Scikit-learn,Keras,Tensorflow,Rest,Fast,Streamlit
    - 📊 Data Visulization: Tableau, MS Excel, Plotly, Matplotlib, Seaborn,Geopandas
    - 📚 Modeling: Logistic regression, linear regression, decision trees
    - 📚 Learning: Supervised, Unsupervised,Ensemble
    - 🗄️ Databases: MySQL
    """
    )

    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Research Intern | Delhi Technological University, Delhi**")
    st.write("01/2023 - Present")
    st.write(
        """
    - ► Used quantitative research methods to define, iterate upon and advance key areas of research agenda.
    - ►Gathered data to meet specific project objectives using various informational sources.
    - ►Monitored and observed experiments, recording production and test data for evaluation by research personnel.
    - ►Build a NLP model for hate speech detection
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Scientist Intern | Neet Navigator**")
    st.write("11/2022 - 01/2023")
    st.write(
        """
    - ► Identified relationships and trends and any factors that affected results of research.
    - ► Cleaned and manipulated raw data using statistical software.
    - ► Tested, validated and reformulated models to deliver accurate prediction of outcomes of interest.
    - ► Created graphs, charts and other visualizations to convey results of data analysis using specialized software.
    - ► Recommended data-driven solutions to key stakeholders.
    """
    )

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Undergrad Research Intern | Manipal University Jaipur**")
    st.write("04/2022 - Present")
    st.write(
        """
    - ► Provided informed suggestions by analyzing research methods and identifying optimization opportunities.
    - ► Drafted reports to summarize research efforts for particular studies.
    - ► Gathered data for supporting ongoing professional studies.
    - ► Published a patent ( title : SYSTEM AND METHOD FOR GENERATING AUDIO INFORMATION TO GUIDE A VISUALLY IMPAIRED USER)
    """
    )
    # --- JOB 4
    st.write('\n')
    st.write("🚧", "**Data Scientist Intern | Indian Institute of Technology Delhi**")
    st.write("06/2022 - 07/2022")
    st.write(
        """
    - ► Designed surveys, opinion polls, or other instruments to collect data.
    - ► Created graphs, charts and other visualizations to convey results of data analysis using specialized software.
    - ► Applied feature selection algorithms to models predicting outcomes of interest, such as sales, attrition and healthcare use.
    - ► Analyzed, manipulated and process large sets of data using statistical software.
    """
    )


# Create a function for the projects page

def timeline1():
    st.write("Here's a summary of my education and work experience:")
    with open("Portfolio/timeline.json", "r") as f:
        timeline_data = json.load(f)

    timeline(timeline_data, height=500)


def projects():
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

# Create a function for the contact page

# Create a function to create the navigation menu
def create_navbar():
    menu = ["Home", "About Me", "Projects", "Timeline"]
    choice = st.sidebar.selectbox("Select a page", menu)

    # Show the appropriate page based on user's choice
    if choice == "Home":
        home()
    elif choice == "About Me":
        about_me()
    elif choice == "Projects":
        projects()
    elif choice == "Timeline":
        timeline1()


# Create the Streamlit app
def main():
    create_navbar()

if __name__ == "__main__":
    main()
