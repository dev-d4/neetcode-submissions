class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for letter in s:
            if letter.isalnum():
                s_list.append(letter.lower())

        if s_list == s_list[::-1]:
            return True
        else:
            return False