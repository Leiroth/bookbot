from stats import get_num_words, get_char_count, sort_char_count_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(path):
    with open(path) as i:
        return i.read()

book = get_book_text(path)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print (f"Found {get_num_words(book)} total words")
print("--------- Character Count -------")
char_count = get_char_count(book)
sorted_char_count = sort_char_count_dict(char_count)
for item in sorted_char_count:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")
print("============= END ===============")