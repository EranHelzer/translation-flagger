import itertools
from typing import List, Tuple

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Define a list of stopwords to remove from the text
stop_words = set(stopwords.words('english'))


stages = {
}


def extract_pos_words(sentence: str) -> List[Tuple[str, str]]:
    words = word_tokenize(sentence)

    # Remove stopwords from the list of words
    words = [word for word in words if word.lower() not in stop_words]

    # Part-of-speech tagging
    return nltk.pos_tag(words)


def check_sentence(sentence: str) -> List[str]:
    pos_words = extract_pos_words(sentence)

    issues_per_stage = [stage(sentence, pos_words) for stage in stages.values()]

    return list(itertools.chain.from_iterable(issues_per_stage))


def check_line(line: str):
    # Remove leading and trailing white space
    line = line.strip()
    # Tokenize the line into sentences
    sentences = sent_tokenize(line)

    issues_per_sentence = [check_sentence(sentence) for sentence in sentences]

    return list(itertools.chain.from_iterable(issues_per_sentence))


def check_file(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            problems = check_line(line)

            if len(problems) > 0:
                print(f'Line: {line}\nProblems: {problems}\n\n')


if __name__ == '__main__':
    check_file("resources/11289.txt")
