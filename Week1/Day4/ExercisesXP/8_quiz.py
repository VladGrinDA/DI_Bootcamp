# 🌟 Exercise 8 : Star Wars Quiz
# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

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
            play_again = input('You have more then 3 incorrect answers. Do you want to play again?')
            if play_again.lower() in 'yes':
                quiz()
            else:
                print('Bye')

if __name__ == '__main__':
    quiz()

