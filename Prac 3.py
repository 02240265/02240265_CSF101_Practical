def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

def count_unique_words(content):
    words = set(content.lower().split())
    return len(words)

# Test the function
num_unique_words = count_unique_words(content)
print(f"Number of unique words: {num_unique_words}")

def longest_word(content):
    words = content.split()
    return max(words, key=len) if words else ""

# Test the function
longest = longest_word(content)
print(f"Longest word: '{longest}'")

def count_specific_word(content, word):
    words = content.lower().split()
    return words.count(word.lower())

# Test the function
specific_word = 'the'  # Change this to any word you want to count
specific_word_count = count_specific_word(content, specific_word)
print(f"Occurrences of the word '{specific_word}': {specific_word_count}")

def percentage_longer_than_avg(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100 if words else 0

# Test the function
percentage_longer = percentage_longer_than_avg(content)
print(f"Percentage of words longer than average: {percentage_longer:.2f}%")

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    num_unique_words = count_unique_words(content)
    longest = longest_word(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Longest word: '{longest}'")
    print(f"Average word length: {avg_length:.2f} characters")
    
    specific_word = 'the'  # Change this to any word you want to count
    specific_word_count = count_specific_word(content, specific_word)
    print(f"Occurrences of the word '{specific_word}': {specific_word_count}")
    
    percentage_longer = percentage_longer_than_avg(content)
    print(f"Percentage of words longer than average: {percentage_longer:.2f}%")

# Run the analysis
analyze_text('sample.txt')