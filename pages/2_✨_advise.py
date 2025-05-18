
import streamlit as st

st.set_page_config(
page_title="Prostate cancer Aid",
page_icon="🧊",
layout="centered",
)

st.sidebar.success("Select a page")

st.title("Advises for prostate cancer")

st.header("Maintain a Healthy Weight")
st.write(""" Obesity can be a risk factor for developing more aggressive prostate cancer.
         In general, losing weight and maintaining a healthy weight as you age can help reduce your risk of cancer and many other health problems.
         """)

st.header("Get Regular Exercise")
st.write("""In addition to helping you achieve a healthy weight, exercise can reduce inflammation,
         improve immune function and fight some of the negative health effects of a sedentary lifestyle—all of which can help prevent cancer.
         """)

st.header("Stop Smoking and Drink Less")
st.write("""Quitting smoking can improve your health in many ways, including lowering your cancer risk. 
         And if you drink, do so in moderation. 
         Some studies suggest that red wine has antioxidant properties that may benefit your health.
         """)

st.header("Increase Your Vitamin D")
st.write("""Most people don’t get enough vitamin D. It can help protect against prostate cancer and many other conditions. 
         Vitamin D-rich foods include cod liver oil, wild salmon and dried shitake mushrooms. 
         Since the sun is a better, more readily available source of vitamin D, many experts recommend getting 10 minutes of sun exposure (without sunscreen) every day. 
         Doctors often recommend vitamin D supplements. However, you should talk to your doctor before taking any vitamin or supplement.
         """)
