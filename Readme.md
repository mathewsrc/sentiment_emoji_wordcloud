# **This project uses TextBlob and Wordcloud libraries to generate sentiment emoji masked wordcloud**

### **Sentiment analysis**

Sentiment analysis is a text analysis method that detects polarity (e.g. a positive or negative opinion) 
within the text. Textblob is a python module used in Natural Language Processing (NLP) tasks like tokenization, 
text classification, spell checking, part-of-speech tagging, noun phrase extraction, translation and sentiment analysis. Textblob return 
the polarity score as float ranging from -1.0 to 1.0.

### **Word cloud**

Word cloud is a technique for visualizing  frequent words in a text where the size of the words represents their frequency.

### **Requirements**

Python 3.6 or latest version
A text file for which you want to generate a word cloud with the extension .txt. This project has three example files that can be used as
example (sample_happy_data.txt, sample_happy_data2.txt and sample_sad_data.txt)

### **Installing dependencies**
You can install dependencies by opening yor Terminal or Command Prompt and use one of these commands:

pip install -r requirements.txt

Or by using Makefile make command
make install

### **Running as CLI**

Simply, open your Terminal or Command Prompt and try one of these below commands:

python app.py --corpora 'sample_happy_data.txt' --wc_background 'white'

python app.py --corpora 'sample_sad_data.txt' --wc_background 'black'

Or by using Makefile and its command make you can just use one these commands on your Terminal or Command Prompt:

make run_happy_example

make run_sad_example
