def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    
    #print(count_words(file_contents))
    #print(count_characters(file_contents))

    print(f"-- Begin report of {path} --")
    print(f"{count_words(file_contents)} were found in the document")

    dict_of_characters = count_characters(file_contents)
    list_of_converted_dicts = list_and_convert_dict(dict_of_characters)
    list_of_converted_dicts.sort(reverse=True, key=sort_on)

    for converted_dict in list_of_converted_dicts:
        print(f"The '{converted_dict["character"]}' character was found {converted_dict["amount"]} times")

    print(f"-- End report --")


def list_and_convert_dict(dict):
    list_of_converted_dicts = []
    for character in dict:
        if character.isalpha():
            converted_dict = {}
            converted_dict["character"] = character
            converted_dict["amount"] = dict[character]
            list_of_converted_dicts.append(converted_dict)
    return list_of_converted_dicts

def sort_on(item_of_list):
    return item_of_list["amount"]

def count_words(text):
    list_of_words = text.split()
    number_of_words = len(list_of_words)
    return number_of_words

def count_characters(text):
    number_of_each_alaphabet = {}
    for character in text:
        if character.lower() in number_of_each_alaphabet:
            number_of_each_alaphabet[character.lower()] += 1
        else:
            number_of_each_alaphabet[character.lower()] = 1
    return number_of_each_alaphabet



main()