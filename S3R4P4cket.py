import subprocess
import time
from datetime import datetime
import os

def get_user_input():
    """Function to get user input."""
    start_time = input("Enter the capture start time (format HH:MM): ")
    duration = int(input("Enter the capture duration in seconds: "))
    repeat_count = int(input("Enter the number of capture repetitions: "))
    interface = input("Enter the network interface name (e.g., enp0s3): ")
    capture_dir = input("Enter the directory to save the capture results (e.g., /home/ubuntu/captures): ")

    # Ensure the directory exists
    if not os.path.exists(capture_dir):
        print("Directory {} does not exist. Creating directory...".format(capture_dir))
        os.makedirs(capture_dir)

    return start_time, duration, repeat_count, interface, capture_dir

def wait_until_start_time(start_time):
    """Wait until the specified time to start the capture"""
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == start_time:
            print("Starting capture at {}".format(start_time))
            break
        # Wait 1 second before checking the time again
        time.sleep(1)

def start_capture(i, duration, interface, capture_dir):
    """Run tshark to capture packets for the specified duration"""
    capture_filename = os.path.join(capture_dir, "capturing{}.pcap".format(i))  # Using os.path.join for cross-platform compatibility
    print("Starting capture {}...".format(i))
    # Run the tshark command using subprocess
    subprocess.run(["sudo", "tshark", "-i", interface, "-a", "duration:{}".format(duration), "-w", capture_filename])
    print("Capture {} complete.".format(i))

def main():
    # Get user input
    start_time, duration, repeat_count, interface, capture_dir = get_user_input()

    # Wait until the specified start time
    wait_until_start_time(start_time)

    # Start capture according to the specified repetition count
    for i in range(1, repeat_count + 1):
        start_capture(i, duration, interface, capture_dir)

    print("All captures completed!")

if __name__ == "__main__":
    main()

