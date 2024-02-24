import random

def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    for question in questions:
        print(question['question'])
        for i, choice in enumerate(question['choices'], 1):
            print(f"{i}. {choice}")

        user_answer = input("Enter the number corresponding to your choice: ")
        
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question['choices']):
            user_choice = question['choices'][int(user_answer) - 1]
            
            if user_choice == question['answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {question['answer']}\n")
        else:
            print("Invalid input. Skipping this question.\n")

    print(f"Quiz completed! Your score is: {score}/{len(questions)}")

# Sample quiz questions
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'choices': ['London', 'Paris', 'Berlin', 'Rome'],
        'answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'choices': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
        'answer': 'Mars'
    },
    {
        'question': 'What is the largest mammal in the world?',
        'choices': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
        'answer': 'Blue Whale'
    }
]

# Run the quiz
run_quiz(quiz_questions)
