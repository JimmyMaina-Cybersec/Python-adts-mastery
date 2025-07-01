number_of_people = int(input("How many people are we working with: "))

# Create a dictionary taking in first_name, last_name, age and city
# number of key-value pairs equals len(people)
person_info = {}
people = {}
for i in range(number_of_people):
    first_name = input(f"\nEnter first name of person {i + 1}: ").title()
    print(f"\tYou entered: '{first_name}' as the first name of person {i + 1}")
    last_name = input("Enter last name: ").title()
    print(f"\tYou entered: '{last_name}' as the last name of person {i + 1}")
    age = int(input("Enter their age: "))
    print(f"\tYou entered: '{age}' as the age of person {i + 1}")
    city = input("Enter city: ").title()
    print(f"\tYou entered: '{city}' as the city of person {i + 1}")

    person_info = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "city": city,
    }

    people["Person"] = person_info

print("\nHere are the people and their information:")
print(people)
