'''
One of our older Mars Rovers has nearly completed its tour of duty and is awaiting instructions for one last mission to explore the Martian surface. 
The survey team has picked a route and has entrusted you with the job of transmitting the final set of instructions to the rover. 
This route is simply a sequence of moves in the cardinal directions: North, South, East, and West.
These instructions can be sent using a string of corresponding characters: N, S, E, and W. However, receiving the signal drains the rover’s power supply,
which is already dangerously low. Fortunately, the rover’s creators built in the ability for you to optionally define a single 
“macro” that can be used if the route has a lot of repetition. More concretely, to send a message with a macro, two strings are sent. 
The first is over the characters {N,S,E,W,M} and the second is over {N,S,E,W}. The first string represents a sequence of moves and calls to a macro (M), 
while the second string determines what the macro expands out to. For example:
'''

#inputString = input()

inputString = "WNESDQWEENEENEEN"
length = len(inputString)

shortest = length

def updateShortest(size, chunkCount):
    global shortest
    candiate = length + size - (size - 1) * chunkCount
    if candiate < shortest:
        shortest = candiate


def getPossibleChunks(chunk_length):
    chunks = set()
    i = 0
    while i + chunk_length < length:
        chunk = inputString[i:i+chunk_length]
        chunks.add(chunk)
        i += 1
    return chunks

for chunk_size in range(2, length//2 + 1):
    chunks = getPossibleChunks(chunk_size)
    for chunk in chunks:
        chunkCount = 0
        i = 0
        while i + chunk_size <= length:
            current_chunk = inputString[i:i+chunk_size]
            if current_chunk == chunk:
                chunkCount += 1
                i+=chunk_size
            else:
                i+= 1

        updateShortest(chunk_size, chunkCount)

print(shortest)



