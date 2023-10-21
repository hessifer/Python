class FileSystem:
    """
    
    
    """
    def __init__(self):
        # constructor sets Directory root to "/"
        self.root = Directory("/")

    def create_directory(self, path):
        # actually we don't validate the entire path, just that
        # it starts with '/'
        FileSystem._validate_path(path)
        
        # get the nodes (directory) names
        directory_nodes = path[1:].split("/")
        
        # accounting for a trailing "/"
        directory_nodes_not_empty = [d for d in directory_nodes if len(d) > 0]
        
        # /parent_dir/child_dir/
        # splict nodes by '/' as separator
        nodes_in_path = path[1:].split('/')
        node_to_create = nodes_in_path[-1]
        
        dir = Directory(node_to_create)
        dir.add_node(node_to_create)
        

    def create_file(self, path, contents):
        # Write your code here.
        pass

    def read_file(self, path):
        # Write your code here.
        pass

    def delete_directory_or_file(self, path):
        # Write your code here.
        pass

    def size(self):
        # Write your code here.
        pass

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")


    def _find_bottom_node(self, node_names):
        # Write your code here.
        pass


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)


if __name__ == "__main__":
    fs = FileSystem()
    fs.create_directory("/dir1")
    print(fs)
