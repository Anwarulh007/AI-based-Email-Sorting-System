#AI BASED EMAIL SORTING System
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the email dataset
data = pd.read_csv('email_dataset.csv')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['category'], test_size=0.2, random_state=42)

# Convert email text to numerical features using CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Make predictions on new emails
new_emails = [
    "Urgent: Project deadline extension",
    "Family gathering this Sunday",
    "Limited time offer: Buy one, get one free"
]

new_emails_vectorized = vectorizer.transform(new_emails)
predicted_categories = classifier.predict(new_emails_vectorized)

# Print predicted categories for new emails
for email, category in zip(new_emails, predicted_categories):
    print(f"Email: '{email}' => Predicted Category: '{category}'")