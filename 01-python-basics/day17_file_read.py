#Day 17:File Handling - Reading Files

#1.Writing some sample data first(so we have a file to read)
with open("sample.txt","w") as file:
    file.write("Python is fun\n")
    file.write("AI and ML are the future\n")
    file.write("Practice makes perfect\n")

#2.Reading the entire file at once
with open("sample.txt","r") as file:
    content = file.read()
print("    FULL FILE CONTENT      ")
print(content)

#3.Reading line by line
print("    Line by Line     ")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

#4.Reading all lines into a list
with open("sample.txt","r") as file:
    lines = file.readlines()
print("\nLines as a list:",lines)

#5.Reading a single line
with open("sample.txt","r") as file:
    first_line = file.readline()
print("\nFirst line only:",first_line.strip())

#Mini Project: Word Counter from a File
with open("sample.txt","r") as file:
    text = file.read()
word_count = len(text.split())
line_count = len(text.splitlines())
char_count = len(text.replace(" "," ").replace("\n",""))

print("\n FILE STATISTICS   ")
print("Total words:",word_count)
print("Total lines:",line_count)
print("Total characters (no spaces):",char_count)
search_word = input("\nEnter a word to search in the file:")
if search_word.lower() in text.lower():
    print("'" + search_word + "' was found in the file!")
else:
    print("'" + search_word + "' was not found in the file!")