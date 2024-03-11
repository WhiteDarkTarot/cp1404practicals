def count_word_occurrences(text):
    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_word_length = max(len(word) for word in word_counts.keys())

    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


user_text = input("Text: ")
count_word_occurrences(user_text)
