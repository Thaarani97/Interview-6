#TC - O(2^n*n)
#SC - O(n)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.result = []
        self.backtrack([])
        return self.result
    
    def check_vp(self,vp):
        count = 0
        for i in range(2*self.n):
                if vp[i] == '(':
                    count +=1
                else:
                    count-=1
                if count < 0:
                    return False   
        return count == 0
  
        
    def backtrack(self,vp):
        #print(vp)
        if len(vp) == 2*self.n:
            if self.check_vp(vp):
                self.result.append("".join(vp))
            
        else:          
            vp.append('(')
            self.backtrack(vp)
            vp.pop()
            vp.append(')')
            self.backtrack(vp)
            vp.pop()
