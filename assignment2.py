import sys

def read_requests_from_file(file_path):
    """Reads cylinder requests from the specified file."""
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file]
    return requests

def fcfs(initial_position, requests):
    """First-Come, First-Served (FCFS) disk scheduling algorithm."""
    current_position = initial_position
    total_head_movements = 0
    
    for request in requests:
        total_head_movements += abs(request - current_position)
        current_position = request
    
    return total_head_movements

def scan(initial_position, requests):
    """SCAN disk scheduling algorithm (elevator algorithm)."""
    current_position = initial_position
    total_head_movements = 0
    
    sorted_requests = sorted(requests)

    total_head_movements += current_position

    for request in sorted_requests:
        if request >= current_position:
            total_head_movements += abs(request - current_position)
            current_position = request

    total_head_movements += (current_position - 0)
    
    return total_head_movements

def cscan(initial_position, requests):
    """Circular SCAN (C-SCAN) disk scheduling algorithm."""
    current_position = initial_position
    total_head_movements = 0
    
    sorted_requests = sorted(requests)

    total_head_movements += current_position

    for request in sorted_requests:
        if request >= current_position:
            total_head_movements += abs(request - current_position)
            current_position = request

    total_head_movements += (4999 - current_position)
    current_position = 0
    
    for request in sorted_requests:
        total_head_movements += abs(request - current_position)
        current_position = request
    
    return total_head_movements

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduler.py initial_position requests_file.txt")
        sys.exit(1)
    
    initial_position = int(sys.argv[1])
    requests_file = sys.argv[2]

    requests = read_requests_from_file(requests_file)

    print("Task 1 - Service requests as they appear:")
    print("FCFS Head Movements:", fcfs(initial_position, requests[:]))
    print("SCAN Head Movements:", scan(initial_position, requests[:]))
    print("C-SCAN Head Movements:", cscan(initial_position, requests[:]))
    
    sorted_requests = sorted(requests)
    
    print("\nTask 2 - Rearranged requests to minimize head movements:")
    print("FCFS Head Movements:", fcfs(initial_position, sorted_requests))
    print("SCAN Head Movements:", scan(initial_position, sorted_requests))
    print("C-SCAN Head Movements:", cscan(initial_position, sorted_requests))

# python disk_scheduler.py <initial_position> <requests_file.txt>
# run in terminal by replacing the initial position and requests file with the desired values
