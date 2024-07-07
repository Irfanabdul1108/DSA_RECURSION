# platform - geeksforgeeks
#link - https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-n-to-1-without-loop
# concept - print n to 1 without using loops

class Solution:
    def printNos(self, n):
        if n<=0:
            return;
        print(n,end=' ')
        self.printNos(n-1);
