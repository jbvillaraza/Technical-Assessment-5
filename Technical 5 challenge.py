import re

# Starter lexicons (replace or extend with words from your chosen public datasets)
HAPPY_WORDS = {
    "happy", "joy", "joyful", "glad", "delighted", "cheerful", "excited",
    "thrilled", "elated", "content", "pleased", "ecstatic", "blissful",
    "hopeful", "optimistic", "grateful", "thankful", "love", "loved",
    "wonderful", "fantastic", "great", "awesome", "amazing", "smile", "smiling"
}

SAD_WORDS = {
    "sad", "unhappy", "sorrow", "sorrowful", "miserable", "depressed",
    "gloomy", "melancholy", "heartbroken", "grief", "grieving", "down",
    "blue", "hopeless", "despair", "lonely", "loneliness", "crying", "cry",
    "tears", "awful", "terrible", "horrible", "pain", "hurt", "regret"
}


def load_word_list(filepath: str) -> set[str]:
    """Load a newline-separated word dataset from a text file."""
    with open(filepath, "r", encoding="utf-8") as file:
        return {line.strip().lower() for line in file if line.strip()}


def tokenize(sentence: str) -> list[str]:
    """Extract lowercase words while stripping punctuation."""
    return re.findall(r"[a-z']+", sentence.lower())


def number_happy(sentence: str, happy_words: set[str] = HAPPY_WORDS) -> int:
    """Return the number of words in `sentence` found in the happy words dataset."""
    words = tokenize(sentence)
    return sum(1 for word in words if word in happy_words)


def number_sad(sentence: str, sad_words: set[str] = SAD_WORDS) -> int:
    """Return the number of words in `sentence` found in the sad words dataset."""
    words = tokenize(sentence)
    return sum(1 for word in words if word in sad_words)


def analyze_tone(sentence: str) -> None:
    happy_count = number_happy(sentence)
    sad_count = number_sad(sentence)

    if happy_count > sad_count:
        sentiment = "positive"
    elif sad_count > happy_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print(f"Happy words: {happy_count}")
    print(f"Sad words: {sad_count}")
    print(f"Analysis: The tone of the sentence is {sentiment}.")


def main() -> None:
    sentence = input("Enter a sentence: ")
    analyze_tone(sentence)


if __name__ == "__main__":
    main()
