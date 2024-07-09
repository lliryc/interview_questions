import itertools

def sherlockAndAnagrams(s):
    """
    Find the number of anagrammatic pairs of substrings in the given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of anagrammatic pairs of substrings.
    """
    # Generate a list of sorted substrings
    substrings = sorted([sorted(s[i:j]) for i in range(len(s)) for j in range(i + 1, len(s) + 1)])
    print(substrings)
    
    # Group the sorted substrings and count occurrences
    counts = list(filter(lambda x: x > 1, [len(list(group)) for key, group in itertools.groupby(substrings)]))
    
    # Calculate the number of anagrammatic pairs using the combination formula
    anagram_pairs = sum((count * (count - 1)) // 2 for count in counts)
    
    return anagram_pairs

def sherlockAnagrams2(s):
    """
    Alternative implementation to find the number of anagrammatic pairs of substrings in the given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of anagrammatic pairs of substrings.
    """
    l = len(s)
    
    # Generate a list of sorted substrings
    substrings = sorted([sorted(s[i:j]) for i in range(l) for j in range(i + 1, l + 1)])
    
    # Group the sorted substrings and count occurrences
    grouped_counts = [len(list(group)) for key, group in itertools.groupby(substrings)]
    
    # Filter out groups with only one occurrence
    filtered_counts = filter(lambda count: count > 1, grouped_counts)
    
    # Calculate the number of anagrammatic pairs using the combination formula
    anagram_pairs = sum((count * (count - 1)) // 2 for count in filtered_counts)
    
    return anagram_pairs

if __name__ == '__main__':
    print(sherlockAnagrams2("ifailuhkqq"))
