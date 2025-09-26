# your code goes here!

class Anagram:
    def __init__(self, word):
        self._base_lower = word.lower()
        self._sorted_base = ''.join(sorted(self._base_lower))

    def match(self, candidates):
        """
        Return a list of candidates that are anagrams of the original word.
        - Comparison is case-insensitive.
        - Identical words (ignoring case) are NOT considered anagrams.
        """
        matches = []
        for candidate in candidates:
            candidate_lower = candidate.lower()
            if candidate_lower == self._base_lower:
                continue
            if ''.join(sorted(candidate_lower)) == self._sorted_base:
                matches.append(candidate)
        return matches
