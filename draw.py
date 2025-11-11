import os
import datetime
import subprocess

# Replace this with your "MANISH" pattern
pattern = [
    "M   M   AAAAA  N   N  III  SSSS  H   H",
    "MM MM   A   A  NN  N   I   S     H   H",
    "M M M   AAAAA  N N N   I   SSSS  HHHHH",
    "M   M   A   A  N  NN   I      S  H   H",
    "M   M   A   A  N   N  III  SSSS  H   H",
]

# Start date: 52 weeks ago (Sunday)
start_date = datetime.date.today() - datetime.timedelta(weeks=52)
start_date -= datetime.timedelta(days=start_date.weekday() + 1)

for col in range(len(pattern[0])):
    for row in range(5):  # only 5 used rows
        if pattern[row][col] != " ":
            # Calculate date of this cell
            day = start_date + datetime.timedelta(weeks=col, days=row)
            # Make a few commits (3 = medium green)
            for i in range(3):
                with open("graph.txt", "a") as f:
                    f.write(f"Commit on {day}\n")
                subprocess.run(["git", "add", "graph.txt"])
                subprocess.run([
                    "git", "commit", "-m", f"Commit on {day}",
                    "--date", f"{day}T12:00:00"
                ])
