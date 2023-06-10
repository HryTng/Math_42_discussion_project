import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import io

web_apps = st.sidebar.selectbox("Select Web-applications", "EDA")

if web_apps == "EDA":

  uploaded_file = st.sidebar.file_uploader("Choose a file")

  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    show_df = st.checkbox("Show Data Frame", key="disabled")

    if show_df:
      st.write(df)

    column_type = st.sidebar.selectbox('Select data type',
                                       ("Numerical", "Categorical"))

    if column_type == "Numerical":
      numerical_column = st.sidebar.selectbox(
          'Select a column', df.select_dtypes(include=['int64', 'float64']).columns)
      choose_opacity = st.slider(
          'Color opacity', min_value=0.0, max_value=1.0, step=0.05)

      hist_bins = st.slider('Number of bins', min_value=5,
                            max_value=150, value=30)
      hist_title = st.text_input('Set Title', 'Histogram')
      hist_xtitle = st.text_input('Set x-axis Title', numerical_column)

      fig, ax = plt.subplots()
      ax.hist(df[numerical_column], bins=hist_bins,
              edgecolor="red", alpha=choose_opacity)
      ax.set_title(hist_title)
      ax.set_xlabel(hist_xtitle)
      ax.set_ylabel('Count')

      st.pyplot(fig)
      filename = "plot.png"
      fig.savefig(filename,dpi = 300)

      with open("plot.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )
