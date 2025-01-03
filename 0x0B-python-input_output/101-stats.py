#!/usr/bin/python3
'''
This script reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
Total file size: File size: <total size>
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
'''

import sys

def print_stats(total_size, status_counts):
    '''
    Prints the statistics.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary containing the count of each status code.
    '''
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def main():
    total_size = 0
    status_counts = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 9:
                status_code = int(parts[8])
                file_size = int(parts[9])
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

if __name__ == "__main__":
    main()
