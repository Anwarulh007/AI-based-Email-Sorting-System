## AI-Based Email Sorting System
This Python code utilizes Naive Bayes classification to categorize emails into different groups for the betterment of the users.

<p align="center"> 
 <img src="https://github.com/Anwarulh007/AI-based-Email-Sorting-System/blob/main/Email%20sort.jpg" alt="AI-Based Email Sorting System" style="width: auto; height: 400px;"/> 
</p>

**Dataset Overview**

<p align="center"> 
 <img src="https://github.com/Anwarulh007/AI-based-Email-Sorting-System/blob/main/Data%20Overview.jpg" alt="Dataset Overview" style="width: auto; height: 300px;"/> 
</p>

**Functionality**

* Loads email data: The code assumes a CSV file named "email_dataset.csv" exists in the same directory, containing email text and corresponding categories in separate columns.
* Splits data: The data is split into training and testing sets for model creation and evaluation.
* Feature extraction: CountVectorizer is used to convert email text data into numerical features, suitable for machine learning algorithms.
* Naive Bayes classification: A Multinomial Naive Bayes model is trained on the training data to learn classification patterns.
* Prediction on new emails: The trained model predicts categories for new, unseen emails.

**Use Case Diagram**

<p align="center"> 
 <img src="https://github.com/Anwarulh007/AI-based-Email-Sorting-System/blob/main/Use%20case%20diagram.jpg" alt="Use Case Diagram" style="width: auto; height: 300px;"/> 
</p>

**Data Flow Diagram**

<p align="center"> 
 <img src="https://github.com/Anwarulh007/AI-based-Email-Sorting-System/blob/main/data%20flow%20%20diagram.jpg" alt="Data Flow Diagram" style="width: auto; height: 300px;"/> 
</p>

## Output:
# Email: 'Urgent: Project deadline extension' => Predicted Category: 'Work'
# Email: 'Family gathering this Sunday' => Predicted Category: 'Personal'
# Email: 'Limited time offer: Buy one, get one free' => Predicted Category: 'Promotions'

**Technology Used**

* Python 
* pandas
* scikit-learn
* Naive Bayes Alogrithm


**Instructions**

* Ensure you have the required libraries installed (pip install pandas scikit-learn).
* Replace the placeholder email data in the new_emails list with your own emails for testing.
* Run the script.

**Recommendations**

This is a basic example. Real-world email classification might require more sophisticated techniques and data pre-processing.
The accuracy of the model depends on the quality of the training data.

**License**

This project is licensed under the MIT License.

## Made with 🤍 by Anwarul Haque
