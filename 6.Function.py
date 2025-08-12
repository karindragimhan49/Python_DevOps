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