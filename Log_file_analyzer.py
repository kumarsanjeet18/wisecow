import re
from collections import Counter

# Function to parse a single log line
def parse_log_line(line):
    pattern = re.compile(
        r'(?P<ip>[\d\.]+) - - \[(?P<date_time>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+|-)'
    )
    match = pattern.match(line)
    if match:
        return match.groupdict()
    return None

# Function to analyze the log file
def analyze_log_file(log_file_path):
    with open(log_file_path, 'r') as file:
        lines = file.readlines()
    
    request_counter = Counter()
    status_counter = Counter()
    ip_counter = Counter()
    page_counter = Counter()
    
    for line in lines:
        log_data = parse_log_line(line)
        if log_data:
            request = log_data['request']
            status = log_data['status']
            ip = log_data['ip']
            
            request_counter[request] += 1
            status_counter[status] += 1
            ip_counter[ip] += 1
            
            # Extracting page from the request
            page = request.split(' ')[1]
            page_counter[page] += 1
    
    return request_counter, status_counter, ip_counter, page_counter

# Function to generate the report
def generate_report(log_file_path):
    request_counter, status_counter, ip_counter, page_counter = analyze_log_file(log_file_path)
    
    print("===== Web Server Log Analysis Report =====")
    
    # Number of 404 errors
    num_404_errors = status_counter.get('404', 0)
    print(f"Number of 404 errors: {num_404_errors}")
    
    # Most requested pages
    print("\nTop 10 Most Requested Pages:")
    for page, count in page_counter.most_common(10):
        print(f"{page}: {count} requests")
    
    # IP addresses with the most requests
    print("\nTop 10 IP Addresses with Most Requests:")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip}: {count} requests")
    
    print("==========================================")

# Example usage
log_file_path = 'webserver.log'  # Replace with your log file path
generate_report(log_file_path)
