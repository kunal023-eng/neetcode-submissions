class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        s1=s  
        s2=t  
        for i in range(n):
            if s1[i] not in dict:
                dict[s1[i]]=1
            else:
                dict[s1[i]] +=1
        for i in range(m):
            if s2[i] in dict:
                dict[s2[i]] -=1
            else:
                return False
        for i in range(m):
            if dict[s1[i]] !=0:
                return False
        return True                         