# Question: Count lines and words in input.txt and write counts to output.txt.
# Create input.txt in this folder before running.
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()
lines, words = len(text.splitlines()), len(text.split())
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(f"Number of lines: {lines}\nNumber of words: {words}\n")
print("Lines:", lines)
print("Words:", words)
print("Counts written to output.txt")
