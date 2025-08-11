# Lesson 4: if/elif/else


#/////////////////////////////////////////////////////////////////////////////////
#f-string (Formatted String Literals)

server_name = "db-server-01"
ip_address = "192.168.1.50"

# without f-string
print("Connecting to server: " + server_name + " with IP: " + ip_address)

# with f-string
print(f"Connecting to server: {server_name} with IP: {ip_address}")



#/////////////////////////////////////////////////////////////////////////////////
#exercise 1

service_status = "running"

if service_status == "running":
    print(f" Status: The service is {service_status}")

elif service_status == "stopped":
    print(f" CRITICAL: The service is stopped!")
else:
    print(f" WARNING: The service status is unknown. Current status: {service_status}")


#/////////////////////////////////////////////////////////////////////////////////
#exercise 2

server_config = {
    "name": "prod-web-01",
    "cpu_cores": 10,
    "ram_gb": 20,
    "environment": "production"
}

ram_gb = server_config["ram_gb"] 
cpu = server_config["cpu_cores"]
environment = server_config["environment"]
name = server_config["name"]

if ram_gb < 16 and cpu < 8:
   print(f"CONFIG ERROR for {name}: Not enough resources for production. RAM requires 16GB (has {ram_gb}) and CPU requires 8 cores (has {cpu}).")

elif environment != "production":
   print(f" CONFIG WARNING for {name}: Environment is set to '{environment}', not 'production'.")

else:
   print(f" SUCCESS: Configuration for server {name} is valid for production.")