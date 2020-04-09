import json
import requests

class User:
    def __init__(self, name, tag):
        self.name = name
        self.tag = tag
        self.chains = {}

n = User("n", "n")
r = User("r", "r")    
class Message:
    def __init__(self, sender, msg_text, prev = None): #recipient is implied thru MessageChain
        self.text = msg_text
        self.sender = sender
        self.prev = prev 
        if not prev:
            self.msg_id = 0
        else:
            self.msg_id = prev.msg_id + 1 # self explanatory

class MessageChain:
    def __init__(self, sender, recipient, msg_text):
        self.latest = Message(sender, msg_text)
        self.sender = sender
        self.recipient = recipient
        self.len = 0
        # maybe keep a list of pointers to messages at intervals of 5? lookup would be O(n),
        # but very rarely do people look back further than ~100 messages
        
    def get_messages(self, length = None , msg_id = None): # only one of these
        msg_node = self.latest
        if not length and not msg_id:
            return msg_node
        if (length and length > self.len) or (msg_id and msg_id > self.len):
            return None
        if msg_id:
            while msg_node.msg_id != msg_id:
                if not msg_node or msg_node.msg_id < msg_id:
                    return None # message node possibly deleted
                msg_node = msg_node.prev
            return msg_node    
        else:
            messages = []
            while length > 0:
                messages.append(msg_node)
                msg_node = msg_node.prev
                length -= 1
            return messages

    def add_message(self, sender, msg_text):
        m = Message(sender, msg_text, self.latest) # message will point to prev
        self.len += 1
        self.latest = m
    
    def delete_message(self, msg_id):
        nodeprev = self.latest
        msg_node = nodeprev.prev
        if self.latest.msg_id == msg_id:
            tmp = self.latest.prev
            self.latest.prev = None
            self.latest = tmp
        else:
            while msg_node.msg_id != msg_id:
                nodeprev = msg_node
                msg_node = msg_node.prev
        self.len -= 1
        nodeprev.prev = msg_node.prev
        msg_node.prev = None

mc = MessageChain(n, r, "fuck you")
mc.add_message(r, "no u")
mc.add_message(n, "orijfiferws")
mc.add_message(r, "what the hell")
mc.add_message(n, "REEEE")
mc.add_message(r, "bruh")
print(mc.get_messages(length=4))
print(mc.get_messages())
print(mc.get_messages(msg_id=2))
mc.delete_message(2)
print(mc.get_messages(msg_id = 2))
print(mc.get_messages(length=3))