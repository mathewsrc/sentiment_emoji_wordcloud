install:
		python -m pip install --upgrade pip &&\
				pip install -r requirements.txt

download_corpora:
		python -m textblob.download_corpora

download_lite_corpora:
		python -m textblob.download_corpora lite

format:
		black  *.py &&\
		black ./text_process/emoji_sentiment/*.py &&\
		black ./text_process/emoji_wordcloud/*.py

run_happy_example:
		python app.py --corpora 'sample_happy_data.txt' --wc_background 'white'

run_sad_example:
		python app.py --corpora 'sample_sad_data.txt' --wc_background 'black'

all:
	install format
