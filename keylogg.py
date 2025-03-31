import psutil
import time


def detect_keyloggers():
    known_suspicious_processes = ["keylogger.exe", "hooker.exe", "spy.exe", "logger.exe"]

    while True:
        print("Scanning for keyloggers...")
        suspicious_found = False

        for process in psutil.process_iter(['pid', 'name']):
            try:
                process_name = process.info['name'].lower()
                if any(suspicious in process_name for suspicious in known_suspicious_processes):
                    print(f"[ALERT] Suspicious process detected: {process.info['name']} (PID: {process.info['pid']})")
                    suspicious_found = True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        if not suspicious_found:
            print("No keyloggers detected.")

        time.sleep(10)  # Scan every 10 seconds


if __name__ == "__main__":
    detect_keyloggers()
