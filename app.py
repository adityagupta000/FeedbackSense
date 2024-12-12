import streamlit as st
import pandas as pd
from feedback_analyzer import FeedbackAnalyzer  # Adjust the import if necessary
import pickle
import os

# Load the trained model from a file
def load_model(filepath='feedback_model.pkl'):
    """Load the trained model from a file"""
    if os.path.exists(filepath):
        try:
            with open(filepath, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return None
    return None

# Main Streamlit app function
def main():
    st.title("Teacher Feedback Analysis System")

    # Initialize session state for the analyzer (model feedback analysis)
    if 'analyzer' not in st.session_state:
        st.session_state.analyzer = load_model()

    if not st.session_state.analyzer:
        st.error("Model not loaded. Please ensure the model file is available.")
        return

    # Individual feedback analysis section
    st.header("Analyze Individual Feedback")
    feedback_text = st.text_area("Enter feedback to analyze (max 50 words):", max_chars=250)

    if st.button("Analyze Feedback") and feedback_text:
        if len(feedback_text.split()) > 50:
            st.warning("Please keep feedback under 50 words.")
        else:
            try:
                result = st.session_state.analyzer.analyze_feedback(feedback_text)

                # Display results
                st.subheader("Analysis Results")
                sentiment_color = "green" if result['sentiment'] == 'positive' else "orange"
                st.markdown(f"**Sentiment:** :{sentiment_color}[{result['sentiment']}]")
                st.markdown(f"**Confidence:** {result['confidence']:.2%}")

            except Exception as e:
                st.error(f"Error analyzing feedback: {str(e)}")

if __name__ == "__main__":
    main()
