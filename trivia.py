questions = {"When the first-ever soccer World Cup happend? ": "1930",
             "Which country won the first-ever soccer World Cup in 1930? ": "Uruguay",
             "Which country has won the world cup five times? ": "Brazil",
             }

for question in questions:
    score = 0
    answer = input(question).capitalize()
    
    if answer != questions[question]:
        print("Wrong answer") 
        score += 1
    else:
        print("Rigth answer") 
print(f"Score: {score}")

