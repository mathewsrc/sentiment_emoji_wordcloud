from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='sentiment_emoji_wordcloud'
    version='0.0.1',
    author='Matheus Ribeiro',
    author_email='',
    description='Generate a sentiment emoji masked wordcloud',
    long_description=description,
    url='',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)