# import re
# import nltk
# #nltk.download('stopwords')
# from nltk.corpus import stopwords

# def preprocess(txt):
#     """
#     This function returns a preprocessed list of texts 
#     :param txt: list containing texts
#     :return: preprocessed list of texts
#     """
#     sw = stopwords.words('english')
#     space_pattern = '\s+'
#     special_letters =  "[^a-zA-Z#]]"
#     p_txt = []

#     for resume in txt : 
#         text = re.sub(space_pattern, ' ', resume)# remove extra spaces
#         text = re.sub(special_letters, ' ', text)#remove special characteres
#         text = re.sub(r'[^\w\s]', '',text)#remove punctuations
#         text = text.split() #split words in a text
#         text = [word for word in text if word.isalpha()] #keep alphabetic word
#         text = [w for w in text if w not in sw] #remove stop words
#         text = [item.lower() for item in text] #lowercase words
#         p_txt.append(" ".join(text))#joins all words

#     return p_txt
import re
import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

def preprocess(txt):
    """
    This function returns a preprocessed list of texts by removing extra spaces, special characters,
    stopwords, and converting all text to lowercase using spaCy.
    
    :param txt: list containing text data (e.g., resumes or job descriptions)
    :return: preprocessed list of texts
    """
    # Define regex patterns for removing special characters and extra spaces
    space_pattern = r'\s+'  # Multiple spaces
    special_letters = r"[^a-zA-Z#]"  # Remove any non-alphabetic characters (except '#' symbol)
    
    # Initialize an empty list to store preprocessed texts
    p_txt = []

    for resume in txt:
        # Step 1: Remove extra spaces
        text = re.sub(space_pattern, ' ', resume)

        # Step 2: Remove special characters (excluding '#' symbol for hashtags)
        text = re.sub(special_letters, ' ', text)

        # Step 3: Use spaCy for tokenization and stopword removal
        doc = nlp(text)

        # Step 4: Filter out stopwords, non-alphabetic tokens, and convert to lowercase
        processed_tokens = [
            token.text.lower() 
            for token in doc 
            if token.is_alpha and not token.is_stop
        ]

        # Step 5: Join tokens back into a single string
        p_txt.append(" ".join(processed_tokens))

    return p_txt
