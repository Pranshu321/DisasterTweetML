import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

tfidf = pickle.load(open('tfidf_vectorizer.pk1', 'rb'))

model = pickle.load(open('model.pk1', 'rb'))

def predict_the_output(text):
    text = [text]
    text = tfidf.transform(text)
    return model.predict(text)

def main():
    html_temp = """
    <div style="background-color:green;padding:10px;margin-bottom:20px;">
    <h2 style="color:white;text-align:center;">Disaster Tweet Detection</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.text("Paste the text for prediction")

    text = st.text_area("Text", "Type Here")
    if text:
        result = ""
        if st.button("Predict"):
            result = predict_the_output(text)
            if result[0] == 1:
                st.success('This is a Disaster Tweet')
            else:
                st.error('This is a Non Disaster Tweet')


if __name__ == '__main__':
    main()
