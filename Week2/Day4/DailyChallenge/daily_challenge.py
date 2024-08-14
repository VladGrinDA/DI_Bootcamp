from collections import Counter 
import re
import nltk


nltk.download('stopwords')
# stops = set(nltk.corpus.stopwords.words('english'))
# print(stops)

# Side Note: When i started to implement solution using Counter object,
# I realized that it may not be the best approach but i still decided to make it work :) 

class Text:
    def __init__(self, text=None) -> None:
        self.__text = text
        self.stats = self.get_counts()

    def from_file(self, file_path):
        with open(file_path, 'r') as f:
            self.__init__(f.read())

    def _update_stats(self):
        self.stats = self.get_counts()

    def get_counts(self):
        return Counter(self.remove_special_chars(self.__text if self.__text else '').lower().split())

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, text):
        self.__text = text
        self._update_stats()

    def __str__(self) -> str:
        return self.text
    
    def __repr__(self) -> str:
        return str(self)
    
    def word_freq(self, word):
        return self.stats[word.lower()]
    
    def most_common(self):
        if len(self.stats.keys()) > 0:
            return self.stats.most_common()[0][0]

    def unique_words(self):
        return list(self.stats.keys())
    
    
    @staticmethod
    def remove_punctuation(text):
        return re.sub(r'[.,!?\-;:\"\[\]\(\)*]', '', text)
    
    @staticmethod
    def remove_stop_words(text):
        stopwords = set(nltk.corpus.stopwords.words('english'))
        return ' '.join([word for word in text.split() if Text.remove_punctuation(word.lower()) not in stopwords])
    
    @staticmethod
    def remove_special_chars(text):
        return re.sub(r'[^\w\s\']', '', text)
    
    


sample_text = "I i Albert Camus can't Camus Camus ♦ THE STRANGER 2.?!, 1,.!-[]()*' 12 "
    
t1 = Text(sample_text)
print(t1)
print(t1.stats)
print("Freq of the word Camus:", t1.word_freq('Camus'))
print("Most common word:", t1.most_common())
print("Unique words:", t1.unique_words())
print("Removing punctuation:", t1.remove_punctuation(t1.text))
print("Removing stopwords:", t1.remove_stop_words(t1.text))
print("Removing special chars:", t1.remove_special_chars(t1.text))

t2 = Text()
t2.from_file('the_stranger.txt')
print(t2.stats)
print("Freq of the word No:", t2.word_freq('No'))
print("Most common word:", t2.most_common())
print("Unique words:", t2.unique_words())
# print("Removing punctuation:", t2.remove_punctuation(t2.text))
# print("Removing stopwords:", t2.remove_stop_words(t2.text))
# print("Removing special chars:", t2.remove_special_chars(t2.text))