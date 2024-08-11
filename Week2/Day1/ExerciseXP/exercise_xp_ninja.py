# Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.

# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.

# Add a method called show_call_history. This method should print the call_history.

# Add another attribute called messages to your __init__() method which value is an empty list.

# Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content

# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

class Phone:
    def __init__(self, phone_number, call_history=None, message_history=None) -> None:
        self.phone_number = phone_number
        self.call_history = call_history if call_history is not None else []
        self.message_history = message_history if message_history is not None else []

    def __repr__(self) -> str:
        return str(self.phone_number)

    def call(self, other):
        call_info = f"{self} called {other}"
        self.call_history.append(call_info)
        other.call_history.append(call_info)

    def show_call_history(self):
        print('Call history:')   
        print(*self.call_history, sep='\n')

    def send_message(self, other, message):
        message = {
            'to': other.phone_number,
            'from': self.phone_number,
            'message': message
        }
        self.message_history.append(message)
        other.message_history.append(message)
    
    def get_outgoing_messages(self):
        return [message for message in self.message_history if message['from'] == self.phone_number]
    
    def get_incoming_messages(self):
        return [message for message in self.message_history if message['to'] == self.phone_number]
    
    def get_messages_from(self, other):
        return [message for message in self.message_history if message['from'] == other.phone_number]
    
    
    @staticmethod
    def show_messages_list(messages):
        for i, message in enumerate(messages):
            print(f"{i}. {message['from']} -> {message['to']}: {message['message']}")

    def show_outgoing_messages(self):
        print('Outgoing messages:')
        self.show_messages_list(self.get_outgoing_messages())

    def show_incoming_messages(self):
        print('Incoming messages:')
        self.show_messages_list(self.get_incoming_messages())

    def show_messages_from(self, other):
        print(f"Messages from {other}:")
        self.show_messages_list(self.get_messages_from(other))

    
if __name__ == '__main__':
    phone1 = Phone("0123456789")
    phone2 = Phone("9876543210")
    phone3 = Phone("5555555555")

    phone1.call(phone2)
    phone2.call(phone1)
    phone1.send_message(phone2, "Hello from phone 1")
    phone1.send_message(phone2, "How are you")
    phone2.send_message(phone1, "Hello from phone 2")
    phone3.send_message(phone1, "Hello from phone 3")

    print('\nCall history:')
    phone1.show_call_history()

    phone1.show_outgoing_messages()

    phone1.show_incoming_messages()

    phone1.show_messages_from(phone2)
        
