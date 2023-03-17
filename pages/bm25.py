import json
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
import string
from math import log
import operator
import timeit
import glob

# import punctuations
punctuations = string.punctuation
ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

supreme_court_cases_file_path = (
    "/Users/elijah.hoole/Documents/paralegal/cases_supreme_court"
)


with open("primary_key_filename_dict.json", "r") as f:
    primary_key_filename_dict = json.load(f)


def preprocess(text):
    # remove punctuation
    text = text.translate(str.maketrans("", "", punctuations))

    # convert to lower case
    text = text.lower()
    # tokenize
    tokens = word_tokenize(text)
    # remove stop words
    tokens = [w for w in tokens if not w in stop_words]
    # stem
    tokens = [ps.stem(w) for w in tokens]
    return tokens


def clean_query(query):
    # remove punctuations and replace with space
    tokens = preprocess(query)
    return " ".join(tokens)


##Github Version of pii.json
def createDocTable(data):
    dlt = defaultdict(int)
    for k, v in data.items():
        for p, q in v.items():
            dlt[p] += len(q)
    return dlt


def queryTokenFreq(query):
    query = clean_query(query)  ## Stemming
    query_token_freq = defaultdict(int)
    for i in set(query.strip().split()):
        query_token_freq[i] = query.split(" ").count(i)
    # print(query_token_freq)
    return query_token_freq


def score_BM25(n, f, qf, r, N, dl, avdl):
    k1 = 1.2
    k2 = 100
    b = 0.75
    R = 0.0
    K = compute_K(dl, avdl)
    first = log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))
    second = ((k1 + 1) * f) / (K + f)
    third = ((k2 + 1) * qf) / (k2 + qf)
    return first * second * third


def compute_K(dl, avdl):
    k1 = 1.2
    b = 0.75
    return k1 * ((1 - b) + (b * dl / avdl))


def search(query, data, dlt):
    query_token_freq = queryTokenFreq(query)

    sum_doc = 0

    for k, v in dlt.items():
        type(v)
        sum_doc += v
    avdl = sum_doc / len(dlt)

    query_doc_score = dict.fromkeys(dlt, 0)
    for k, v in data.items():
        if k in query_token_freq:
            for p, q in v.items():
                query_doc_score[p] += score_BM25(
                    len(data[k]),
                    len(q),
                    query_token_freq[k],
                    0,
                    len(dlt),
                    dlt[p],
                    avdl,
                )

    sorted_rank = sorted(
        query_doc_score.items(), key=operator.itemgetter(1), reverse=True
    )
    doc_list = []
    for i in sorted_rank:
        doc_list.append(i[0])

    return doc_list
