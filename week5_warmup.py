# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
text = "abracadabra"
print(text[4])
# b. Retrieve the second to last character.
print(text[-2])
# c. Find the first occurrence of the letter 'c'.
print(text.find("c"))
#prints 4
print(text[4])

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
text2= "abcdefghijklmnopqrstuvwxyz"
substring= text2.find("hij")
print(substring) 
print(text2[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(text2[0:14:2])

# c. Reverse the entire string using slicing.
print(text2[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
sentence="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
substring=sentence.find("John F. Kennedy")
print(substring)
print(sentence[83:])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
sentence2 = "Python is fun. Fun is good. Good is subjective."
print(sentence2.find("subjective"))
print(sentence2[36:46])
# b. Extract every third word.
sentence2 = sentence2.split()
print(sentence2[::3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
sentence3 = "MAY THE FORCE BE WITH YOU."
print(sentence3.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
word_list = "Make", " haste", " slowly."
joined_list= "" .join(word_list)
print(joined_list)
# b. Now, split the string at every occurrence of the letter 'a'.


# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
sentence4 = "Life is what happens when you are busy making other plans."
new_sentence=sentence4.replace( "busy", "distracted").replace("busy", "distracted")
print(new_sentence)

# b. Replace "plans" with "mistakes".
new_sentence2=sentence4.replace( "plans", "mistakes")
print(new_sentence2)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repetition= "iteration"*15
print(repetition)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
sentence5 =  "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
if "moonlight" in sentence5:
print(sentence5.find("moonlight"))

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
text = "Supercalifragilisticexpialidocious"
length = len(text)
print(length)
# b. Count the number of times the letter 'i' appears in the same word/phrase.
frequency = text.count("i")
print(frequency)