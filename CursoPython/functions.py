def describe_pet(horse):  
    """Muestra información sobre una mascota."""  
    return f"I have a {horse}."
    # print(f"My {horse}'s name is {pet_name.title()}.")


def build_person(first_name, last_name, age=None):  
    """Devuelve un nombre completo, con un formato adecuado."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix') 
print(musician)


# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False
#         mapping = {')': '(', ']': '[', '}': '{'}
#         stack = []
#         for char in s:
#             if char in mapping.values():
#                 stack.append(char)
#             elif char in mapping.keys():
