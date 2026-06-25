#Day 14:String Methods

text = "Python is fun and powerful"

#1.strip - removes leading/trailing whitespace
print("Stripped:",text.strip())

#2.lower/upper
print("Lower:",text.lower())
print("Upper:",text.upper())

#3.Replace
print("Replace:",text.replace("Fun","Awesome"))

#4.split- breaks string into a list
words = text.strip().split()
print("Split:",words)

#5.Join - combines list iinto a string
joined = "-".join(words)
print("Joined:",joined)

#6.Find and Count
sentence = "Python is easy.Python is powerful."
print("Find 'Python':",sentence.find("Python"))
print("Count 'Python',:",sentence.count("Python"))

#7.Starswitch/endswitch
print("Starts with 'Python':",sentence.startswith("Python"))
print("Ends with 'powerful':",sentence.endswith("Python"))

#8.Formatting with str.format()
name = "Prachiti"
age = 18
greeting = "My name is {} and I am {} years old.".format(name,age)
print(greeting)

#Minin Project :Simple Text Analyzer
paragraph = input("\nEnter a sentence to analyze:")
word_count = len(paragraph.split())
char_count = len(paragraph.replace(" "," "))
upper_version = paragraph.upper()
reversed_text = paragraph[::-1]
vowel_count = sum(1 for ch in paragraph.lower()if ch in "aeiou")

print("\n  TEXT ANALYZER   ")
print("Word count:",word_count)
print("Character count (no spaces):",char_count)
print("Uppercase version:",upper_version)
print("Reversed text:",reversed_text)
print("Vowel count:",vowel_count)