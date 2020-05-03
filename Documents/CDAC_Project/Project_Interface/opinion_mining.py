import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""

    # use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    for idx, score in sorted_items:
        fname = feature_names[idx]

        # keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    # create a tuples of feature,score
    # results = zip(feature_vals,score_vals)
    results = {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]] = score_vals[idx]

    return results


# put the common code into several methods
def get_keywords(feature_names, tfidf_transformer, docs_test, cv, idx):
    # generate tf-idf for the given document
    tf_idf_vector = tfidf_transformer.transform(cv.transform([docs_test[idx]]))

    # sort the tf-idf vectors by descending order of scores
    sorted_items = sort_coo(tf_idf_vector.tocoo())

    # extract only the top n; n here is 10
    keywords = extract_topn_from_vector(feature_names, sorted_items, 20)

    return keywords


def print_results(dt, idx, keywords):

    return dt[idx]


def opi_main(path1, path2):
    df_csv = path1
    df_csv1 = path2

    df_csv.replace(to_replace='[^a-zA-Z ]', value="", regex=True, inplace=True)
    df_csv = df_csv.iloc[:, 0].values
    # print(type(df_csv))

    df_csv = pd.DataFrame(df_csv)
    # print(type(df_csv))

    df_csv = df_csv.dropna(axis=0)
    # print(df_csv.isna().sum())
    # print(df_csv[0])

    docs = df_csv[0].tolist()
    cv = CountVectorizer(max_df=0.85)
    word_count_vector = cv.fit_transform(docs)
    # print(word_count_vector.shape)
    # print(list(cv.vocabulary_.keys())[:10])
    # print(list(cv.get_feature_names())[3000:3015])

    # you only needs to do this once
    feature_names = cv.get_feature_names()

    tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
    tfidf_transformer.fit(word_count_vector)
    # print(tfidf_transformer.idf_)

    df_csv1.replace(to_replace='[^a-zA-Z ]', value="", regex=True, inplace=True)
    df_csv1 = df_csv1.iloc[:, 4].values
    # print(type(df_csv1))

    df_csv1 = pd.DataFrame(df_csv1)
    # print(type(df_csv1))

    df_csv1 = df_csv1.dropna(axis=0)
    # print(df_csv1.isna().sum())
    # print(df_csv1[0])

    docs_test = []

    docs_test = [' '.join(df_csv[0][0: len(df_csv1[0])])]

    # print(docs_test)

    keywords = get_keywords(feature_names, tfidf_transformer, docs_test, cv, 0)
    result = print_results(docs_test, 0, keywords)
    return result
