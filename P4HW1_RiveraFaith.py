# CTI-110
# P4HW1 - Score List
# Faith Rivera
# 04/27/2023

# Ask user to enter for number of scores they would like to enter.
num_of_scores = int(input("How many scores do you want to enter? "))

# Create a loop to collect the number of scores the user wants to enter.
scores = []
for i in range(1, num_of_scores+1):
    score = float(input("Enter Score #" + str(i) + ": "))
    
    # Evaluate if the score is valid, it should be between 0 and 100 .
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter Score #" + str(i) + " again: "))
    
    scores.append(score)

# Sort scores in ascending order to drop the lowest score
scores.sort()

# Remove the lowest score from the list
dropped_score = scores.pop(0)

# Calculate the average of the remaining scores
avg_score = sum(scores) / len(scores)

# Assign letter grade based on average score
if avg_score >= 90:
    letter_grade = "A"
elif avg_score >= 80:
    letter_grade = "B"
elif avg_score >= 70:
    letter_grade = "C"
elif avg_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print("\n------Results------")
print("Lowest Score:", dropped_score)
print("Modified List:", scores)
print("Scores Average: {:.2f}".format(avg_score))
print("Grade:", letter_grade)
print("--------------------")
