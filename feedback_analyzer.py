import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import pickle

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

class FeedbackAnalyzer:
    def __init__(self):
        # Initialize the vectorizer and classifier
        self.vectorizer = TfidfVectorizer(max_features=1000)  # Limit to 1000 features
        self.classifier = MultinomialNB()  # Naive Bayes classifier for text classification
        self.stop_words = set(stopwords.words('english'))  # Set of stop words to filter out

    def preprocess_text(self, text):
        """
        Preprocess the feedback text: lowercasing, removing special characters,
        tokenizing, and removing stop words.
        """
        # Convert to lowercase
        text = text.lower()
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stop words
        tokens = [t for t in tokens if t not in self.stop_words]
        # Join tokens back into a single string
        return ' '.join(tokens)

    def prepare_data(self, df):
        """
        Preprocess the feedback data, clean it, and create labels.
        """
        # Ensure feedback is a string
        df['Feedback_Text'] = df['Feedback_Text'].astype(str)
        # Preprocess each feedback
        df['processed_feedback'] = df['Feedback_Text'].apply(self.preprocess_text)
        # Create binary labels: 1 for rating >= 4, 0 for rating < 4
        df['label'] = (df['Rating'] >= 4).astype(int)
        return df

    def train(self, df):
        """
        Train the Naive Bayes classifier on the given DataFrame.
        """
        # Prepare data
        prepared_df = self.prepare_data(df)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            prepared_df['processed_feedback'],
            prepared_df['label'],
            test_size=0.2,
            random_state=42
        )

        # Convert text data to TF-IDF features
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        X_test_tfidf = self.vectorizer.transform(X_test)

        # Train the classifier
        self.classifier.fit(X_train_tfidf, y_train)

        # Make predictions on the test set
        y_pred = self.classifier.predict(X_test_tfidf)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy

    def analyze_feedback(self, feedback_text):
        """
        Analyze a single piece of feedback and predict its sentiment.
        """
        # Preprocess the feedback text
        processed_feedback = self.preprocess_text(feedback_text)
        # Convert feedback to TF-IDF features
        feedback_tfidf = self.vectorizer.transform([processed_feedback])
        # Predict sentiment
        prediction = self.classifier.predict(feedback_tfidf)[0]
        # Get probability scores for both classes (positive and needs improvement)
        proba = self.classifier.predict_proba(feedback_tfidf)[0]

        # Return the predicted sentiment and the confidence level
        return {
            'sentiment': 'positive' if prediction == 1 else 'needs_improvement',
            'confidence': float(max(proba))  # Maximum confidence from the prediction probabilities
        }

    def get_top_feedback(self, df, sentiment, n=5):
        """
        Get the top 'n' feedback entries based on their predicted sentiment and confidence.
        """
        # Preprocess the data
        df['processed_feedback'] = df['Feedback_Text'].apply(self.preprocess_text)
        # Convert the feedback text into TF-IDF features
        tfidf_features = self.vectorizer.transform(df['processed_feedback'])
        # Predict sentiment for each feedback
        df['prediction'] = self.classifier.predict(tfidf_features)

        # Filter the data based on the sentiment (positive or needs_improvement)
        filtered_df = df[df['prediction'] == (1 if sentiment == 'positive' else 0)]

        # Get the confidence scores for each prediction
        filtered_df['confidence'] = self.classifier.predict_proba(tfidf_features)[:, 1 if sentiment == 'positive' else 0]

        # Return the top 'n' feedback based on the highest confidence
        return filtered_df.nlargest(n, 'confidence')[['Feedback_Text', 'confidence']]

    def save_model(self, filepath='feedback_model.pkl'):
        """
        Save the trained model to a file.
        """
        with open(filepath, 'wb') as f:
            pickle.dump({
                'vectorizer': self.vectorizer,
                'classifier': self.classifier
            }, f)

    @staticmethod
    def load_model(filepath='feedback_model.pkl'):
        """
        Load the trained model from a file.
        """
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                model = pickle.load(f)
                analyzer = FeedbackAnalyzer()
                analyzer.vectorizer = model['vectorizer']
                analyzer.classifier = model['classifier']
                return analyzer
        return None
