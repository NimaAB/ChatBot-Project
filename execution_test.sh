#! /bin/bash
python3 server.py -p 6000 &
python3 client.py -bn Alice &
python3 client.py -bn Bob &
python3 client.py -bn Dora &
python3 client.py -bn Chuck &


