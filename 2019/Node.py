class Planet():
    def __init__(self, name: str, parent: 'Planet' = None, child: 'Planet' = None):
        self.name = name
        self.parent = parent
        self.children = set()
        if child is not None:
            self.children.add(child)
        
    def __eq__(self, n: object) -> bool:
        return self.name == n.name

    def __repr__(self):
        return str(self.name)

    def __hash__(self):
        return hash(self.name)

    def __iter__(self):
        for child in self.children:
            yield child
