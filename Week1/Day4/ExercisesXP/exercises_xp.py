#1
print(10 * '-' + '\n', 'Exercise 1')

def display_message():
    print('In this course we are learning Data Analysis!')

display_message()

#2
print(10 * '-' + '\n', 'Exercise 2')

def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('Alice in Wonderland')

#3
print(10 * '-' + '\n', 'Exercise 3')

def describe_city(city='Reykjavik', country='Iceland'): 
    print(f"{city} is in {country}")

describe_city()

#4
print(10 * '-' + '\n', 'Exercise 4')

import random

def compare_with_random(number):
    random_number = random.randint(1, 100)
    if number == random_number:
        print('Success')
    else:
        print('Fail')
    print(number)
    print(random_number)


compare_with_random(50)

#5
print(10 * '-' + '\n', 'Exercise 5')

def make_shirt(size='large', text='I love Python'):
    print(f'The size of the shirt is {size} and the text is {text}')


make_shirt()
make_shirt(size='medium')
make_shirt(size='small', text='I love Python too')
make_shirt(text='I love Python', size='medium')

#6
print(10 * '-' + '\n', 'Exercise 6')

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians():
    for name in magician_names:
        print(name)

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = 'The Great ' + magician_names[i]

make_great(magician_names)
show_magicians()

#7
print(10 * '-' + '\n', 'Exercise 7')

import random

def get_random_temp(season=''):
    season_ranges = {
        'spring': (10, 25),
        'summer': (20, 40),
        'autumn': (0, 15),
        'winter': (-10, 5)
    }
    
    if season not in season_ranges:
        return None

    temp = random.random() * (season_ranges[season][1] - season_ranges[season][0]) + season_ranges[season][0]
    return temp


def main():
    month = int(input('Enter a month number: '))
    season = ['spring', 'summer', 'autumn', 'winter'][(month - 1) // 3]
    temp = get_random_temp(season)
    message = f'The season is {season} and t4he temperature right now is {temp:.2f} degrees Celsius.'
    if temp < 0:
        message += ' Brrr, that\'s freezing! Wear some extra layers today'
    elif temp < 16:
        message += ' Quite chilly! Don\'t forget your coat'
    elif temp < 23:
        message += ' Perfect weather. You should go for a walk!'
    elif temp < 32:
        message += ' Pretty warm. You should wear some shorts today'
    else:
        message += ' Really hot. Don\'t forget to wear a hat today'
    print(message)

main()

#8
print(10 * '-' + '\n', 'Exercise 8')

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def quiz():
    global data
    correct_answers_count = 0
    incorrect_answers = []
    for question in data:
        answer = input(question['question'] + ' ')
        if answer == question['answer']:
            correct_answers_count += 1
            print('Correct!')
        else:
            incorrect_answers.append(question)
            incorrect_answers[-1]['user_answer'] = answer
            print('Wrong')
    
    print(10 * '-' + '\n\n')
    print(f'You\'ve got {correct_answers_count} correct answers out of {len(data)}')

    if len(incorrect_answers) > 0:
        print('You got these questions wrong:')
        for question in incorrect_answers:
            print(question['question'])
            print(f'Your answer: {question["user_answer"]}')
            print(f'Correct answer: {question["answer"]}')
    
        if len(incorrect_answers) > 3:
            play_again = input('You have more then 3 incorrect answers. Do you want to play again? ')
            if play_again.lower() in 'yes':
                quiz()
            else:
                print('Bye')


quiz()