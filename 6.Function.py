#//////////////////////////////////////////////////////


#   1. def keyword     2. function name    3. parameters (optional)
def                 check_service_status(service_name, port_number):
    
    # 4. function body (the code that does the work)
    print(f"Checking status for {service_name} on port {port_number}...")
    # (Imagine code here to actually check the service)
    is_running = True # Let's pretend it's running
    
    if is_running:
        return "ACTIVE" # 5. return value (optional)
    else:
        return "INACTIVE"
    
    


    
    
    
    
    
    
    
    
    
#////////////////////////////////////////////////////////

# Function No Parameters, No Return
def start_deployment_log():
    """This function just prints a starting message to the console."""
    print("=========================================")
    print("===      STARTING DEPLOYMENT      ===")
    print("=========================================")

# --- Script Starts Here ---
# දැන් function එක "call" කරලා (නමින් අඬගහලා) වැඩේ කරගන්නවා.
start_deployment_log() 

# (Some other deployment code goes here...)
print("Deploying web application...")

# (Some other code...)
print("Deployment finished.")











#////////////////////////////////////////////////////////

# Function takes Parameters, No Return
    
    

# Function Definition
def create_user(username, user_id):
    """Creates a new system user based on the provided info."""
    print(f"-> Creating user account: {username}")
    print(f"-> Setting user ID to: {user_id}")
    # Imagine a command like: subprocess.run(f"useradd -u {user_id} {username}")
    print(f"-> User '{username}' created successfully.")
    # Notice: No 'return' keyword

# --- Script Starts Here ---
print("Setting up new server...")

# Function එක call කරනවා, අවශ්‍ය data (arguments) වරහන් ඇතුලේ දෙනවා
create_user("dhanushka", 1001) 
create_user("api_service_acc", 1002)

print("Server setup complete.")

    
    
    
    
  

#////////////////////////////////////////////////////////

# Function takes Parameters, No Return
    
  

  # Function Definition
def is_disk_space_ok(disk_usage_percent, threshold):
    """
    Checks if the disk usage is below a given threshold.
    Returns True if space is OK, False otherwise.
    """
    print(f"-> Checking if {disk_usage_percent}% is below {threshold}% threshold...")
    if disk_usage_percent < threshold:
        return True  # ඉඩ තියෙනවා, ඒ නිසා True කියන boolean value එක return කරනවා
    else:
        return False # ඉඩ නෑ, ඒ නිසා False කියන boolean value එක return කරනවා

# --- Script Starts Here ---
# Function එක call කරලා, ඒකෙන් එන return value එක variable එකකට දාගන්නවා
server1_disk_ok = is_disk_space_ok(65, 90)

# දැන් අපිට ඒ return value එක (True/False) if condition එකක පාවිච්චි කරන්න පුළුවන්
if server1_disk_ok == True:
    print(" Server 1: Disk space is sufficient. Proceeding with backup.\n")
else:
    print(" Server 1: Not enough disk space! Aborting backup.\n")


# ආයෙමත් call කරමු, වෙන data එක්ක
server2_disk_ok = is_disk_space_ok(95, 90)

if server2_disk_ok == True:
    print(" Server 2: Disk space is sufficient. Proceeding with backup.")
else:
    print(" Server 2: Not enough disk space! Aborting backup.")
    