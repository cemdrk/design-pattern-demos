
class ClassDef(object):
    indent_size = 4

    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        _indent = self.indent_size * ' '
        output = 'class {}\n{{'.format(self.name)

        for field in self.fields:
            output += '\n{}{} {};'.format(_indent, field.get('type'), field.get('name'))

        output += '\n};'
        return output


class CodeGenerator(object):
    def __init__(self, cls_name):
        self.root = ClassDef(cls_name)

    def add_field(self, name, _type):
        self.root.fields.append(dict(
            name=name,
            type=_type
        ))
        return self

    def __str__(self):
        return self.root.__str__()


if __name__ == '__main__':
    generator = CodeGenerator('Person').add_field('name', 'string').add_field('age', 'int')
    print generator
