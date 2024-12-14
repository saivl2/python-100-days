student_scores = [150, 142, 60, 123, 90, 156]

maximum_score = 0
for num in student_scores:
    current_score = num
    if current_score > maximum_score:
        maximum_score = current_score
print(maximum_score)
