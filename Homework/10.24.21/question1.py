"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2021
question1.py - DP planks with turtle
"""

### Longest Palindrome
test_cases = [
    "a", "abaab", "racecar", "bullet", "rarfile",
    "computer", "windows", "saippuakivikauppias",
    "aaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "kkkkkkkkkkkkkkkkkkkkkkdldkkkkkkkkkkkkkkkkkkkkkk",
    "ddddddddddddddddddddddddddddddddddddddddddddddddddks"
]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0  # Start position of longest palindrome
        end = 0  # End position of longest palindrome

        '''RUN TIME COMPLEXITY OF N^2'''

        for i in range(1, len(s)):

            # Palindome can be centered around 1 character or 2 characteres.
            # example aba  -> center is a
            #         abba -> center is bb
            # Try both methods and see which one gives the longer palindome.
            start1 = 0
            end1 = 0

            if len(s) % 2 != 0:  # if the length of s is odd
                for j in range(1, len(s)):

                    if (i - j >= 0) and (i + j) < len(s):
                        if s[i - j] == s[i + j]:
                            start1 = i - j
                            end1 = i + j

                        else:
                            if (end1 - start1) > (end - start):
                                end, start = end1, start1
                            break

                    else:
                        if (end1 - start1) > (end - start):
                            end, start = end1, start1
                        break

            if len(s) % 2 == 0:  # if the length of s is even
                for j in range(1, len(s)):

                    if (i - j >= 0) and (i + 1 + j) < len(s):
                        if s[i] == s[i + 1]:
                            start1 = i
                            end1 = i + 1
                            if s[i - j] == s[i + 1 + j]:
                                start1 = i - j
                                end1 = i + 1 + j

                            else:
                                if (end1 - start1) > (end - start):
                                    end, start = end1, start1
                                break

                    else:
                        if (end1 - start1) > (end - start):
                            end, start = end1, start1
                        break

        return s[start: end + 1]

    def expand_around(self, s, left, right):

        pass


if __name__ == "__main__":
    solution = Solution()

    for test_case in test_cases:
        print(solution.longestPalindrome(test_case))
