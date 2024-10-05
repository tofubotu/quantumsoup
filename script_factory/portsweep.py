import socket, threading, argparse, ipaddress, time
def check_ports(ip, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                print(f"{ip}:{port} open")
            sock.close()
        except:
            pass
def scan_network(network, ports):
    threads = []
    for ip in ipaddress.IPv4Network(network):
        t = threading.Thread(target=check_ports, args=(str(ip), ports))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("network"), parser.add_argument("ports")
    args = parser.parse_args()
    start = time.time()
    scan_network(args.network, [int(p) for p in args.ports.split(",")])
    print(f"Scan completed in {time.time() - start:.2f} seconds")
