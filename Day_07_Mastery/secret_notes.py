with open("tracker.txt", "a") as log:
    task1 = input("enter day: ")
    task2 = input("count: ")
    log.write(f"{task1} - {task2} pushups")