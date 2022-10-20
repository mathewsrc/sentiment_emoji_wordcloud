install:
		pip install --upgrade pip &&\
				pip install -r requirements.txt

download_corpora:
		python -m textblob.download_corpora

download_lite_corpora:
		python -m textblob.download_corpora lite

format:
		black ./text_process/*.py &&\
		black ./text_process/emoji_sentiment/*.py &&\
		black ./text_process/emoji_wordcloud/*.py

run_happy_example:
		python ./text_process/app.py --corpora 'sample_happ_data.txt' --wc_background 'white'

run_sad_example:
		python ./text_process/app.py --corpora 'sample_sad_data.txt' --wc_background 'black'
