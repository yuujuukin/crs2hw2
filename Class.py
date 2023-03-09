class Candidate:
    def __init__(self, id, name, position, skills, picture, age, gender):
        self.id = id
        self.name = name
        self.position = position
        self.skills = skills
        self.picture = picture
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f'{self.name} \n {self.position} \n {self.skills}'
