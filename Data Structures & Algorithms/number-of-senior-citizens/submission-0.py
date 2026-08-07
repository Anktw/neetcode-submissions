class Solution:
    def countSeniors(self, details: List[str]) -> int:
        n=0
        for l in range(len(details)):
            age = int(details[l][11:13])
            if age>60:
                n+=1
        return n