import os

if not os.path.exists("Photos"):
    os.mkdir("Photos")


if not os.path.isfile('data/bank.json'):
    #open("data/bank.json", "w").close()
    with open('data/bank.json',"w") as f:
        f.write("{\n}")