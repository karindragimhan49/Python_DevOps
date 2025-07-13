#Variables and Data Types

# 1 - String
server_name = "web-server-01"
status_message= "Server is running correctly"


# 2- Integer
cpu_cores = 8
active_connection = 150

# 3 - Float
load_average= 2.5
disk_usage = 75.5

# 4 - Boolean
is_server_is_running= True
is_backuped_failed= False

# 5 - printing variables
print("Server Name:", server_name)
print("Server is running correctly",status_message )

## type() when using type funtion we can see varible ,data type

print("Server Name :", type(server_name))
print("Status Message:", type(status_message))
print("CPU Cores:", type(cpu_cores))
print("Active Connections:", type(active_connection))
print("Load Average:", type(load_average))
print("Disk Usage:", type(disk_usage))
print("Is Server Running:", type(is_server_is_running))
print("Is Backup Failed:", type(is_backuped_failed))


