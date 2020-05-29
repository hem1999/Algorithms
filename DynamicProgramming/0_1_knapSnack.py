
class knapSnackDP():
    def __init__(self,max_weight,weights=[],values=[]):
        self.weights = weights
        self.values = values
        self.max_weight = max_weight
        self.taken_weights = [False for i in self.weights]
        self.DPtable = []

    def print_table(self):
        for i,j in zip(self.weights,self.values):
            print(i,'________',j)

    def createDPtable(self):
        '''
            so basic intitution is that we follow below steps:
            1) if current weight in columns is less than the present weight with
                respect to row, we take the above of the present i,j
            2) if current weight in columns is greater than or equal to present weight with
                respect to row, we have two cases:
                1) consider that row weight to be taken then over values will
                    value of present row weight + value with out that weight
                2) we don't consider present row weight so it will be same as above of i,j
                so we take maximum of both

            video explanation:
            https://youtu.be/8LusJS5-AGo?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

        '''
        for i in self.weights:
            self.DPtable.append([0 for j in range(self.max_weight+1)])
        for i in range(len(self.weights)):
            for j in range(self.max_weight+1):
                if j<self.weights[i]:
                    self.DPtable[i][j]=self.DPtable[i-1][j]
                else:
                    self.DPtable[i][j]=max(self.values[i]+self.DPtable[i-1][j-self.weights[i]],self.DPtable[i-1][j])



    def retrieveWeights(self):
        i = len(self.weights)-1
        j = self.max_weight
        print(i,j)
        while(True):
            if self.DPtable[i][j] == 0 or i<=0 or j<=0:
                break
            if self.DPtable[i][j] == self.DPtable[i-1][j]:
                i = i-1
                j = j
            else:
                self.taken_weights[i]=True
                j = j-self.weights[i]
                i = i-1



    def printDPtable(self):
        for i in self.DPtable:
            print(i)


if __name__=='__main__':
    myweights = [1,3,4,5]
    myvalues = [1,4,5,7]
    kp = knapSnackDP(weights= myweights,values=myvalues,max_weight=7)
    print("our Items: ")
    kp.print_table()
    kp.createDPtable()
    kp.printDPtable()
    kp.retrieveWeights()
    print(kp.taken_weights)
    print(kp.weights)
