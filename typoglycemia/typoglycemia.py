
import sys
from random import shuffle


def not_in_place_shuffle(lst):
    lst = list(lst)
    shuffle(lst)
    return ''.join(lst)


def get_required_newline(word):
    return '\n' if not len(word) == len(word.strip('\n')) else ''


def shuffle_word(word):
    stripped_word = word.strip('\n')
    return stripped_word[0] + not_in_place_shuffle(stripped_word[1:-1]) + stripped_word[-1]


def get_sentences(text):
    return text.split('.')


class Parser(object):

    def __init__(self, split_char, text):
        self.split_char = split_char
        self.text = text

    def parse(self):
        raise NotImplementedError


class TextParser(Parser):
    pass


class SentenceParser(Parser):

    def parse(self):
        pass


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        response_sentences = []
        sentences = get_sentences(f.read())
        for sentence in sentences:
            response_sub_sentences = []
            sub_sentences = sentence.split(',')
            for sub_sentence in sub_sentences:
                response_words = []
                words = sub_sentence.split(' ')
                for word in words:
                    scrambled_word = word
                    if len(word) > 2:
                        scrambled_word = get_required_newline(word) + shuffle_word(word)
                    response_words.append(scrambled_word)
                response_sub_sentences.append(' '.join(response_words))
            response_sentences.append(','.join(response_sub_sentences))
    print '.'.join(response_sentences)


if __name__ == '__main__':
    main()
