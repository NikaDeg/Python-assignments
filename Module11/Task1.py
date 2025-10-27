class Publication:

    def __init__(self, name):
        self.name = name


class Book(Publication):

    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"Book: {self.name} by {self.author}, {self.page_count} pages")


class Magazine(Publication):

    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"Magazine: {self.name}, chief editor: {self.chief_editor}")