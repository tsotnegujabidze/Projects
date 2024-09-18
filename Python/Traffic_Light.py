import time
current_mode = "Green"
while current_mode == "Green":

    if current_mode == "Green":
        print(current_mode)
        time.sleep(15)
        current_mode = "Yellow"


    if current_mode == "Yellow":
        print(current_mode)
        time.sleep(5)
        current_mode = "Red"

    if current_mode == "Red":
        print(current_mode)
        time.sleep(10)
        current_mode = "Yellow"

    if current_mode == "Yellow":
        print(current_mode)
        time.sleep(5)
        current_mode = "Green"