def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    text = text.lower()
    chars = {}
    for words in text:
        for char in words:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_report(dict):
    report = list()
    for key, value in dict.items():
        report.append({"char": key, "num": value})
    report.sort(reverse=True, key=sort_on)
    return report
