# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.decomposition import TruncatedSVD
# import pandas as pd


# def txt_features(p_resumetxt, p_jdtxt):
#     """
#     This function returns a dataframe of features 
#     extracted from a list of texts
#     :param p_resumetxt: preprocessed list of resume texts
#     :param p_jdtxt: preprocessed list of job description texts
#     :return: dataframe of features 
#     """
#     txt = p_resumetxt+p_jdtxt
#     tv = TfidfVectorizer(max_df=0.85,min_df=1,ngram_range=(1,3))
#     tfidf_wm = tv.fit_transform(txt)

#     tfidf_tokens = tv.get_feature_names_out()
#     df_tfidfvect = pd.DataFrame(data = tfidf_wm.toarray(),columns = tfidf_tokens)

#     return df_tfidfvect

# def feats_reduce(feats_df):

#     """
#     This function returns a reduced dimensionality of a dataframe of features
#     :param feats_df: dataframe of features extracted from a list of texts
#     :return: reduced dimensionality of a dataframe of features
#     """
#     dimrec = TruncatedSVD(n_components=30, n_iter=7, random_state=42)
#     feats_red = dimrec.fit_transform(feats_df)
#     # Converting transformed vector to list
#     feats_red = feats_red.tolist()
#     # Converting list to DataFrame
#     feat_red = pd.DataFrame(feats_red)

#     return feat_red

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import pandas as pd

def txt_features(p_resumetxt, p_jdtxt):
    """
    This function extracts text features from a list of preprocessed resume and job description texts 
    using TF-IDF Vectorizer and returns the features as a DataFrame.
    
    :param p_resumetxt: preprocessed list of resume texts
    :param p_jdtxt: preprocessed list of job description texts
    :return: DataFrame containing the extracted TF-IDF features
    """
    # Combine both resume and job description texts
    txt = p_resumetxt + p_jdtxt

    # Initialize TF-IDF Vectorizer with specified parameters
    tv = TfidfVectorizer(max_df=0.85, min_df=1, ngram_range=(1, 3))

    # Apply the vectorizer to the text data
    tfidf_wm = tv.fit_transform(txt)

    # Get the feature names (tokens)
    tfidf_tokens = tv.get_feature_names_out()

    # Create a DataFrame from the TF-IDF sparse matrix
    df_tfidfvect = pd.DataFrame(data=tfidf_wm.toarray(), columns=tfidf_tokens)

    return df_tfidfvect


def feats_reduce(feats_df):
    """
    This function reduces the dimensionality of the feature matrix using Truncated SVD 
    (Singular Value Decomposition) for dimensionality reduction.

    :param feats_df: DataFrame of features extracted from text
    :return: DataFrame with reduced dimensionality features
    """
    # Initialize TruncatedSVD for dimensionality reduction
    dimrec = TruncatedSVD(n_components=30, n_iter=7, random_state=42)

    # Apply dimensionality reduction
    feats_red = dimrec.fit_transform(feats_df)

    # Convert the transformed features to a DataFrame
    feat_red = pd.DataFrame(feats_red)

    return feat_red
