import re
import os

input_file = os.path.join('raw_data', 'paragraph_0.txt')

with open(input_file, 'r', newline='') as text:
    lines = text.read()

word_count = 0
sentence_count = 0
letter_count = 0
sentence_length = 0

# count word
words = re.split('\W+', lines)[:-1]
# print(words)
word_count = len(words)

# count sentence
# sentences = re.split(r"(?<=[.!?]) +", lines)
sentences = re.split('[.!?]', lines)

# print(sentences)
sentence_count = len(sentences)

# count letter
word_total_length = 0
for i in range(word_count):
    word_total_length = word_total_length + len(words[i])
letter_count = word_total_length / word_count

# count sentence length
sentence_total_length = 0
for i in range(len(sentences)):
    sentence_total_length = sentence_total_length + len(sentences[i])
sentence_length = sentence_total_length / sentence_count

# print
print('Paragraph Analysis\n-------------------')
print('Approximate word count: ' + str(word_count))
print('Approximate Sentence Count: ' + str(sentence_count))
print('Average Letter Count: ' + str(letter_count))
print('Average Sentence Length: ' + str(sentence_length))
