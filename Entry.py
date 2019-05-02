class Entry:
    def __init__(self, fields):
        self.fields = fields
    def addField(self, field):
        self.fields.append(field)

class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value