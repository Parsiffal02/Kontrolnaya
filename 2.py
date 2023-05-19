import os
path = 'C:/Users/mrgor/OneDrive/Рабочий стол/код/бидон/Kontrolnaya/Rob'
word_count = {}
for filename in os.listdir(path):

    if filename.endswith(".txt"):

      with open(path + filename) as f:

        lines = f.readlines()

for line in lines:

   words = line.split()

for word in words:

   word = word.strip(".,!?-()[]{}")

word = word.lower()

if word in word_count:
    word_count[word] += 1
else:
   word_count[word] = 1
most_common_word = ""
max_count = 0
for word, count in word_count.items():
   if count > max_count:
    most_common_word = word
max_count = count
print("Наиболее часто встречающееся слово:", most_common_word)
print("Частота встречаемости:", max_count)





