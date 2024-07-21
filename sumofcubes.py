# platform - geeksforgeeks
#link - https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1
# concept - sum of cubes in o(1)

class Solution:
    def sumOfSeries(self,n,total=0):
        p=(n*(n+1))//2;
        return p*p;