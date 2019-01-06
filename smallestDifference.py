class Solution:
    """
    @param A: An integer array
    @param B: An integer array
    @return: Their smallest difference.
    """
    def smallestDifference(self, A, B):
        # write your code here
        A.sort()
        B.sort()
        i = 0
        j = 0
        diff = abs(A[0] - B[0])
        
        while i < len(A) and j < len(B):
            diff = min(diff, abs(A[i] - B[j]))
            
            if A[i] < B[j]:
                i += 1
            else:
                j += 1
        return diff
