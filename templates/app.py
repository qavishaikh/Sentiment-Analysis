from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Function to analyze sentiment of user input
def analyze_sentiment(sentence):
    # Analyze sentiment of the sentence
    sentiment_scores = sid.polarity_scores(sentence)
    
    # Determine sentiment label based on compound score
    if sentiment_scores['compound'] >= 0.05:
        return "positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        user_input = request.form['text']
        sentiment = analyze_sentiment(user_input)
        return render_template('index.html', sentiment=sentiment, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
