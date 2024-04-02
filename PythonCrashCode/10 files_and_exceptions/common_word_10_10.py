from pathlib import Path

path = Path('gutenberg.txt')

contents = path.read_text()

count_the = contents.lower().count("the")

print("Number of 'the' is: ",count_the)

count_the_ = contents.lower().count("the ")
print("Number of 'the ' is: ",count_the_)