from textblob import TextBlob
import pandas as pd


def get_sentiment(t):
    blob = TextBlob(str(t))
    polarity = blob.polarity
    if polarity == 0:
        sentiment = 'Neutral'
    elif polarity > 0:
        sentiment = 'Positive'
    else:
        sentiment = 'Negative'
    return sentiment


def print_sentiment_analysis(df):
    sent = []
    for i in df['review_body']:
        sentiment = get_sentiment(i)
        sent.append({
            'text': i,
            'sentiment': sentiment
        })
    neutral, positive, negative = 0, 0, 0
    for info in sent:
        if info['sentiment'] == 'Neutral':
            neutral += 1
        elif info['sentiment'] == 'Positive':
            positive += 1
        elif info['sentiment'] == 'Negative':
            negative += 1

    count = neutral + negative + positive
    neutral = (neutral / count) * 100
    positive = (positive / count) * 100
    negative = (negative / count) * 100

    list01 = [positive, neutral, negative]

    return list01


def sent_any(csv):
    a = print_sentiment_analysis(csv)
    return a
