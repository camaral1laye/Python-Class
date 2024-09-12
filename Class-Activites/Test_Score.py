#This program test scores
print("This is 3 Test Score")
print()
print("Enter 3 test scores")
print("="*20)
test_score1 = int(input("Enter test score: "))
test_score2 = int(input("Enter test score: "))
test_score3 = int(input("Enter test score: "))
print("="*20)

total_score = test_score1+test_score2+test_score3
average_score = total_score/3

print(f"Total Score: {total_score:.0f}")
print(f"Average Score: {average_score:.0f}\n")
print("Bye!")
