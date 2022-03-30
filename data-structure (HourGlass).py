arr = [ [1, 1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0], 
        [1, 1, 1, 0, 0, 0], 
        [0, 0, 2, 4, 4, 0], 
        [0, 0, 0, 2, 0, 0], 
        [0, 0, 1, 2, 4, 0]]

arr2 =[ [1, 1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 9, 2, -4, -4, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, -1, -2, -4, 0]
]

class HourGlass:
    def __init__(self, arr):
        self.arr = arr

    def hourglassSum(self):
        HG = []
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if (j+3) <= len(self.arr[0]) and (i+2) < len(self.arr):
                    topHG = self.arr[i][j:j+3]
                    centerHG = self.arr[i+1][j+1]
                    bottomHG = self.arr[i+2][j:j+3]
                HG.append(sum([sum(topHG), centerHG, sum(bottomHG)]))
            else:
                continue
            break
        return max(HG)

HG1 = HourGlass(arr2)

print(HG1.hourglassSum())