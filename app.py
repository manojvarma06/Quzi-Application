questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "Which language is used for AI and ML?",
        "options": ["A. C", "B. Python", "C. Java", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True/False?",
        "options": ["A. int", "B. string", "C. boolean", "D. float"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    ans = input("Your answer: ").upper()

    if ans == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nFinal Score:", score, "/", len(questions))