class Person:
    def __init__(self, name=None, address=None, connection=None):
        self.name = name
        self.address = address
        self.connection = connection

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"{{ " \
               f"\"sender\" : {self.name}" \
               f"\"content\" : {self.address}" \
               f"\"action\" : {self.connection}" \
               f"}}"
