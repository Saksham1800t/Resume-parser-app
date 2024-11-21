import re
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess(txt):
    """
    This function returns a preprocessed list of texts by removing extra spaces, special characters,
    stopwords, and converting all text to lowercase using spaCy.
    
    :param txt: list containing text data (e.g., resumes or job descriptions)
    :return: preprocessed list of texts
    """
    space_pattern = r'\s+'  # Multiple spaces
    special_letters = r"[^a-zA-Z#]"  # Remove any non-alphabetic characters (except '#' symbol)
    
    p_txt = []

    for resume in txt:
        text = re.sub(space_pattern, ' ', resume)

        text = re.sub(special_letters, ' ', text)

        doc = nlp(text)

        processed_tokens = [
            token.text.lower() 
            for token in doc 
            if token.is_alpha and not token.is_stop
        ]

        p_txt.append(" ".join(processed_tokens))

    return p_txt
