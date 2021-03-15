class Message:
    def __init__(self, sender=None, content=None, action=None, action_and_subject=None, action_type=None,
                 thoughts=None, content_type="CHAT"):
        self.sender = sender
        self.content = content
        self.action = action
        self.action_and_subject = action_and_subject
        self.action_type = action_type
        self.thoughts = thoughts
        self.content_type = content_type

    def __str__(self):
        return f"{{ \n" \
               f"\t\"sender\" : \"{self.sender}\",\n" \
               f"\t\"content\" : \"{self.content}\",\n" \
               f"\t\"action\" : \"{self.action}\",\n" \
               f"\t\"action_and_subject\" : \"{self.action_and_subject}\",\n" \
               f"\t\"action_type\" : \"{self.action_type}\",\n" \
               f"\t\"thoughts\" : \"{self.thoughts}\",\n" \
               f"\t\"content_type\" : \"{self.content_type}\"" \
               f"}}"
