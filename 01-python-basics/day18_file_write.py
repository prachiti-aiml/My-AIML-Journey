#Day 18:File Handling - Writing Files

#1. Writing to a file (overwrites existing content)
with open("notes.txt","a") as file:
    file.write("This is my first note.\n")
    file.write("Learning file handling in Python.\n")

#2.Appending to a file (adds without erasing old content)
with open("notes.txt","a") as file:
    file.write("This line was appended.\n")

#3.Writing multiple lines at once using writelines()
lines_to_add = ["Line A\n","Line B\n","Line C\n"]
with open("notes.txt","a") as file:
    file.writelines(lines_to_add)

#4.Reading back to confirm what was written
with open("notes.txt","r") as file:
    print("   CURRENT FILE CONTENT       ")
    print(file.read())

#Mini Project:Personal Diary App
print("    PERSONAL DIARY   ")
entry = input("Write todays diary entry:")
with open("diary.txt","a") as file:
    file.write(entry + "\n")
print("\nEntry saved! Here is your full diary so far:\n")
with open("diary.txt","r") as file:
    diary_lines = file.readlines()
for i in range(len(diary_lines)):
    print("Entry",i + 1,":",diary_lines[i].strip())