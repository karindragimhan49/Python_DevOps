# Create a dictionary to store server configuration
server_config = {
    "hostname": "web-server-01",    # Server name
    "ip_address": "192.168.1.10",   # Server IP address
    "ram_gb": 16,                   # Amount of RAM in GB
    "is_virtual": True              # Is it a virtual server? True or False
}

# Print the full server configuration
print("Server configuration:", server_config)



# Get and print value of 'ram_gb' key
print("ram_gb:", server_config["ram_gb"])

# Get and print value of 'is_virtual' key
print1 = print("is_virtual:", server_config["is_virtual"])

vm = server_config["is_virtual"]
print("vm is :", vm)


# Store the IP address in a variable and print it
ip = server_config["ip_address"]
print("Server IP:", ip)




# Add a new key-value pair to the dictionary for operating system
server_config["os"] = "Ubuntu 20.04"

# Print the updated dictionary after adding the new key
print("Updated configuration:", server_config)
