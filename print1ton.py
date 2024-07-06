# platform - geeksforgeeks
#link - https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1
# concept - print 1 to n without using loops

class Solution:    
    def printNos(self,N):
        if N<=0:
              return;
        self.printNos(N-1);
        print(N,end=' ');
