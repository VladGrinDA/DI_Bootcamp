import math


class Pagination:
    def __init__(self, items, pageSize=10) -> None:
        self.items = items
        self.pageSize = int(pageSize)
        self.currentPage = 1
        self.totalPages = math.ceil(len(self.items) / self.pageSize)
    
    def getVisibleItems(self):
        return self.items[(self.currentPage - 1) * self.pageSize: (self.currentPage) * self.pageSize]
    
    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self
    
    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self
    
    def goToPage(self, pageNum):
        self.currentPage = min(self.totalPages, max(1, int(pageNum)))
        return self
    

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# alphabetList = list("abc")

p = Pagination(alphabetList, 4)

print(p.getVisibleItems())
# ["a", "b", "c", "d"]

p.nextPage()
print(p.getVisibleItems())
# ["e", "f", "g", "h"]

p.lastPage()
print(p.getVisibleItems())
# ["y", "z"]

p.goToPage(2)
print(p.getVisibleItems())
p.nextPage().nextPage()
print(p.getVisibleItems())

p.goToPage(20)
print(p.getVisibleItems())
p.goToPage(0)
print(p.getVisibleItems())