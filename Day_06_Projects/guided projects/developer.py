from employee import Employee

class Developer(Employee):
    def __init__(self, name, id_number, language):
        super().__init__(name, id_number)
        self.language = language