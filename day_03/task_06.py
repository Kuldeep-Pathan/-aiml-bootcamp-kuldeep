import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta
import random


# ============================================================
# TASK 06 - Parse a Real Log File
# ============================================================

# ------------------------------------------------------------
# 1. Generate a log file with 250 lines
# ------------------------------------------------------------

levels = ["INFO", "WARN", "ERROR"]

messages = {
    "INFO": [
        "User logged in successfully",
        "Data processing completed",
        "File uploaded successfully",
        "Database connection established",
        "Request processed successfully",
    ],
    "WARN": [
        "High memory usage detected",
        "Slow response time detected",
        "Disk space is getting low",
        "API rate limit approaching",
        "Connection is unstable",
    ],
    "ERROR": [
        "Database connection failed",
        "File not found",
        "Authentication failed",
        "Request timeout",
        "Database connection failed",
    ],
}

start_time = datetime(2026, 9, 22, 0, 0, 0)

with open("application.log", "w") as file:
    for i in range(250):
        timestamp = start_time + timedelta(
            minutes=random.randint(0, 1439),
            seconds=random.randint(0, 59)
        )

        level = random.choice(levels)
        message = random.choice(messages[level])

        line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} {level} {message}\n"
        file.write(line)

print("application.log created with 250 lines")


# ------------------------------------------------------------
# 2. Read the log file
# ------------------------------------------------------------

with open("application.log", "r") as file:
    lines = file.readlines()


# ------------------------------------------------------------
# 3. Regex pattern
# ------------------------------------------------------------

pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(.*)"


# ------------------------------------------------------------
# 4. Parse log entries
# ------------------------------------------------------------

entries = []

for line in lines:
    line = line.strip()

    m = re.match(pattern, line)

    if m:
        ts, level, msg = m.groups()

        timestamp = datetime.strptime(
            ts,
            "%Y-%m-%d %H:%M:%S"
        )

        entries.append({
            "timestamp": timestamp,
            "level": level,
            "message": msg
        })


# ------------------------------------------------------------
# 5. Count entries per level
# ------------------------------------------------------------

level_counts = Counter(
    entry["level"]
    for entry in entries
)

print("\nEntries per level:")
print(level_counts)


# ------------------------------------------------------------
# 6. Find the busiest hour
# ------------------------------------------------------------

hour_counts = Counter(
    entry["timestamp"].hour
    for entry in entries
)

busiest_hour, busiest_count = hour_counts.most_common(1)[0]

print("\nBusiest hour:")
print(f"{busiest_hour:02d}:00 - {busiest_hour:02d}:59")
print("Entries:", busiest_count)


# ------------------------------------------------------------
# 7. Most frequently repeated ERROR message
# ------------------------------------------------------------

error_messages = Counter(
    entry["message"]
    for entry in entries
    if entry["level"] == "ERROR"
)

if error_messages:
    most_common_error, error_count = error_messages.most_common(1)[0]

    print("\nMost frequent ERROR message:")
    print(most_common_error)
    print("Count:", error_count)
else:
    print("\nNo ERROR entries found.")


# ------------------------------------------------------------
# 8. Group entries by level using defaultdict
# ------------------------------------------------------------

entries_by_level = defaultdict(list)

for entry in entries:
    entries_by_level[entry["level"]].append(entry)

print("\nEntries grouped by level:")

for level, level_entries in entries_by_level.items():
    print(level, ":", len(level_entries))


# ------------------------------------------------------------
# 9. Bonus - Longest gap between ERROR entries
# ------------------------------------------------------------

error_entries = sorted(
    [
        entry
        for entry in entries
        if entry["level"] == "ERROR"
    ],
    key=lambda entry: entry["timestamp"]
)

if len(error_entries) >= 2:

    longest_gap = timedelta(0)
    gap_start = None
    gap_end = None

    for i in range(1, len(error_entries)):

        current_time = error_entries[i]["timestamp"]
        previous_time = error_entries[i - 1]["timestamp"]

        gap = current_time - previous_time

        if gap > longest_gap:
            longest_gap = gap
            gap_start = previous_time
            gap_end = current_time

    print("\nLongest gap between ERROR entries:")
    print("Gap:", longest_gap)
    print("From:", gap_start)
    print("To:", gap_end)

else:
    print("\nNot enough ERROR entries to calculate a gap.")


# ------------------------------------------------------------
# 10. Display total parsed entries
# ------------------------------------------------------------

print("\nTotal parsed entries:")
print(len(entries))