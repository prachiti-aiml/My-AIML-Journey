#Day 45:Pandas Sorting
import pandas as pd

#Creating sample DataFrame
data = {
    "Name":["Prachiti","Asha","Riya","Sam","Tom","Neha","Raj","Priya"],
    "Age":[18,19,20,18,21,19,22,20],
    "Marks":[78,85,92,60,75,88,45,95],
    "City":["Mumbai","Delhi","Pune","Chennai","Bangalore","Mumbai","Delhi","Pune"],
    "Course":["AI/ML","CS","IT","AI/ML","CS","IT","AI/ML","CS"]
}

df = pd.DataFrame(data)
print("Original DatFrame:\n",df)

#1.sort_values()-ascending
print("\nSorted by Marks (ascending):\n",
      df.sort_values("Marks"))

#2.sort_values() -descending
print("\nSorted by Marks (descending):\n",
      df.sort_values("Marks",ascending=False))
 
#3.Sort by Multiple columns
print("\nSorted by City then Marks:\n",
      df.sort_values(["City","Marks"],ascending=[True,False]))

#4.Sort by string column
print("\nSorted by Name alphabetically:\n",
      df.sort_values("Name"))

#5.sort_index()
df2 = df.sort_values("Marks",ascending=False)
print("\nAfter sorting by marks:\n",df2)
print("\nAfter reset and sort index:\n",
      df2.reset_index(drop=True))

#6.nLargest and nsmallest
print("\nTop 3 students by marks:\n",
      df.nlargest(3,"Marks"))

print("\nBottom 3 students by marks:\n",
      df.nsmallest(3,"Marks"))

#7.Rank
df["Rank"] =df["Marks"].rank(ascending=False).astype(int)
print("\nWith rank Column:\n",df.sort_values("Rank"))

#Mini Project:Student Leaderboard
print("\n    SUTDNET LEADERBOARD   ")
leaderboard = df.sort_values("Marks",ascending=False).reset_index(drop=True)
leaderboard.index += 1
leaderboard.index.name = "Position"
print(leaderboard[["Name","Marks","City","Course"]])

print("\nTop scorer:",leaderboard.iloc[0]["Name"],
      "with",leaderboard.iloc[0]["Marks"],"marks")
print("Last position:",leaderboard.iloc[-1]["Name"],
      "with",leaderboard.iloc[-1]["Marks"],"marks")