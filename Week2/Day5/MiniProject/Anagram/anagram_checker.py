# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.

# Note: None of the methods in the class should print anything.


from collections import Counter


class AnagramChecker:
    def __init__(self, file_path=None, words=None) -> None:
        self.words = self.init_words(file_path, words)
        self.anagrams = None

    def init_words(self, file_path, words):
        if words is not None:
            return  words
        elif file_path is not None:
            return self.load_words_from_file(file_path)
        else:
            raise ValueError("Either 'words' or 'file_path' must be provided")

    @staticmethod
    def load_words_from_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return set(f.read().lower().split('\n'))

    @staticmethod
    def char_counter_hash(word):
        """
        This function takes a dictionary where the keys are the characters of a word and the values are the counts of each character.
        It returns a string representing the character counts in alphabetical order (by character) and Counter object.
        That can be used as a hash for matching anagrams

        For example, if the input is {'a': 2, 'b': 3}, the output will be 'a2b3'.
        """
        char_cntr = Counter(word)
        return ''.join(sorted(['{}{}'.format(char, str(cnt)) for char, cnt in char_cntr.items()])), char_cntr


    @staticmethod
    def is_anagram(word1, word2):
        return Counter(word1) == Counter(word2)

    def compute_anagrams(self):
        """
        This method takes the word list and transforms it into an anagrams dictionary where:
        - Keys: the hashes of the character counts of the words (eg. 'a2b3')
        - Values: The dictionaries containing the character counter and the list of words that fit the character counter
        The result is stored in the self.anagrams variable.
        """
        anagrams = {}
        for word in self.words:
            char_hash, char_cntr = self.char_counter_hash(word)
            if char_hash in anagrams:
                anagrams[char_hash]['words'].append(word)
            else:
                anagrams[char_hash] = {'char_cntr': char_cntr, 'words': [word]}
        self.anagrams = anagrams
            
    def is_valid_word(self, word):
        return word in self.words
    
    def get_anagrams_brute(self, word, include=False):
        anagrams = []
        for candidate in self.words:
            if len(word) == len(candidate):
                if self.is_anagram(word, candidate) and (include or word != candidate):
                    anagrams.append(candidate)
        return anagrams

    def get_anagrams_pre_computed(self, word, include=False):
        char_hash, _ = self.char_counter_hash(word)
        if char_hash in self.anagrams:
            if include:
                return self.anagrams[char_hash]['words']
            else:
                return [anagram for anagram in self.anagrams[char_hash]['words'] if word != anagram]

    def get_anagrams(self, word, include=False):
        if self.anagrams:
            return self.get_anagrams_pre_computed(word, include=include)
        else:
            return self.get_anagrams_brute(word, include=include)



if __name__ == '__main__':
    import random
    import timeit

    file_path = 'sowpods.txt'
    word = 'meat'

    ac = AnagramChecker(file_path)
    print(ac.is_valid_word(word))
    char_cntr = ac.char_counter_hash(word)
    print(char_cntr)


    # print(Counter('mamar') == Counter('amamr'))


    n = 100

    print('Time to construct anagrams dict: ', timeit.timeit(lambda: ac.compute_anagrams(), number=1))
    print(f'Time to get anagram for {n} words from constucted dict: ', timeit.timeit(lambda: ac.get_anagrams_pre_computed(random.choice(list(ac.words))), number=n))
    print(f'Time to get anagram for {n} words with brute force: ', timeit.timeit(lambda: ac.get_anagrams_brute(word), number=n))

    words = ['team', 'meat', 'tame', 'mate', 'eatm', 'tea', 'moot',
            'mote', 'moat', 'oatm', 'tome', 'toem', 'omeat', 'meato']

    ac = AnagramChecker(words=words)

    ac.compute_anagrams()
    print(ac.anagrams)

    word = 'meat'
    print(word)
    print(ac.get_anagrams_pre_computed(word))
    print(ac.get_anagrams_brute(word))

    word = 'master'
    print(word)
    print(ac.get_anagrams_pre_computed(word))
    print(ac.get_anagrams_brute(word))


