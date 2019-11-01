import wfuzz
import json
import socket
import pickle

# TODO: Needs moving to command line
input_string = "-u http://testphp.vulnweb.com/listproducts.php?cat=FUZZ -w ./test_wl.txt --hl 97 -s 0.7"


nodes = ["51.89.231.21:65432", "51.89.230.190:65432", "51.91.137.190:65432", "51.91.142.97:65432"]

def chunker_list(seq, size):
    return (seq[i::size] for i in range(size))

s = wfuzz.get_session(input_string)
wl = json.loads(s.export_json())["wfuzz_recipe"]["payloads"][0][1]["default"]

print("Reading wordlist: " + wl + "...")
with open(wl, 'r') as f:
    lines = f.read().splitlines()

print("Splitting up...")
wl_parts = list(chunker_list(lines, len(nodes)))

print("Sending to clients...")
nodeSockets = {}
nodeNum = 0
for node in nodes:
    try:
        nodeInfo = node.split(":")
        nodeSockets[node] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        nodeSockets[node].connect((nodeInfo[0], int(nodeInfo[1])))
        nodeSockets[node].sendall((input_string + "\n").encode("utf-8"))
        nodeSockets[node].sendall(pickle.dumps(wl_parts[nodeNum]))
        
        nodeNum = nodeNum + 1
    except:
        print("Error connecting to " + node)
        pass

if (nodeNum < 1):
    print("Error connecting to all nodes, exiting!")
    exit()

print("Waiting for responses")
while len(nodeSockets) >= 1:
    for nodeIP in nodeSockets:
        conn = nodeSockets[nodeIP]

        curLine = ""
        while True:
            data = conn.recv(1)
            if not data:
                break
            
            if (data == b'\n'):
                if (curLine == "$$"):
                    del(nodeSockets[nodeIP])
                    break
                print(curLine)
                curLine = ""
                break
            else:
                curLine += data.decode("utf-8")



print("Done")