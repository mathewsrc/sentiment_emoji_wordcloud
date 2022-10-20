import click
from emoji_sentiment.sentiment_analysis import extract_sentiment
from emoji_wordcloud.wordcloud_analysis import show_wordcloud


@click.command
@click.option("--corpora", required=True, help="input file name")
@click.option("--wc_background", default="black", help="The wordcloud background color")
def cli(corpora, wc_background):
    with open(corpora, "r", encoding="utf-8") as f:
        text = f.read()
        sentiment = extract_sentiment(text)
        show_wordcloud(text, sentiment, wc_background)


if __name__ == "__main__":
    cli()
