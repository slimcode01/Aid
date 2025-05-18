import streamlit as st
import pandas as pd

def main_page():

    with st.sidebar:
        st.page_link("pages/3_⏮_logout.py", label="Logout", icon="🔒")

        st.write("")

    # Title of the application
    st.title("PATIENT :red[DECISION] DASHBOARD")


    # Introduction
    st.header("Welcome to the Prostate Cancer Decision Aid")
    st.write("This tool is designed to help you understand your options regarding prostate cancer treatment.")

    # Load image
    image = "prostate_diagram.jpg"

    # Display image
    st.image(image, caption="Prostate Cancer", width=500,use_container_width=True)

    # Information Section
    st.header("Understanding Prostate Cancer")
    st.write("""
    A cancer in a man's prostate, a small walnut-sized gland that produces seminal fluid.
    A man's prostate produces the seminal fluid that nourishes and transports sperm.
    Prostate cancer is a common cancer among men. It can be slow-growing or aggressive. 
    Understanding your diagnosis and treatment options is crucial for making informed decisions.
    """)

    # Risk Factors
    st.header(":red[Risk Factors]")
    st.write("""
    Some risk factors for prostate cancer include age, family history, and race. 
    Discussing these factors with your healthcare provider can help assess your risk.
    """)

    # Treatment Options
    st.header(":green[Treatment Options]")
    treatment_options = ["Active Surveillance", "Surgery", "Radiation Therapy", "Hormone Therapy", "Chemotherapy"]
    selected_treatment = st.selectbox("Select a treatment option to learn more:",treatment_options,key=1)

    if selected_treatment == "Active Surveillance":
        st.write("Active surveillance involves closely monitoring the cancer without immediate treatment.")
    elif selected_treatment == "Surgery":
        st.write("Surgery involves removing the prostate gland and some surrounding tissue.")
    elif selected_treatment == "Radiation Therapy":
        st.write("""Radiation therapy uses high-energy rays to target and kill cancer cells.
                Radiation is the strategic use of ionizing radiation or photons to kill cancer cells.
                It works by damaging the cancer cells’ DNA (the genetic blueprint of the cancer cell).
                The targeted cells die without growing or replicating themselves.
                Radiation therapy, like surgery, is very effective at killing localized or locally advanced prostate cancer.
                """)
    elif selected_treatment == "Hormone Therapy":
        st.write("""Hormone therapy reduces the levels of male hormones to slow the growth of cancer.
                Testosterone is the primary male hormone, and plays an important role in establishing and maintaining typical male characteristics, 
                such as body hair growth, muscle mass, sexual desire, and erectile function, and contributes to a host of other normal physiologic processes in the body.
                """)
    elif selected_treatment == "Chemotherapy":
        st.write("Chemotherapy uses drugs to kill rapidly growing cancer cells.")


    tab1, tab2, tab3 = st.tabs(["Personal Information", "Thresholds", "Uncertainty values"])

    with tab1:
        
        st.header("Personal Information")
        risk= st.selectbox(
        'What is your risk group categorization:',
        options=[
        "Intermediate Risk",
        "Low risk",
        "High risk"])

        erection= st.selectbox(
        'In the past 4 weeks, what percentage of the time that you wanted to have an erection, were you able to achive one:',
        options=[
        "Always",
        "Sometimes",
        "Not at all"],key=2)

        urine= st.selectbox(
        'In the past 4 weeks, how often have you had uncontrolled leakage of urine:',
        options=[
        "Rarely",
        "Sometimes",
        "Never"],key=3)

        stool= st.selectbox(
        'In the past 4 weeks, how often have you had uncontrolled leakage of stool or feces:',
        options=[
        "Rarely",
        "Sometimes",
        "Never"],key=4)
        
        if st.button("Submit", key=15):

            data = {'risk': [risk], 'erection': [erection], 'urine_leakage': [urine],'stool_leakage': [stool]}
            df = pd.DataFrame(data)
            st.write("Selected Data:")
            st.table(df)


    with tab2:
        st.header("Thresholds")
        t1= st.selectbox(
        'One or more years after treatment, i would tolerate NOT being able to have an erection, at most what percentage of time that l wanted to have one:',
        options=[
        "Never","Sometimes"],key=5)

        t2= st.selectbox(
        'One or more years after treatment, i would tolerate at most uncontrolled urinary leakage:',
        options=[
        "Once a week",
        "Once a month",
        "Once a year"],key=6)

        t3= st.selectbox(
        'One or more years after treatment, i would tolerate at most uncontrolled bowel leaking:',
        options=[
        "Once a week",
        "Once a month",
        "Once a year"],key=7)

        t4 = st.slider(
        'One or more years after treatment, l would tolerate at most, waking up ----- times to go to bathroom after l went to bed',
        0,5,1,1)

        if st.button("Submit",key=12):

            data = {'erection': [t1], 'urinary_leakage': [t2], 'bowel_leakage': [t3], 'Waking_up': [t4]}
            df = pd.DataFrame(data)
            st.write("Selected Data:")
            st.table(df)


    with tab3:
        st.header("Uncertainty values")
        slider_value = st.slider(
        'Progression of the disease less than 5 years from today:',
        0,100,1,5,key=14)

        slider_value1 = st.slider(
        'Waking up to go to the bathroom more than 2 times after you went to sleep:',
        0,100,1,5,key=16)

        if st.button("Submit",key=13):

            data = {'progression (%)': [slider_value], 'frequency (%)': [slider_value1]}
            df = pd.DataFrame(data)
            st.write("Selected Data:")
            st.table(df)

    # Sample data for risk groups and corresponding side effects and treatments
    data = {
        'Risk Group': ['Low', 'Intermediate', 'High'],
        'Side Effects': [
            'Minimal side effects, regular monitoring recommended.',
            'Possible side effects include fatigue, urinary issues, and sexual dysfunction.',
            'Severe side effects, aggressive treatment required, including chemotherapy.'
        ],
        'Treatment Recommendations': [
            'Active surveillance or watchful waiting.',
            'Radiation therapy or hormone therapy.',
            'Combination of surgery, radiation, and chemotherapy.'
        ]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Risk group analysis
    st.write('### :blue[Prostate Cancer Risk Group Analysis]')
    risk_group = st.selectbox('Select Risk Group:', df['Risk Group'],key=8)

    # Display corresponding side effects and treatment recommendations
    selected_row = df[df['Risk Group'] == risk_group]
    st.write('### :red[Side Effects:]')
    st.write(selected_row['Side Effects'].values[0])
    st.write('### :green[Treatment Recommendations:]')
    st.write(selected_row['Treatment Recommendations'].values[0])

    if risk_group=="High":
        import matplotlib.pyplot as plt

        categories = ['SURGERY', 'RADIATION', 'CHEMOTHERAPY']
        values = [100, 98, 95]
        colors = ['#FF5733', '#33FF57', '#3357FF']

        # Create bar graph
        plt.bar(categories, values, color=colors,width=0.4)
        plt.xlabel('Treatments')
        plt.ylabel('Majority (%)')
        plt.title('High Risk-group Recommendation')

        # Display the graph in Streamlit
        st.pyplot(plt)

    elif risk_group=="Low":
        import matplotlib.pyplot as plt

        categories = ["""ACTICVE 
        SURVEILLANCE""",'']
        values = [100,0]
        colors = ['#3357FF','#fefefefe']

        # Create bar graph2
        plt.bar(categories, values, color=colors,width=0.2,align="center")
        plt.xlabel('Treatments')
        plt.ylabel('Majority (%)')
        plt.title('Low Risk-Group Recommendation')

        st.pyplot(plt)

    else:
        import matplotlib.pyplot as plt

        categories = ['RADIATION', 'HORMONE THERAPY']
        values = [100, 90]
        colors = ['#33FF57', '#3357FF']

        plt.bar(categories, values, color=colors,width=0.2)
        plt.xlabel('Treatments')
        plt.ylabel('Majority (%)')
        plt.title('Intermediate Risk-Group Recommendation')

        st.pyplot(plt)

    data1 = {"Treatment":['Chemotherapy','Radiation Therapy','Hormone Therapy','Surgery'],
            "Side Effects":['hair loss,loss of appetite,mouth sores',
                            'erectile dysfunction,loose stools,urinary issues',
                            'decreased sexual desire,erectile dysfunction, fatigue',
                            'urinary issues,sexual dysfuction,fertility issues']}

    data1 = pd.DataFrame(data1)

    df_styled = data1.style.set_properties(**{"background-color":"lightblue","color":"red","border":"solid"})
    st.title("Treatment and Side Effects")
    st.table(df_styled)

    # Decision Making
    st.header(":green[Making Your Decision]")
    st.write("""
    Consider discussing your options with your healthcare team. 
    They can provide personalized advice based on your health and preferences.
    """)

    # Conclusion
    st.header(":blue[Conclusion]")
    st.write("Thank you for using the Prostate Cancer Patient Decision Aid. We hope this tool helps you make informed decisions.")


main_page()