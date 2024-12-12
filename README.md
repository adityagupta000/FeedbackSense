# Teacher Feedback Analysis System

## Overview
The **Teacher Feedback Analysis System** is a Streamlit application designed to analyze and evaluate textual feedback provided to teachers. This system helps identify sentiments and highlights areas for improvement or excellence based on the feedback.

## Features
- **Analyze Individual Feedback**: Enter text-based feedback and get sentiment analysis with confidence scores.
- **Pre-trained Model**: The system uses a pre-trained machine learning model for efficient feedback classification.
- **Sentiment Detection**: Identifies positive feedback and areas that need improvement.
- **Confidence Score**: Provides a confidence percentage for the sentiment classification.

## Usage
### Analyze Individual Feedback
1. Enter feedback text (up to 50 words).
2. Click the "Analyze Feedback" button.
3. View the sentiment (Positive or Needs Improvement) and its confidence score.

## How to Run Locally
### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Project Structure
```
.
├── app.py                  # Main Streamlit application
├── feedback_analyzer.py    # Feedback analysis logic and model
├── requirements.txt        # Required Python packages
├── feedback_model.pkl      # Pre-trained machine learning model
└── README.md               # Project documentation
```
