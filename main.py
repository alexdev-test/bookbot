import sys

def file_content(file):
    with open(file) as f:
        file_content = f.read()
    return file_content

def word_count(book):
    file = file_content(book)
    words = file.split()
    return len(words)

def char_count(book):
    file = file_content(book)
    lower = file.lower()
    char_count = {}
    for char in lower:
        if char in char_count:
            if char.isalpha():
                char_count[char] = char_count[char] + 1
        elif char.isalpha():
            char_count[char] = 1 
    return char_count

def sort_on(dict):
    return dict["count"]

def prep_report(char_dict):
    report_list = []
    for key, value in char_dict.items():
        report_list.append({"char": key, "count": value})
    report_list.sort(reverse=True, key=sort_on)
    return report_list

def print_report(book, report):
    print(f"{word_count(book)} words found in the document")
    for entry in report:
        print(f"The character '{entry['char']}' was found {entry['count']} times")


def main(book):
    # file = file_content(book)
    print(f"--- Begin report of {book} ---")
    count = char_count(book)
    report = prep_report(count)
    print_report(book, report)

if __name__ == '__main__':
    main("./books/frankenstein.txt")