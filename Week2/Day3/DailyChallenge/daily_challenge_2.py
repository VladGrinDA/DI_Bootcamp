from googletrans import Translator

def translate_words(words, translator):
    return {word: translator.translate(word, src='fr', dest='en').text for word in words}


translator = Translator()
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
print(translate_words(french_words, translator))

