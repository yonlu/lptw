from sys import argv

script, user_name, title = argv
prompt = 'You: '

print(f"Hi {title} {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questiosn.")
print(f"Do you like me {title} {user_name}?")
likes = input(prompt)

print(f"Where do you live {title} {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
