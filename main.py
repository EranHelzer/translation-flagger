import itertools
import string
from typing import List, Tuple
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Define a list of stopwords to remove from the text
from arguments import parser
from stages.ambiguity_check import ambiguity_check
from stages.spell_check import spell_check

# Load the nltk resources
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')


stop_words = set(stopwords.words('english'))
table = str.maketrans('', '', string.punctuation)


stages = {
    "spelling": spell_check,
    "ambiguity": ambiguity_check
}


def tokenize(sentence: str) -> List[Tuple[str, str]]:
    tokens = word_tokenize(sentence)

    # Remove stopwords from the list of words
    # tokens = [word.translate(table) for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word.lower() not in stop_words]

    # Part-of-speech tagging
    return nltk.pos_tag(tokens)


def check_sentence(sentence: str) -> List[str]:
    pos_tokens = tokenize(sentence)

    issues_per_stage = [stage(sentence, pos_tokens) for stage in stages.values()]

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
    args = parser.parse_args()
    files = args.files
    # for file in files:
    #     check_file(file)
    check_file("resources/11289.txt")
