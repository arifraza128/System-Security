def vm_isolation_simulation():
 print("\nTOP EXP 10: VM ISOLATION SIMULATION")
 virtual_machines = {
 "VM1": {
 "owner": "alice",
 "data": "Banking application data",
 "allowed": ["alice", "hypervisor_admin"]
 },
 "VM2": {
 "owner": "bob",
 "data": "Healthcare application data",
 "allowed": ["bob", "hypervisor_admin"]
 },
 "VM3": {
 "owner": "charlie",
 "data": "Research application data",
 "allowed": ["charlie", "hypervisor_admin"]
 }
 }
 print("Available VMs:", ", ".join(virtual_machines))
 username = input("Enter username: ")
 vm_name = input("Enter VM to access: ")
 if vm_name not in virtual_machines:
 print("VM not found.")
 return
 vm = virtual_machines[vm_name]
 if username in vm["allowed"]:
 print("Hypervisor access control: ACCESS GRANTED")
 print("VM:", vm_name)
 print("Data:", vm["data"])
 else:
 print("Hypervisor access control: ACCESS DENIED")
 print("VM isolation prevented unauthorized access.")
 print("Note: This is a logical simulation, not actual hypervisor isolation.")
