# platform - geeksforgeeks
# link -https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-1-to-n-without-using-loops
# concept - print n times without using loops

class Solution:    
    def printNos(self,N):
        if N<=0:
              return;
        self.printNos(N-1);
        print(N,end=' ');
              




