class Message:
    def __init__(self, sender=None, content=None, action=None, action_and_subject=None, action_type=None,
                 thoughts=None, message_type="CHAT"):
        self.sender = sender
        self.content = content
        self.action = action
        self.action_and_subject = action_and_subject
        self.action_type = action_type
        self.thoughts = thoughts
        self.message_type = message_type

    def __str__(self):
        return f"{{ \n" \
               f"\"sender\" : \"{self.sender}\",\n" \
               f"\"content\" : \"{self.content}\",\n" \
               f"\"action\" : \"{self.action}\",\n" \
               f"\"action_and_subject\" : \"{self.action_and_subject}\",\n" \
               f"\"action_type\" : \"{self.action_type}\",\n" \
               f"\"thoughts\" : \"{self.thoughts}\",\n" \
               f"}}"
