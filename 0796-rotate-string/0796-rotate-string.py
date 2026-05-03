class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        r=s
        i=len(s)
        while(i>0):
            if r == goal:
                return True
            r=r[-1]+r[0:len(r)-1]  
            i-=1
        return False