class MyHashSet:
    
    def __init__(self):
        self.values = []
    
    def add(self, key):
        if key not in self.values:
            self.values.append(key)

    def remove(self, key):
        if key in self.values:
            self.values.remove(key)
    
    def contains(self, key):
        if key in self.values:
            return True
