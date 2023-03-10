import os

def main():

    os.system('cls')

    print('People')
    print('------')
    
    # Person1
    Person1 = Person('Adam')
    Person1.show_person()

    # Person2
    Person2 = Person('Andreas')
    Person2.show_person()

    # Person3
    Person3 = Person('Barbora')
    Person3.show_person()

    # Person4 - ADMIN
    Person4 = Admin('Marcus')
    Person4.show_person()

    # Person4 - SUPER ADMIN
    Person5 = SuperAdmin('Antony')
    Person5.show_person()

    print()
    print("-------")
    print("MEETING")
    print("-------")
    meeting_members = [Person("Raul"), Admin("Susan"), SuperAdmin("Theresa")]
    for m in meeting_members:
        m.show_person()



# parent
class Person:
    
    new_id = 1

    def __init__(self, name):
        self.id = Person.new_id
        Person.new_id += 1
        self.name = name
 
    # show name and id of person
    def show_person(self):
        print("Name:", self.name, "\t id:", self.id)


class User:
  def __init__(self, username, role="Visitor"):
    self.username = username
    self.role = role


# child
class Admin(Person, User):

    def __init__(self, name):
        super().__init__(name)
        User.__init__(self, self.id, "ADMIN")

    # overrided method
    def show_person(self):
        # using super() we cas access the behavior of parent method
        super().show_person()
        print("Name:", self.name, "\t", self.role)


#  multiple inheritance
class SuperAdmin(Admin):
    
    def show_person(self):
        print("SUPER ADMIN")
        print("-----------")
        return super().show_person()



if __name__ == '__main__':
    main()