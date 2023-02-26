from typing import List

from nltk.corpus import wordnet


# Check for spelling errors
def spell_check(sentence, pos_words) -> List[str]:
    spelling_errors = []
    for word in pos_words:
        if not wordnet.synsets(word[0]) and not word[0].isdigit():
            spelling_errors.append(word[0])

    return spelling_errors
