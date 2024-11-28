# Sentence Reverser Program

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    print(f"Reversed sentence: {reversed_sentence}")

if __name__ == "__main__":
    main()