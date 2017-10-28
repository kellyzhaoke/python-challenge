# coding: utf-8

f = open("paragraph_1.txt", "r")
x = open("paragraph_2.txt","r")

data = f.read()
f.close()

words = data.split(" ") 

num_words = len(words)

lines = data.split(".")

average_sentence=float(len(words))/float(len(lines))

average_words=(float(average_sentence)/float(len(lines)))

print("Paragrah Analysis for Paragraph 1")
print("----------------")
print("Approximate Word Count:", num_words)
print("Approximate Sentence Count:", len(lines))
print("Average Letter Count:", average_words)
print("Average Sentence Length:", average_sentence)

data = x.read()
x.close()

words = data.split(" ") 

num_words = len(words)

lines = data.split(".")

average_sentence=float(len(words))/float(len(lines))

average_words=(float(average_sentence)/float(len(lines)))


print("Paragrah Analysis for Paragraph 2")
print("----------------")
print("Approximate Word Count:", num_words)
print("Approximate Sentence Count:", len(lines))
print("Average Letter Count:", average_words)
print("Average Sentence Length:", average_sentence)
