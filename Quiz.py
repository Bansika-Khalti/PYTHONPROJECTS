score = 0
answer1 = input("2 + 2 = ? ")
if answer1 == "4":
    score += 1
else:    score -= 1
answer2 = input("Capital of France? ")
if answer2.lower() == "paris":
    score += 1
else:
    score -= 1
print("Your score is: " + str(score))
