# Chatbot Project
The project is a portfolio assignment in Data nettwork and Cloud Computing topic at OsloMet university.

## Breaf Explanation:
The goal is to creat a chatroom, where participants are bots. The bots will connect to a server on the same address, and they will receive an intial message
that includes an action(verb). Then, based on the bot's interest in the action they will send a message back to the chat room. The server then will broadcat it to all the clients (bots).

## Some Simplification That I have taken here: 
- The server will wait for all four bots to join, then start broadcating messages. 
- Each client(bot) will wait for the others to join, then strating to write.

## Room for future improvments:
- Making a web server for the project. 
- Making it a chating app between real participants.

## Running the current version:
*python3 is required for running the code.*
cd to the project file
```bash
py server.py --help
py client.py --help
```

### Picture:
Image of Alex Knight from Pexels
