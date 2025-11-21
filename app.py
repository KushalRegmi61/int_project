import streamlit as st
import requests
import json


# CONFIG

API_URL = "http://127.0.0.1:8000/predict"   # Change if deployed elsewhere

st.set_page_config(
    page_title="Sambodhan – Department Classifier",
    layout="centered"
)


# UI

st.title("📨 Sambodhan – Department Classifier")
st.write("Enter a grievance and the AI model will classify it to the appropriate municipal department.")

# Text input
input_text = st.text_area(
    "Citizen Grievance:",
    height=200,
    placeholder="Example:\nStreet lights have been broken in our area for 2 weeks..."
)

# Classify button
if st.button(" Classify"):
    if not input_text.strip():
        st.error("Please enter a grievance first.")
    else:
        try:
            # Make API request
            payload = {"text": input_text}
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                result = response.json()[0]
                

                st.subheader(" Prediction")

                # for res in results:
                #     with st.container():
                #         st.markdown(f"""
                #         **Department:** `{res.get('label', 'N/A')}`  
                #         **Confidence:** `{round(res.get('score', 0.0) * 100, 2)}%`
                #         """)\
                    

                with st.container():
                    st.markdown(f"""
                    **Urgency:** `{result.get('label', 'N/A')}`  
                    **Confidence:** `{round(result.get('score', 0.0) * 100, 2)}%`
                    """)

            else:
                st.error(f"Server Error: {response.status_code}")
                st.write(response.text)

        except Exception as e:
            st.error("Could not reach backend!")
            st.exception(e)


st.markdown("---")
st.caption("Built with ❤️ using Streamlit and FastAPI")
