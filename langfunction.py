#Ask the user for their language
lang=input("What is your language: ")

#Ask the user for their name
name=input("Please enter your first name: ")

#Define the different language options
def greet(lang):
    if lang == 'spanish':
        return "Hola"
    elif lang == 'french':
        return "Bonjour"
    else:
        return "Hello"

#Greet the user in their language and print their name
print(lang, name)
