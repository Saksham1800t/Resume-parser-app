import re
import spacy

nlp = spacy.load("en_core_web_sm")

def get_number(text):
    """
    This function returns a list of phone numbers from a given text
    :param text: text to search for phone numbers
    :return: list of phone numbers
    """
    pattern = re.compile(r'([+(]?\d+[)\-]?[ \t\r\f\v]*[(]?\d{2,}[()\-]?[ \t\r\f\v]*\d{2,}[()\-]?[ \t\r\f\v]*\d*[ \t\r\f\v]*\d*[ \t\r\f\v]*)')
    pt = pattern.findall(text)

    pt = [re.sub(r'[,.]', '', ah) for ah in pt if len(re.sub(r'[()\-.,\s+]', '', ah)) > 9]
    pt = [re.sub(r'\D$', '', ah).strip() for ah in pt]
    pt = [ah for ah in pt if len(re.sub(r'\D', '', ah)) <= 15]

    for ah in list(pt):
        if len(ah.split('-')) > 3:
            continue
        for x in ah.split("-"):
            try:
                if x.strip()[-4:].isdigit():
                    if int(x.strip()[-4:]) in range(1900, 2100):
                        pt.remove(ah)
            except:
                pass

    number = list(set(pt))
    return number


def get_email(text):
    """
    This function returns a list of emails from the given text
    :param text: text to search for emails
    :return: list of emails
    """
    r = re.compile(r'[A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    return r.findall(str(text))


def rm_number(text):
    """
    This function removes phone numbers from the given text
    :param text: text to remove phone numbers from
    :return: text without phone numbers
    """
    pattern = re.compile(r'([+(]?\d+[)\-]?[ \t\r\f\v]*[(]?\d{2,}[()\-]?[ \t\r\f\v]*\d{2,}[()\-]?[ \t\r\f\v]*\d*[ \t\r\f\v]*\d*[ \t\r\f\v]*)')
    pt = pattern.findall(text)

    pt = [re.sub(r'[,.]', '', ah) for ah in pt if len(re.sub(r'[()\-.,\s+]', '', ah)) > 9]
    pt = [re.sub(r'\D$', '', ah).strip() for ah in pt]
    pt = [ah for ah in pt if len(re.sub(r'\D', '', ah)) <= 15]

    for ah in list(pt):
        if len(ah.split('-')) > 3:
            continue
        for x in ah.split("-"):
            try:
                if x.strip()[-4:].isdigit():
                    if int(x.strip()[-4:]) in range(1900, 2100):
                        pt.remove(ah)
            except:
                pass

    number = list(set(pt))
    for i in number:
        text = text.replace(i, " ")
    return text


def rm_email(text):
    """
    This function removes emails from the given text
    :param text: text to remove emails from
    :return: text without emails
    """
    pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
    pt = pattern.findall(text)
    email = list(set(pt))
    for i in email:
        text = text.replace(i, " ")
    return text


def get_name(text):
    """
    This function returns the candidate's name from the given text using a combination of spaCy's NER
    and rule-based matching for better accuracy.
    :param text: text to extract name from
    :return: name of the candidate
    """
    doc = nlp(text)

    # Rule-based extraction: Assume the name is typically in the first few lines
    lines = text.splitlines()
    for line in lines[:5]:  # Limit search to the first 5 lines
        potential_name = re.match(r"^[A-Za-z ,.'-]+$", line.strip())
        if potential_name:
            return potential_name.group().strip()

    # Fallback to spaCy NER for "PERSON" entity
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text.strip()

    return "Name not found"

def get_skills(text, skills):
    """
    This function returns a list of skills from the given text
    :param text: text to extract skills from
    :param skills: list of predefined skills
    :return: set of found skills
    """
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if token.is_alpha]
    
    # Match skills from the predefined skills list
    found_skills = {skill for skill in skills if skill in tokens}
    return found_skills
