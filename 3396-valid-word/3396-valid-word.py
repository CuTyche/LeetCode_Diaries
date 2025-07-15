class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            return False
        if not word.isalnum():
            return False

        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False

        for char in word:
            if char.isalpha():
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant