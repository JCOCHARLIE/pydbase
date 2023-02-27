from main import People

try:
    people_name = input("Enter your name \n")
    people_number = input("Enter your phone number \n")
    people_email = input("Enter yor email \n")
    people_county = input("Enter your county \n")
    people_gender = input("Enter your gender \n")
    people_religion = input("Enter your religion \n")
    people_password = input("Enter your password \n")

    People.create(people_name=people_name, phone=people_number, people_email=people_email, county=people_county, gender=people_gender, religion=people_religion, people_password=people_password)
    print("Registered successfully")

except:
    print("Registration failed. Use a different  email")