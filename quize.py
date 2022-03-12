#Creating the professor class with phone_number,name,lastname,teaching_hours,tutoring_fees_per_hour attributes
class professor :
    def __init__(self,phone_number,name,lastname,teaching_hours,tutoring_fees_per_hour ) :
        self.phone_number = phone_number
        self.name = name
        self.lastname = lastname
        self.teaching_hours = teaching_hours
        self.tutoring_fees_per_hour = tutoring_fees_per_hour


#Creating a function that calculates the salary
def salary_calculator (person):
    return person.teaching_hours*person.tutoring_fees_per_hour


#Creating a function that shows professors name,lastname and salary
def salary(list):
    print("Name","Salary",sep="\t\t\t")
    for person in list:
        print((person.name+" "+person.lastname),(salary_calculator(person)),sep="\t\t")
#Creating a function that shows professors name with the same salary and at the end show sorted salaries
def sorted_salary(list):
    
    for i in range(len(list)):
        same_salary = []
        for j in range(i+1,len(list)):
            if salary_calculator(list[i]) == salary_calculator(list[j]):
                same_salary.append((list[i].name+" "+list[i].lastname))
                same_salary.append((list[j].name+" "+list[j].lastname))
        same_salary = set(same_salary)
        if len(same_salary) != 0 :
            print("Professors with same salary : ",same_salary)
    print("==== Sorted salaries ====")
    list.sort(key = lambda x:salary_calculator(x),reverse =True)
    for i in range(len(list)):
        print(i+1,".",(list[i].name+" "+list[i].lastname),":\t",salary_calculator(list[i]))

#constructing the professors list and object
professor_list = []
professor_list.append(professor(555689,"Ali","Kazemi",35,3.5))
professor_list.append(professor(491218,"Reza","Amiri",35,3.5))
professor_list.append(professor(316848,"Mina","Hafezi",10,4.5))
professor_list.append(professor(168631,"Kamran","Abdi",5,1.5))
professor_list.append(professor(165846,"Sahra","Shirzad",41,4))
professor_list.append(professor(156464,"Hamed","Farsi",10,4.5))

print("==== Professor's name , last name and salary ====")
#showing the list of professors salries
salary(professor_list)

#showing the sorted and same salaries
print("==== If there is same salries ====")
sorted_salary(professor_list)
            