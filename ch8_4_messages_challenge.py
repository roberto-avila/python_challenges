#-----Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

messages = ['hi', 'lol', 'lmao']

def show_messages(messages):
    """Display the text messages in the list"""
    for message in messages:
        print(f"{message}")

show_messages(messages)

print('\n')

#-----Start with the previous code. Write a function called send_messages() that prints each text message and moves each message to a new list 
# called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

messages = ['hi', 'lol', 'lmao']
sent_messages = []

def show_messages(messages):
    """Display the text messages in the list"""
    print("Showing all pending messages:")
    for message in messages:
        print(f"{message}")

def send_messages(messages, sent_messages):
    """Display messages being sent and move them to the sent_messages list"""
    print("Sending the following messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

show_messages(messages)
send_messages(messages, sent_messages)

print("Here are the resulting lists:")
print(messages)
print(sent_messages)

print('\n')

#-----Start with the previous code. Call the function send_messages() with a copy of the list of messages. After calling the function,
#  print both of your lists to show that the original list has retained its messages.

messages = ['hi', 'lol', 'lmao']
sent_messages = []

send_messages(messages[:], sent_messages)

print("Here are the resulting lists:")
print(messages)
print(sent_messages)