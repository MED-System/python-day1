from models import MedicalRobot
from security import eror_handle

hospital_fleet = []

print("--- MED-ROBOTICS REGISTRY SYSTEM ---")
total_to_register = int(eror_handle("How many robots are in today's batch? "))

# 2. Use that number to set the range
for i in range(total_to_register):
    print(f"\n[Processing Robot {i + 1} of {total_to_register}]")

    name = input("Enter Model Name: ")
    weight = eror_handle(f"Enter Weight for {name} (kg): ")

    # 3. Create and store
    robot = MedicalRobot(name, weight)
    hospital_fleet.append(robot)

# --- Simple Summary ---
print("REGISTRY COMPLETE!")
print("Here are your robots:")

# 'r' is just a nickname for each robot in your list
for r in hospital_fleet:
    print("Robot Name:", r.name)
    print("Robot Weight:", r.weight)
