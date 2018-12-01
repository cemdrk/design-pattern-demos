class HTMLElements(object):

    indent_size = 2

    def __init__(self, name=None, text=None):
        self.name = name
        self.text = text
        self.elements = []

    def __str__(self, indent=0):
        _indent = self.indent_size * indent * ' '
        output = _indent + '<{}>\n'.format(self.name)

        if self.text:
            output += _indent + self.indent_size * ' '
            output += self.text
            output += '\n'

        for elem in self.elements:
            output += elem.__str__(indent+1)

        output += _indent + '</{}>\n'.format(self.name)
        return output


class HTMLBuilder(object):
    def __init__(self, name):
        self.root = HTMLElements(name)

    def add_child(self, name, text=None):
        elem = HTMLElements(name, text)
        self.root.elements.append(elem)

    def __str__(self):
        return self.root.__str__()


if __name__ == '__main__':
    builder = HTMLBuilder('ul')
    builder.add_child('li', 'Apple')
    builder.add_child('li', 'Banana')

    print builder
