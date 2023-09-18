#old version
letter = "Hey my name is {} and I am from {}"
country="India"
name = "Abhishek"
print(letter.format(country, name))

#new version
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")