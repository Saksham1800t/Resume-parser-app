# from extract_txt import read_files
# from txt_processing import preprocess
# from txt_to_features import txt_features, feats_reduce
# from extract_entities import get_number, get_email, rm_email, rm_number, get_name, get_skills, get_location
# from model import simil
# import pandas as pd
# #import nltk
# #nltk.download('omw-1.4')


# if __name__=="__main__":
#     directory = '/home/ayoub/DS/Parser-Shortlisting-Project/Data/'
#     resume_path = '/home/ayoub/DS/Parser-Shortlisting-Project/files/resumes'
#     jd_path = directory + 'JobDesc/'

#     resumetxt=read_files(resume_path)
#     p_resumetxt = preprocess(resumetxt)

#     jdtxt=read_files(jd_path)
#     p_jdtxt = preprocess(jdtxt)
    
#     feats = txt_features(p_resumetxt, p_jdtxt)
#     feats_red = feats_reduce(feats)

#     df = simil(feats_red, p_resumetxt, p_jdtxt)

#     t = pd.DataFrame({'Original Resume':resumetxt})
#     dt = pd.concat([df,t],axis=1)
#     dt['Phone No.']=dt['Original Resume'].apply(lambda x: get_number(x))
    
#     dt['E-Mail ID']=dt['Original Resume'].apply(lambda x: get_email(x))

#     dt['Original']=dt['Original Resume'].apply(lambda x: rm_number(x))
#     dt['Original']=dt['Original'].apply(lambda x: rm_email(x))
#     dt['Candidate\'s Name']=dt['Original'].apply(lambda x: get_name(x))

#     skills = pd.read_csv('/home/ayoub/DS/Parser-Shortlisting-Project/Data/skill_red.csv')
#     skills = skills.values.flatten().tolist()
#     skill = []
#     for z in skills:
#         r = z.lower()
#         skill.append(r)

#     dt['Skills']=dt['Original'].apply(lambda x: get_skills(x,skill))
#     dt['Location']=dt['Original'].apply(lambda x: get_location(x))
#     print(dt['Location'].head(30))

from extract_txt import read_files
from txt_processing import preprocess
from txt_to_features import txt_features, feats_reduce
from extract_entities import get_number, get_email, rm_email, rm_number, get_name, get_skills
from model import simil
import pandas as pd
import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

def get_location(text):
    """
    Extracts locations from the given text using spaCy's NER.
    :param text: text to extract locations from
    :return: comma-separated string of locations
    """
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]
    return ", ".join(set(locations)) if locations else "Location not found"

if __name__ == "__main__":
    directory = '/home/ayoub/DS/Parser-Shortlisting-Project/Data/'
    resume_path = '/home/ayoub/DS/Parser-Shortlisting-Project/files/resumes'
    jd_path = directory + 'JobDesc/'

    # Read and preprocess resume and job description files
    resumetxt = read_files(resume_path)
    p_resumetxt = preprocess(resumetxt)

    jdtxt = read_files(jd_path)
    p_jdtxt = preprocess(jdtxt)

    # Extract features from the processed text
    feats = txt_features(p_resumetxt, p_jdtxt)
    feats_red = feats_reduce(feats)

    # Calculate similarity between resume and job description
    df = simil(feats_red, p_resumetxt, p_jdtxt)

    # Create a dataframe for storing original resumes and extracted information
    t = pd.DataFrame({'Original Resume': resumetxt})
    dt = pd.concat([df, t], axis=1)

    # Extract phone numbers and email IDs
    dt['Phone No.'] = dt['Original Resume'].apply(get_number)
    dt['E-Mail ID'] = dt['Original Resume'].apply(get_email)

    # Remove phone numbers and emails, then extract candidate's name
    dt['Original'] = dt['Original Resume'].apply(rm_number).apply(rm_email)
    dt['Candidate\'s Name'] = dt['Original'].apply(get_name)

    # Load and prepare the skills list
    skills = pd.read_csv('/home/ayoub/DS/Parser-Shortlisting-Project/Data/skill_red.csv')
    skills = skills.values.flatten().tolist()
    skills = [skill.lower() for skill in skills]  # Convert all skills to lowercase

    # Extract skills from resumes
    dt['Skills'] = dt['Original'].apply(lambda x: get_skills(x, skills))

    # Extract location using the spaCy-based `get_location`
    dt['Location'] = dt['Original'].apply(get_location)

    # Print the extracted location for review
    print(dt['Location'].head(30))
