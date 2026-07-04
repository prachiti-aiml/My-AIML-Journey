#Day 35:Numpy Statistics

import numpy as np

#1.Basic Statistics
marks = np.array([45,78,92,33,67,88,55,21,99,60])

print("Marks:",marks)
print("\nMean:",np.mean(marks))
print("Median:",np.median(marks))
print("Std deviation:",np.std(marks))
print("Variance:",np.var(marks))
print("Min:",np.min(marks))
print("Max:",np.max(marks))
print("Sum:",np.sum(marks))
print("Range:",np.max(marks) - np.min(marks))

#2.Percentiles
print("\n25th percentile:",np.percentile(marks,25))
print("50th percentile:",np.percentile(marks,50))
print("75th percentile:",np.percentile(marks,75))

#3.Sorting
print("\nSorted marks:",np.sort(marks))
print("Sorted descending:",np.sort(marks)[::-1])
print("Index of sorted:",np.argsort(marks))

#4.Unique values
arr = np.array([1,2,2,3,3,3,4,4,5])
print("\nUnique values:",np.unique(arr))
print("Unique with counts:",np.unique(arr,return_counts=True))

#5.Correlation and covariance
a = np.array([1,2,3,4,5])
b = np.array([2,4,5,4,5])

print("\nCorrealtion:\n",np.corrcoef(a,b))
print("Covariance:\n",np.cov(a,b))

#Mini Project:Exam Results Analyzer
subjects = ["Maths","Science","English","History","Computer"]
scores = np.array([78,85,62,90,95])

print("\n      EXAMS RESULTS ANALYZER       ")
for i in range(len(subjects)):
    print(subjects[i],":",scores[i])

print("\nTotal marks:",np.sum(scores))
print("Average marks:",np.mean(scores))
print("Highest marks:",np.max(scores),"in",subjects[np.argmax(scores)])
print("Lowest marks:",np.min(scores),"in",subjects[np.argmin(scores)])
print("Std Deviation:",round(np.std(scores),2))
above_avg = [subjects[i] for i in range(len(subjects)) if scores[i] > np.mean(scores)]
print("Subjects above average:",above_avg)                                                                            