#Day 15:List Comprehension

#1.Basic List Comprehension 
squares = [x*x for x in range(1,11)]
print(squares)

#2.List Comprehension with Condition
even_numbers = [x for x in range(1,21) if x%2 == 0]
print(even_numbers)

#3.List Comprehension with if-else
labels = ["even" if x%2 == 0 else "odd" for x in range(1,11)]
print(labels)

#4.List comprehension on strings
words = ["python","java","html","css"]
upper_words = [word.upper() for word in words]
print(upper_words)

#5.Nested List Comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened = [num for row in matrix for num in row]
print(flattened)
 
#Mini Project:Student Marks Filter
marks = [45,78,92,33,67,88,55,21,99,60]

passed_marks = [m for m in marks if m>=40]
failed_marks = [m for m in marks if m<40]
grades = ["A" if m >= 90 else "B" if m >= 75 else "C" if m >= 60 else "D" if m >= 40 else "Fail" for m in marks]

print("\n     STUDENT MARKS ANALYSIS    ")
print("All marks:",marks)
print("Passed:",passed_marks)
print("Failed:",failed_marks)
print("Grades:",grades)
