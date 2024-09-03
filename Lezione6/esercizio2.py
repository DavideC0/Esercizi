class Student:
    def __init__(self, name, study_program) -> None:
        self.name = name
        self.study_program = study_program
        self.age = None
        self.gender = None

    def __str__(self) -> str:
        if self.age and self.gender:
            return f"nome = {self.name}, programma di studio = {self.study_program}, età = {self.age}, genere = {self.gender}"
        else:
            if self.age:
                return f"nome = {self.name}, programma di studio = {self.study_program}, età = {self.age}"
            elif self.gender:
                return f"nome = {self.name}, programma di studio = {self.study_program}, genere = {self.gender}"
            else:
                f"nome = {self.name}, programma di studio = {self.study_program}"

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender
            
davide = Student('Davide C.', "python")
walter = Student('Walter N. A.', 'barese')
elena = Student('Elena M.', 'vivere')
bardh = Student("Bardh", "non lo vuoi sapere")
print(davide)
print(walter)
print(elena)
print(bardh)
davide.set_age(19)
davide.set_gender("elicottero")
walter.set_age(38)
elena.set_gender("non binario")
print(davide)
print(walter)
print(elena)
print(bardh)