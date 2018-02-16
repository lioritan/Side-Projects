from sklearn.preprocessing import LabelEncoder
import numpy as np
from nltk import FreqDist
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
stopwords = set(stopwords.words('english'))


def read_data_as_words(source_path):
    """
    Expects data with no punctuation and one sentence per line
    :param source_path:
    :return:
    """
    with open(source_path, 'r') as fptr:
        lines = fptr.readlines()

    punctuation_to_remove = {mark:None for mark in string.punctuation.replace('.', '')}
    words = [word.lower().translate(punctuation_to_remove) for line in lines for word in line.split()]
    words = [word for word in words if word not in stopwords]
    return words


def get_unique_words(words):
    return list(set(words))


def get_encoder(unique_words):
    enc = LabelEncoder()
    enc.fit(unique_words)
    return enc


def get_encoded_words(words, encoder):
    encoded_words = encoder.transform(words)
    return np.atleast_2d(encoded_words)


def get_word_frequencies(words):
    return FreqDist(np.squeeze(words))
