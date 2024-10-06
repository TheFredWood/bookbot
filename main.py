def count_words(s):
    words = s.split()
    return len(words)    

def count_letters(s):
    s = s.lower()
    d = {}
    for letter in s:
        if letter < 'a' or letter > 'z':
            continue
        if not letter in d:
            d[letter] = 0
        d[letter] += 1 
    return d

def sort_on(dict):
    return dict["num"]

def report_results(d):
    l = []
    for e in d:
       l.append({"letter":e, "num":d[e]}) 
    l.sort(reverse=True, key= sort_on)
    for e in l:
        print(f"The '{e["letter"]}' character was found {e["num"]} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        f.close()
    print(count_words(file_contents))

    letters = count_letters(file_contents)
    report_results(letters)

main() 