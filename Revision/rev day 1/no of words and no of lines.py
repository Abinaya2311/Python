def count_words(line):
    words = line.split()
    return len(words)

def count_lines(paragraph):
    lines = paragraph.split('\n')
    return len(lines)

paragraph = """This is an example of a paragraph.
It contains multiple lines of text.
Each line may have a different number of words.
But the total number of words in the paragraph
can be calculated by adding up the number of words
in each line."""

num_lines = count_lines(paragraph)
print(f"Number of lines: {num_lines}")

total_words = 0
for line in paragraph.split('\n'):
    num_words = count_words(line)
    total_words += num_words
    print(f"Line has {num_words} words")

print(f"Total number of words: {total_words}")
