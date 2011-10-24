import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer

stemmer = LancasterStemmer()
stopwords = {word for word in stopwords.words('english')}

def get_stems(query):
    """ Tokenize and stem query """
    query = re.sub('[^\w]', ' ', query)
    query = word_tokenize(query)
    filtered_words = [stemmer.stem(word) for word in query if word not in stopwords]
    return filtered_words

#def search(
