from utils import preprocess_data, write_log, is_scam_ip

def main():
    # Define the log file path
    log_file_path = "logs/detection.log"

    # List of IP addresses to check
    ip_list = ["8.8.8.8", "192.168.1.100", "203.0.113.5","185.220.101.1","100.64.0.1","10.0.0.1"]

    for ip_to_check in ip_list:
        if is_scam_ip(ip_to_check):
            print(f"IP address {ip_to_check} is flagged as scam/malicious!")
            write_log(f"Scam IP detected: {ip_to_check}", log_file_path)
        else:
            print(f"IP address {ip_to_check} is clean.")
            write_log(f"IP checked and clean: {ip_to_check}", log_file_path)

if __name__ == "__main__":
    main()
    