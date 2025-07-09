 Port Scanner GUI using Python

A user-friendly and multithreaded **Port Scanner Tool** built using **Python**, **Tkinter**, and **sockets**. This GUI-based application allows users to scan a specific IP address or domain for open and closed ports within a defined range, and it displays associated service names (e.g., HTTP, FTP, SSH).

 Developed as part of a Cybersecurity Internship Project  
 For ethical use and educational demonstrations only


## Demo

Screenshot.png

##  Features

-  Graphical User Interface using **Tkinter**
-  Fast **multithreaded** port scanning
-  **Domain/IP resolution** with error handling
-  Detects and displays:
  - Open ports
  - Closed ports
  - Common services (HTTP, FTP, SSH, etc.)
-  Real-time logging inside GUI
-  Lightweight and beginner-friendly

## Tech Stack

| Component     | Description                           |
|---------------|----------------------------------------|
| Python        | Core programming language              |
| Tkinter       | GUI creation                           |
| socket        | Network communication (TCP scan)       |
| threading     | Concurrent scanning                    |
| ScrolledText  | Scrollable output box in GUI           |



## Setup Instructions

--Clone the Repository

git clone https://github.com/abireshu/Python-port-scanner.git
cd Python-port-scanner.git

--Create a Virtual Environment
python -m venv venv
source venv/bin/activate

--install requirements
pip install -r requirements.txt

--run
python Port_scan.py

***Educational Use Case***
This project is ideal for:

Students learning about network security.

Beginners exploring ethical hacking and port scanning.

Demonstrating how TCP ports and services interact.

Visualizing the impact of open ports in a system/network.



