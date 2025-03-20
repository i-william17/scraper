import json
import os

#Files to store questions and scores
QUESTIONS_FILE = "questions.json"
SCORES_FILE = "scores.json"

def load_questions ():
    """Load questions from file"""
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "r") as file:
            return json.load(file)
    return []

def save_questions(questions):
    """Save questions to the file."""
    with open(QUESTIONS_FILE, "w") as file:
        json.dump(questions, file, indent=4)

def load_scores():
    """Load scores from the file"""
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as file:
            return json.load(file)
    return []

def save_scores (scores):
    """Save scores to a file"""
    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file, indent=4)

def take_quiz(questions):
    """Take the quiz and calculate the score."""
    score = 0
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for j, option in enumerate(question["options"], 1):
            print(f"{j}. {option}")
        answer = input("Your answer (1-4): ")
        if answer == str(question["answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
    print(f"\nYour final score is {score}/{len(questions)}.")
    return score

def view_leaderboard (scores):
    """Displays leaderboard"""
    if not scores:
        print("No scores available yet.")
    else:
        print("\nLeaderboard:")
        sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)
        for i, entry in enumerate(sorted_scores,1):
            print(f"{i}.{entry['name']}: {entry['score']} points")

def add_questions(questions):
    """Add a new question to the quiz"""
    question = input("enter the question:")
    options = [input(f"Enter option {i+1}:") for i in range(4)]
    answer = input("Enter the correct option number (1-4): ")
    if not answer.isdigit() or int (answer) < 1 or int(answer) > 4:
        print("Invalid answer. Questions not added")
        return
    questions.append({
        "question": question,
        "options": options,
        "answer": int(answer)
    })
    save_questions(questions)
    print("Question added successfully")

def main():
    """Main function to run the quiz app"""
    questions = load_questions()
    scores = load_scores()

    while True:
        print("\nQuiz application.")
        print("1. Take Quiz")
        print("2. View Leaderboard")
        print("3. Add Questions (Admin)")
        print("4. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            if not questions:
                print("No questions available. Add questions first!!")
            else:
                name = input("Enter your name:")
                score = take_quiz(questions)
                scores.append({"name": name, "score": score})
                save_scores(scores)
        elif choice == "2":
            view_leaderboard(scores)
        elif choice == "3":
            add_questions(questions)
        elif choice == "4":
            print("Exiting Quiz Application. Goodbye!! ")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()