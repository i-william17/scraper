import psutil
import time

def monitor_network():
    print("MONITERING NETWORK ACTIVITY>>>>>>")

    while True:
        connections = psutil.net_connections(kind='inet')
        for conn in connections:
            if conn.status == 'ESTABLISHED':
                print(f"Active Connection:{conn.laddr.ip}:{conn.laddr.port}->{conn.raddr.ip}:{conn.raddr.port} (PID:{conn.pid})")

            time.sleep(5) #REfresh every 5 seconds

if __name__ == "__main__":
    monitor_network()