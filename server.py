import socket  # I bet you dont know what does that

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Defines the server with the protocol thing
my_ip = socket.gethostbyname(socket.gethostname())  # Gets IP of the computer
print(my_ip)  # Prints the IP (Dont have to do this)
serverRunning = True  # Just a variable to say serverRunning is True
server.bind(("10.1.129.12", 5636))  # AF_INET uses IP Addresses and SOCK_STREAM needs a port, so bind computer's ip add-
# ress and a port which is above 1024
server.listen(2)  # The server listen up for 2 clients

while serverRunning is True:  # loop
    client, address = server.accept()  # When clients attempt to join, they it takes their info as client, address
    print("A client from the IP {} has joined".format(address)) #  Just some info


