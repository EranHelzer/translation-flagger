import nltk
from nltk.corpus import wordnet


def ambiguity_check(sentence, pos_words):
    # Create a list of candidate words for each ambiguous word
    ambiguous_words = get_ambiguous_words(pos_words)

    # for word in ambiguous_words:
    #     print(f"Ambiguous word: '{word}' in sentence '{sentence}'")
    #     synsets = wordnet.synsets(word)
    #     best_synset = None
    #     best_score = -1
    #     for synset in synsets:
    #         context = synset.definition() + ' ' + ' '.join(synset.lemma_names())
    #         score = nltk.jaccard_distance(set(nltk.word_tokenize(context.lower())), set(pos_words))
    #         if score > best_score:
    #             best_synset = synset
    #             best_score = score
    #     if best_synset:
    #         print(f"Disambiguated sense: '{best_synset.definition()}'")

    return [f'Word: {word} is ambiguous' for word in ambiguous_words]


def get_ambiguous_words(pos_words):
    # Create a list of candidate words for each ambiguous word
    ambiguous_words = []
    for word, tag in pos_words:
        if tag in ['NN', 'VB', 'JJ', 'RB']:
            synsets = wordnet.synsets(word)
            if len(synsets) > 1:
                ambiguous_words.append((word, synsets))

    return ambiguous_words


def disambiguate(sentence, ambiguous_words):
    # Loop through each candidate and use context to disambiguate
    for word, synsets in ambiguous_words:
        for synset in synsets:
            hypernyms = synset.hypernyms()
            if hypernyms:
                for hypernym in hypernyms:
                    for example in hypernym.examples():
                        if example.lower() in sentence.lower():
                            print(f"Ambiguous word: '{word}' in sentence '{sentence}'")
                            print(f"Disambiguated sense: '{synset.definition()}'")
