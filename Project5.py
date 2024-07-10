with open("Project5.txt",'r') as f:
    story = f.read()

print(story)
words = set()
word_start = -1

for i,char in enumerate(story):
    if char == '<':
        word_start = i

    if char == '>' and word_start != -1:
        word = story[word_start:i + 1]
        words.add(word)
        word_start = -1

answers = {}

for word in words:
    answer = input(f"Enter word to replace {word} :")
    answers[word] = answer

for word in words:
    story = story.replace(word,answers[word])

print(story)