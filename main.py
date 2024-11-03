def main():
    book_path = "/home/niklas/workspace/github.com/mooplol/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = count_characters(text)
    

    test = count_characters(text)
    #print(test)
    print(f"{num_words} words found in the document")
    print(num_characters)

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



main()


    