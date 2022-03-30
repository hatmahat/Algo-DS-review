class CountQueries:
    def __init__(self, filename):
        self.f = open(filename, "r")
        self.arr = [string.strip() for string in self.f.readlines()]
        self.dataset = {
            "n":int(self.arr[0]),
            "strings":self.arr[1:int(self.arr[0])+1],
            "q":int(self.arr[int(self.arr[0])+1]),
            "queries":self.arr[int(self.arr[0])+2:]
        }

    def countQueries(self):
        out = []
        for q in self.dataset["queries"]:
            count = 0
            for s in self.dataset["strings"]:
                if q == s:
                    count += 1
            out.append(count)
        return out

CQ1 = CountQueries("sample.txt")
print(CQ1.countQueries())