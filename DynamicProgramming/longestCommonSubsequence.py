
class longestCommongSubsequence():
    def __init__(self,stringone,stringtwo):
        self.stringone = '0'+stringone
        self.stringtwo = '0'+stringtwo
        self.DPtable = []
        self.commonsequence = ""

    def print_Strings(self):
        print(f"String one: {self.stringone}")
        print(f"String two: {self.stringtwo}")

    def CreateDptable(self):
        '''
                if two letters are equal then we will check the
                longestcommonsubsequence without the current letter
                and add one to it

                else we will consider the maximum of two below cases
                1) maximum subsequence with row,column-1
                2) without considering column i.e; row-1, column

                videolink:
                https://youtu.be/NnD96abizww?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
        '''
        for i in range(len(self.stringone)):
            self.DPtable.append([0 for j in range(len(self.stringtwo))])
        for i in range(0,len(self.stringone)):
            for j in range(0,len(self.stringtwo)):
                if self.stringone[i]==self.stringtwo[j]:
                    self.DPtable[i][j] = self.DPtable[i-1][j-1]+1
                else:
                    self.DPtable[i][j] = max(self.DPtable[i-1][j],self.DPtable[i][j-1])


    def retrievesequence(self):
        i = len(self.stringone)-1
        j = len(self.stringtwo)-1
        while(True):
            if i<=0 or j<=0:
                break
            if self.DPtable[i][j] != max(self.DPtable[i-1][j],self.DPtable[i][j-1]):
                self.commonsequence+=self.stringone[i]
                i = i-1
                j = j-1
            else:
                if self.DPtable[i-1][j]>self.DPtable[i][j-1]:
                    i -=1
                else:
                    j-=1
        self.commonsequence = self.commonsequence[::-1]


    def printDPtable(self):
        for i in range(len(stringone)):
            print(self.DPtable[i])

if __name__=='__main__':
    stringone = "acbcf"
    stringtwo = "abcdaf"
    lcs = longestCommongSubsequence(stringone,stringtwo)
    lcs.CreateDptable()
    lcs.printDPtable()
    lcs.retrievesequence()
    print(lcs.commonsequence)
    stringone = "Hemanth"
    stringtwo = "Hemanth"
    lcs = longestCommongSubsequence(stringone,stringtwo)
    lcs.CreateDptable()
    lcs.printDPtable()
    lcs.retrievesequence()
    print(lcs.commonsequence)
    stringone = "AGGTAB"
    stringtwo = "GXTXAYB"
    lcs = longestCommongSubsequence(stringone,stringtwo)
    lcs.CreateDptable()
    lcs.printDPtable()
    lcs.retrievesequence()
    print(lcs.commonsequence)
