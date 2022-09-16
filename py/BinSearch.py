# Binary Search File
#Kirk Martin
#CSCI 77800 Fall2022
# September 14, 2022
#

class BinSearch :
    # *
    #     int binSearch(int[],int) -- searches an array of ints for target int
    #     precondition:  input array is sorted in ascending order
    #     postcondition: returns index of target, or returns -1 if target not found
    @staticmethod
    def  binSearch( a,  target) :
        
        #allows use of multiple arrays multiple times
        return BinSearch.binSearchRec(a, target, 0, len(a) - 1)
    @staticmethod
    def  binSearchRec( a,  target,  loPos,  hiPos) :
        tPos = -1
        # init return var to flag/signal value
        mPos = int((loPos + hiPos) / 2)
        # init tracker var for middle position
        # exit case. If lo & hi have crossed, target not present
        if (loPos > hiPos) :
            print("Not here")
            return tPos
        print("a[mPos] is %d and target is %d\n" % (a[mPos],target),end ="",sep ="")
        # target found
        if (a[mPos] == target) :
            tPos = mPos
            print("Found")
        elif(a[mPos] > target) :
            print("Checking lower")
            tPos = BinSearch.binSearchRec(a, target, loPos, mPos - 1)
            print("Done checking lower")
        elif(a[mPos] < target) :
            print("Checking upper")
            tPos = BinSearch.binSearchRec(a, target, mPos + 1, hiPos)
            print("Done checking upper")
        return tPos
    # end binSearchRec
    # tell whether an array is sorted in ascending order
    @staticmethod
    def  isSorted( arr) :
        retBoo = True
        # init to true, assume array is sorted
        # Q: Why would a FOREACH loop not suffice here?
        i = 0
        while (i < len(arr) - 1) :
            if ((arr[i] > arr[i + 1])) :
                return False
            i += 1
        return retBoo
    # utility/helper fxn to display contents of an array of Objects
    @staticmethod
    def printArray( arr) :
        output = "[ "
        for c in arr :
            output += str(c) + ", "
        output = output[0:len(output) - 2] + " ]"
        print(output)
    # main method for testing
    @staticmethod
    def main( args) :
        # move the bar down to uncover tests in succession...
        print("\nNow testing binSearch on int array...")
        # This Declares and initializes array of ints
        iArr = [2, 4, 6, 8, 6, 42]
        BinSearch.printArray(iArr)
        print("iArr1 sorted? -- " + str(BinSearch.isSorted(iArr)))
        iArr2 = [2, 4, 6, 8, 13, 42]
        BinSearch.printArray(iArr2)
        print("iArr2 sorted? -- " + str(BinSearch.isSorted(iArr2)))
        iArr3 = [0] * (10000)
        i = 0
        while (i < len(iArr3)) :
            iArr3[i] = i * 2
            i += 1
        # printArray( iArr3 );
        print("iArr3 sorted? -- " + str(BinSearch.isSorted(iArr3)))
        # search for 6 in array
        print(BinSearch.binSearch(iArr2, 2))
        print(BinSearch.binSearch(iArr2, 4))
        print(BinSearch.binSearch(iArr2, 6))
        print(BinSearch.binSearch(iArr2, 8))
        print(BinSearch.binSearch(iArr2, 13))
        print(BinSearch.binSearch(iArr2, 42))
        # search for 43 in array
        print(BinSearch.binSearch(iArr2, 43))
        print("now testing binSearch on iArr3...")
        print(BinSearch.binSearch(iArr3, 4))
        print(BinSearch.binSearch(iArr3, 8))
        print(BinSearch.binSearch(iArr3, 5))
        # search for 43 in array
        print(BinSearch.binSearch(iArr3, 43))
    

if __name__=="__main__":
   BinSearch.main([])
