# from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd

# def simil(feats, p_resumetxt, p_jdtxt):
#     """
#     This function returns a dataframe of similiraty scores
#     between resumes and job description
#     :param p_resumetxt: preprocessed list of resume texts
#     :param p_jdtxt: preprocessed list of job description texts
#     :param feats: dataframe of text features
#     :return: dataframe of similiraty scores 
#     """
#     similarity = cosine_similarity(feats[0:len(p_resumetxt)],feats[len(p_resumetxt):])
#     abc = []
#     for i in range(1,len(p_jdtxt)+1):
#         abc.append(f"JD {i}")

#     # DataFrame of similarity score
#     df_sim=pd.DataFrame(similarity,columns=abc)

#     return df_sim



from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def simil(feats, p_resumetxt, p_jdtxt):
    """
    This function returns a dataframe of similarity scores
    between resumes and job descriptions.
    
    :param feats: DataFrame of text features (should be a combined feature set for both resumes and job descriptions)
    :param p_resumetxt: preprocessed list of resume texts
    :param p_jdtxt: preprocessed list of job description texts
    :return: DataFrame of similarity scores
    """
    # Compute cosine similarity between resume features and job description features
    similarity = cosine_similarity(feats[0:len(p_resumetxt)], feats[len(p_resumetxt):])

    # Create a list of labels for job descriptions (e.g., 'JD 1', 'JD 2', ...)
    job_desc_labels = [f"JD {i}" for i in range(1, len(p_jdtxt) + 1)]

    # Create a DataFrame to store similarity scores, with job description labels as columns
    df_sim = pd.DataFrame(similarity, columns=job_desc_labels)

    return df_sim

