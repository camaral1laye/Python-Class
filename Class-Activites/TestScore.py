def display_welcome_message():
    print("The Test Scores application")
    print()
    print("Enter test scores")
    print("Enter 'x' to end input")
    print("======================")

def get_test_scores():
    scores = []
    while True:
        test_score = input("Enter test score (or 'x' to quit): ")
        if test_score == "x":
            break
        try:
            test_score = int(test_score)
            if test_score < 0 or test_score > 100:
                print("Test score must be from 0 through 100. Score discarded. Try again.")
            else:
                scores.append(test_score)
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100 or 'x' to quit.")
    return scores

def calculate_average(scores):
    return round(sum(scores) / len(scores))

def display_results(score_total, average_score):
    print("======================")
    print(f"Total Score: {score_total}")
    print(f"Average Score: {average_score}")
    print()
    print("Bye")

def main():
    display_welcome_message()
    scores = get_test_scores()
    if scores:
        score_total = sum(scores)
        average_score = calculate_average(scores)
        display_results(score_total, average_score)
    else:
        print("No valid scores entered. Bye.")

if __name__ == "__main__":
    main()