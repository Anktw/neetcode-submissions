class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.strip()
        for l in range(len(s)-1,-1,-1):
            if s[l] == " ":
                break
            length +=1
        return length