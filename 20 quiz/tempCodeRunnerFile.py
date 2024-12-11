def run_quiz():
    # List of dictionaries containing questions, choices and answers
    questions = [
        {
            "question": "What is the capital of India?",
            "choices": ["A. Modi ki Delhi", "B. Kejriwal ki Delhi", "C. Delhi", "D. Rahul ki Delhi"],
            "correct": "C"
        },
        {
            "question": "Which planet is known as the Black Planet?",
            "choices": ["A. Venus", "B. Just press B", "C. Jupiter", "D. Saturn"],
            "correct": "B"
        },
        {
            "question": "What is 2 + 2 + 2 + 2 + 2?",
            "choices": ["A. 3", "B. 4", "C. 5", "D. 6"],
            "correct": "B"
        }
    ,
        {
            "question": "What is the largest mammal?",
            "choices": ["A. Black Whale", "B. Blue Whale", "C. White Whale", "D. Pink Whale"],
            "correct": "B"
        },
        {
            "question": "Which element has the symbol 'Au'?",
            "choices": ["A. Pink Whale", "B. Amul Doodh", "C. Aurum", "D. Auntogin"],
            "correct": "C"
        },
        {
            "question": "When will World War III start?",
            "choices": ["A. 2036", "B. 2035", "C. 2037", "D. 2025"],
            "correct": "D"
        }
    ]

    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game!")
    print("------------------------")

    for i, q in enumerate(questions, 1):
        # Display question and choices
        print(f"\nQuestion {i}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        
        # Get user's answer
        while True:
            answer = input("\nYour answer (A/B/C/D): ").upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input! Please enter A, B, C, or D.")

        # Check answer and update score
        if answer == q['correct']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['correct']}")

    # Display final score
    print("\n------------------------")
    print(f"Quiz completed! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    run_quiz()