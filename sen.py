import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

# Main function to interact with the sentiment analysis chatbot
def sentiment_chatbot():
    print("Hi! I'm a sentiment analysis chatbot. You can type a sentence and I'll analyze its sentiment.")
    print("Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Analyze sentiment of user input
        sentiment = analyze_sentiment(user_input)
        
        # Print sentiment analysis result
        print("Sentiment Analysis:", sentiment)

# Call the sentiment_chatbot function to start interaction
if __name__ == "__main__":
    sentiment_chatbot()
