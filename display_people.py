from main import People
mypeople = People.select()
for persons in mypeople:
    print(persons.people_name, persons.phone, persons.people_email, persons.county, persons.gender, persons.religion, persons.people_password)