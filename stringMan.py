import time
import threading
from models.message import Message
import json
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

json_msg = json.loads(str(msg))
msg_fromJSON = Message(json_msg["sender"], json_msg["content"], json_msg["action"], json_msg["action_type"])
print(2, msg_fromJSON.__str__())

