class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        sum1 = ''
        for i in digits:
            sum1 += str(i)
            
        return list(str(int(sum1)+1))