def log_message(message):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

log_message("Started studying Chapter 10")
log_message("Finished file reading/writing exercises")

with open("log.txt", "r") as f:
    lines = f.readlines()

print(f"Total log entries: {len(lines)}")
for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")