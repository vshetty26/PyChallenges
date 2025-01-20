def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["1. Berlin", "2. Paris", "3. Madrid", "4. Rome"],
            "answer": 2
        },
        {
            "question": "Which programming language is known as the backbone of web development?",
            "choices": ["1. Python", "2. C++", "3. JavaScript", "4. Java"],
            "answer": 3
        },
        {
            "question": "What is the smallest prime number?",
            "choices": ["1. 0", "2. 1", "3. 2", "4. 3"],
            "answer": 3
        },
    ]

    score = 0

    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        try:
            user_answer = int(input("Enter the number of your choice: "))
            if user_answer == q['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        print("-" * 30)

    print(f"Your final score is: {score}/{len(questions)}")
    print("Thank you for playing!")

quiz_game()
