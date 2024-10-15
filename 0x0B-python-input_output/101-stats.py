#!/usr/bin/python3
# Parses logs from stdin and computes metrics

import sys

# Initialize variables to track file size and status codes
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_codes = status_codes.keys()
line_count = 0

def print_stats():
    """Print the current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        # Ensure the line has at least the expected number of fields
        if len(parts) > 6:
            try:
                # Extract the file size
                size = int(parts[-1])
                total_size += size
            except ValueError:
                pass
            
            try:
                # Extract the status code
                status_code = int(parts[-2])
                if status_code in valid_codes:
                    status_codes[status_code] += 1
            except ValueError:
                pass
        
        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle Ctrl+C interrupt and print stats before exiting
    print_stats()
    raise

# Print final stats after processing all lines
print_stats()
