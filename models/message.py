class Message:
    def __init__(self, sender=None, content=None, action=None, action_type=None):
        self.sender = sender
        self.content = content
        self.action = action
        self.action_type = action_type

    def __str__(self):
        return f"{{ \n" \
               f"\"sender\" : \"{self.sender}\",\n" \
               f"\"content\" : \"{self.content}\",\n" \
               f"\"action\" : \"{self.action}\",\n" \
               f"\"action_type\" : \"{self.action_type}\"\n" \
               f"}}"
