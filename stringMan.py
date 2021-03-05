import time
import threading
from models.message import Message
import json
import pickle
"""
def thread_func(nmbr):
    print(f"thread {nmbr}:  starts")
    time.sleep(2)
    print(f"thread {nmbr}:  done")


thList = list()
for i in range(0, 4):
    th = threading.Thread(target=thread_func, args=(i,))
    thList.append(th)
    th.start()

for j, th in enumerate(thList):
    th.join()
"""

msg = Message("Nima", "Hello", "none", "____")
print(1, msg)
ser_msg = pickle.dumps(msg)
print(ser_msg)
dser_msg = pickle.loads(ser_msg)
print(dser_msg)
msg1 = {
    "sender": dser_msg.sender,
    "content": dser_msg.content,
    "action": dser_msg.action,
    "action_type": dser_msg.action_type
}
print(3, msg1)

print("type of dser_msg: ", type(dser_msg))
# msg1 = Message(dser_msg["sender"], dser_msg["content"], dser_msg["action"], dser_msg["action_type"])
# print(2, msg1)

json_msg = json.loads(str(msg))
msg_fromJSON = Message(json_msg["sender"], json_msg["content"], json_msg["action"], json_msg["action_type"])
print(4, msg_fromJSON.__str__())

