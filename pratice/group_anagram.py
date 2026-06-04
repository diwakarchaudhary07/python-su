def groupAnagrams(strs):
    anagrams = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in anagrams:
            anagrams[key] = []

        anagrams[key].append(word)

    return list(anagrams.values())

# Example
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))