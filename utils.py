import os
from datetime import datetime

def is_scam_ip(ip_address, scam_ip_file="scam_ips.txt"):
    try:
        with open(scam_ip_file, "r") as f:
            scam_ips = {line.strip() for line in f if line.strip()}
        return ip_address in scam_ips
    except FileNotFoundError:
        print("Scam IP file not found.")
        return False

def preprocess_data(data):
    return data

def write_log(message, log_file_path):
    # Ensure the logs directory exists (robust for all cases)
    log_file_path = os.path.abspath(log_file_path)
    log_dir = os.path.dirname(log_file_path)
    try:
        os.makedirs(log_dir, exist_ok=True)
    except Exception as e:
        print(f"Error creating log directory: {e}")
        return
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")