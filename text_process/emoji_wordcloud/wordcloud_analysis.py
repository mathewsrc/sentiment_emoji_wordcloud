from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def show_wordcloud(corpora, sentiment, background):
    """Generate a sad or happy wordcloud from a text"""
    # get a set of stop words
    stopwords = set(STOPWORDS)

    # get the mask
    mask = get_mask(sentiment)

    # generate a wordcloud from text
    wordcloud = WordCloud(
        stopwords=stopwords,
        mask=mask,
        max_font_size=50,
        max_words=500,
        background_color=background,
        colormap="Dark2",
    ).generate(corpora)

    plt.figure(figsize=[7, 7])
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def get_mask(sentiment):
    """Return a mask by transforming a png image to a numpy array and swipe black to white"""
    mask = []
    if sentiment > 0:
        mask = np.array(Image.open("emoji_images/1F642_color.png"))
        mask = np.where(mask == 0, 255, mask)
    else:
        mask = np.array(Image.open("emoji_images/1F643_color.png"))
        mask = np.where(mask == 0, 255, mask)
    return mask
