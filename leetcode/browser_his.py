class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.current_page = self.homepage

    def visit(self, url: str) -> None:
        new_page = Node(url)
        while self.current_page.next:
            self.current_page = self.current_page.next
        self.current_page.next = new_page
        new_page.prev = self.current_page
        self.current_page = new_page

    def back(self, steps: int) -> str:
        i = 1
        if self.current_page.prev is None:
            return self.current_page.val
        while self.current_page.prev:
            self.current_page = self.current_page.prev
            if i == steps:
                return self.current_page.val
            i+=1
        return self.current_page.val
    def forward(self, steps: int) -> str:
        i = 1
        if self.current_page.next is None:
            return self.current_page.val
        while self.current_page.next:
            self.current_page = self.current_page.next
            if i == steps:
                return self.current_page.val
            i += 1
        return self.current_page.val

obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
obj.back(1)
obj.back(1)
obj.forward(1)
obj.visit("linkedin.com")
obj.forward(2)
obj.back(2)
print(obj.back(7))
