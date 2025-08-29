# TextStatistics.py

def text_statistics(text):
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    return char_count, word_count, sentence_count

if __name__ == "__main__":
    paragraph = input("Enter a paragraph:\n")
    chars, words, sentences = text_statistics(paragraph)

    print("\n--- Text Statistics ---")
    print("Characters:", chars)
    print("Words:", words)
    print("Sentences:", sentences)
