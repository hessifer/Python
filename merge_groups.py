class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    def get_members(self):
        return sorted(self.members)

    def merge(self, group):
        return Group("New_Group", self.members + group.members)

def main():
    g1 = Group("A-Team", ["Tim", "Clement"])
    g2 = Group("B-Team", ["Antoine"])
    g3 = g1.merge(g2)

    print(g3.get_members())


if __name__ == "__main__":
    main()
