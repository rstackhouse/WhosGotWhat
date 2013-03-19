class Skill(object):
    def __init__(self, skill_name, skill_description):
        self.name = skill_name
        self.description = skill_description
        self.associated_skills = []
