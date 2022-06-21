name = input("Name? ")

Siblings = ["gary", "glen", "gina"]

#method on input
def sib(person):
    if person.lower() in Siblings:
        return person + " is a sibling!"
    else:
        return person + " is not a sibling..."

print(sib(name))