from textblob import TextBlob
import numpy as np
import click


def extract_sentiment(corpora):
    """Return the polarity of text"""
    textblob = TextBlob(corpora).correct()
    sentiment = textblob.sentiment.polarity
    click.echo(f"Sentiment: {sentiment}")
    return sentiment
