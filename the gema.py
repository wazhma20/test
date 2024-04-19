def play_game():
    """Plays the calculator game."""
    score = 0
    num_questions = 5

    print("Welcome to the Calculator Game!")
    print("Answer the following arithmetic questions:")

    for _ in range(num_questions):
        question, correct_answer = "generate_question" ()
        print(question)
        user_answer = float(input("Enter your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is {score}/{num_questions}.")

play_game()
