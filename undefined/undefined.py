class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = ['a', 'e', 'i', 'o', 'u']
        return sum(map(lambda x: 1, filter(lambda word: word[0] in vowel and word[-1] in vowel, words[left:right+1])))