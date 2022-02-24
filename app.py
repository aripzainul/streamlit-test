import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
   page_title="Azazin", #ini header dalam websitenya
   #link pavicon : https://www.webfx.com/tools/emoji-cheat-sheet/
   page_icon=":octocat:", #ini untuk pavicon
   layout="wide"
)


st.markdown("""

This is my first streamlit app.

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

---

Normal Text

*Italic*

**Bold**

***Italic & Bold***

"""
)


st.header('CSV Data')

df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data.csv')
df


# ----- st.map -----
st.header('Map')

df2 = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.map(df2)


# ----- st.text_input -----
st.header('Text Input')

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


# ----- st.file_uploader -----
st.sidebar.header('File Uploader')

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
   # Can be used wherever a "file-like" object is accepted:
   dataframe = pd.read_csv(uploaded_file)
   st.header('Data Upload')
   st.write(dataframe)

"""---"""
# ----- st.columns -----
st.header('Columns')

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)

"""---"""

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")


"""---"""
# ----- st.video -----
st.header('Video')

st.video('https://www.youtube.com/watch?v=cuoPma70qac&list=PLNlU9Z3WL94PYseGgjPYT1GxbkAznhQAs&index=38&t=127s', start_time=300)


"""---"""
# ----- st.metric -----
st.header('Metric')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")







# ----- HIDE STREAMLIT STYLE -----
hide_st_style = """
   <style>
   #MainMenu {visibility: hidden;}
   footer {visibility: hidden;}
   header {visibility: hidden;}
   </style>
   """
st.markdown(hide_st_style, unsafe_allow_html=True)