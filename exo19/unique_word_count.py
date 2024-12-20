unique_words = set()
total_words = 0
while True:
    word = input("Enter a word: ").strip()
    total_words += 1
    if word in unique_words:
        print(f"\nYou typed in {len(unique_words)} unique words.")
        print(f"Total words entered: {total_words}")
        print("Unique words (sorted):", ", ".join(sorted(unique_words)))
        save_to_file = (
            input("Would you like to save the unique words to a file? (yes/no): ")
            .strip()
            .lower()
        )
        if save_to_file == "yes":
            filename = input("Enter the filename: ").strip()
            try:
                with open(filename, "w") as file:
                    file.write("\n".join(sorted(unique_words)))
                print(f"Unique words saved to {filename}.")
            except Exception as e:
                print(f"Error saving to file: {e}")

        break

    # Add the word to the set of unique wordsY
    unique_words.add(word)
