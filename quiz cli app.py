dict1 = {
    'Which movie has a blue alien race called Na’vi?': {
        'option': ['Avatar', 'Star Wars', 'Guardians of the Galaxy', 'Dune'],
        'answer': 'Avatar'
    },
    'Which movie made dinosaurs scary again ?': {
        'option': ['King Kong', 'Jurassic Park', 'Godzilla', 'Ice Age'],
        'answer': 'Jurassic Park'
    },
    'Which movie shows  the quote “I am Iron Man”?': {
        'option': ['Batman', 'Iron Man', 'Avengers: Endgame', 'Spider-Man'],
        'answer': 'Avengers: Endgame'
    }
}

score = 0

for question, op_ans_dict in dict1.items():
    print(question)

    num = 1
    for eachop in op_ans_dict['option']:
        print(f"{num}. {eachop}")
        num += 1

    user_num = int(input("Enter the number of your answer: "))

    correct_answer = op_ans_dict['answer']
    selected_answer = op_ans_dict['option'][user_num - 1]

    if selected_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer is:", correct_answer)

print("\nYour final score:", score)