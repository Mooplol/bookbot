def main():
    book_path = "/home/niklas/workspace/github.com/mooplol/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = count_characters(text)
    sorted_characters = sort_characters(num_characters)
    create_report(num_words,sorted_characters)
    
    
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters(text):
    lowered_text = text.lower()
    dictionary_character_count = {}
    for txt in lowered_text:
        if txt not in dictionary_character_count:
            dictionary_character_count[txt] = 1

        else:
            dictionary_character_count[txt] += 1

    return dictionary_character_count


def sort_characters(num_characters):
    num_characters_list = list(num_characters.items())
    num_characters_list.sort(reverse=True, key=lambda num_characters_list: num_characters_list[1])
    
    

    return num_characters_list

def create_report(num_words, sorted_characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for char in sorted_characters:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")

    print("--- End report ---")

    return None
        

main()


    