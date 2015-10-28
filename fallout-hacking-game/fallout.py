
import sys

from random import randint, shuffle


DIFFICULTY_MAP = {
    '1': {
        'words': 5,
        'length': 4
    },
    '2': {
        'words': 8,
        'length': 8
    },
    '3': {
        'words': 10,
        'length': 10
    },
    '4': {
        'words': 12,
        'length': 12
    },
    '5': {
        'words': 15,
        'length': 15
    }
}


def load_words(no_words, word_length):
    words = []
    with open('enable1.txt', 'r') as f:
        for line in f.readlines():
            if len(line.strip()) == word_length:
                words.append(line.strip())
    shuffle(words)
    return words[:no_words]


def game(words):
    print words
    lives = 4
    winner = words[randint(0, len(words)-1)]
    while lives > 0:
        guess = raw_input('Guess ({lives} left)?'.format(
            lives=lives
        ))
        errors = 0
        for i in xrange(len(guess)):
            if not winner[i] == guess[i]:
                errors += 1
        if not errors:
            return True
        else:
            lives -= 1
            print errors
    return False


def main():
    difficulty = sys.argv[1]
    difficulty_settings = DIFFICULTY_MAP[difficulty]
    no_words, word_length = difficulty_settings['words'], difficulty_settings['length']
    words = load_words(no_words, word_length)
    winner = game(words)

    print 'yay' if winner else 'nay'


if __name__ == '__main__':
    main()
