def score_summary(name, a, b, c):
   #  Convert the three score values to numbers. If conversion fails, return Invalid score.
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        return "Invalid score"

   #  If any score is below 0 or above 100, return Invalid score.
    if  not (0 <= a <= 100) or (0 <= b <= 100) or (0 <= c <= 100):
        return "Invalid score"

   # Otherwise calculate the average, round it to 2 decimal places
    average = round((a + b + c) / 3, 2)

   # Choose a grade, Grade is A for 90 and above, B for 80 and above, C for 70 and above, and F below 70.
    if average >= 90 and average <= 100:
        grade = "A"
    elif average >= 80 and average < 90:
        grade = "B"
    elif average >= 70 and average < 80:
        grade = "C"
    else:
        grade = "F"

   #  return a three-line report with labels Student, Average, and Grade
    return f"Student: {name}\nAverage: {average}\nGrade: {grade}"

print(score_summary("Alice", 80, 90, 200))