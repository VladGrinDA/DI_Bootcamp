print('Exercise 1')

import random

def get_words_from_file(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as f:
        words = set(f.read().split('\n'))

    return words

def get_random_sentence(length):
    global words
    return ' '.join([random.choice(list(words)).lower() for _ in range(length)]) + '.'

def main():
    print("This program generates a random sentence based on a list of words.")
    
    try:
        length = int(input("How long do you want the sentence to be? (Enter a number between 2 and 20): "))
        
        if length < 2 or length > 20:
            raise Exception("Error: The sentence length must be between 2 and 20.")
        else:
            sentence = get_random_sentence(length)
            print(f"Generated sentence: {sentence}")
    
    except Exception as e:
        print(e)
        exit()
        

# Load words and run the main function
words = get_words_from_file('sowpods.txt')
main()


print('\n\nExercise 2')


import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sample_json = json.loads(sampleJson)
print(sample_json['company']['employee']['payable']['salary'])


sample_json['company']['employee']['birth_date'] = '1990-01-01'

with open('sample_json.json', 'w') as f:
    json.dump(sample_json, f, indent=4)




