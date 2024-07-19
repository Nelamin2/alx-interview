#!/usr/bin/python3
"""
Log parsing script
"""
import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    """
    Prints the accumulated metrics
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C)
    """
    print_metrics()
    sys.exit(0)

# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 9:
            continue

        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            total_file_size += file_size
        except ValueError:
            continue

        line_count += 1

        if line_count % 10 == 0:
            print_metrics()

except Exception as e:
    pass

# Print metrics one last time after all lines are processed
print_metrics()

