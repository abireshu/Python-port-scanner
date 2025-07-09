import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

root = tk.Tk()
root.title("Port Scanner")
root.geometry("500x500")
root.resizable(False, False)

print_lock = threading.Lock()

port_services = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}

def scan_port(ip, port, output_area):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        service = port_services.get(port, "Unknown")
        with print_lock:
            output_area.insert(tk.END, f" [OPEN]   Port {port} ({service})\n")
    except:
        service = port_services.get(port, "Unknown")
        with print_lock:
            output_area.insert(tk.END, f" [CLOSED] Port {port} ({service})\n")
    finally:
        s.close()

def start_scan():
    target = entry_target.get()
    start_port = entry_start.get()
    end_port = entry_end.get()

    output_area.delete('1.0', tk.END)

    if not target or not start_port or not end_port:
        messagebox.showwarning("Missing Fields", "Please fill in all fields.")
        return

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        messagebox.showerror("Invalid Host", "Could not resolve hostname.")
        return

    try:
        start_port = int(start_port)
        end_port = int(end_port)
    except ValueError:
        messagebox.showerror("Port Error", "Ports must be valid numbers.")
        return

    output_area.insert(tk.END, f" Scanning {target} ({ip}) from port {start_port} to {end_port}...\n\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port, output_area))
        threads.append(t)
        t.start()

    def wait_for_threads():
        for t in threads:
            t.join()
        output_area.insert(tk.END, " Scanning completed.\n")

    threading.Thread(target=wait_for_threads).start()

tk.Label(root, text="Target IP / Domain:").pack(pady=5)
entry_target = tk.Entry(root, width=50)
entry_target.pack(pady=5)

tk.Label(root, text="Start Port:").pack()
entry_start = tk.Entry(root, width=20)
entry_start.pack(pady=5)

tk.Label(root, text="End Port:").pack()
entry_end = tk.Entry(root, width=20)
entry_end.pack(pady=5)

tk.Button(root, text="Start Scan", bg="#00aaff", fg="white", command=start_scan).pack(pady=10)

output_area = scrolledtext.ScrolledText(root, width=60, height=15)
output_area.pack(pady=10)

root.mainloop()
