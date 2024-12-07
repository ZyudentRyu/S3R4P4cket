


![image](https://github.com/user-attachments/assets/ed123546-c604-49b8-8ffb-a40e0ae2a262)

This project automates network packet capture using tshark. The Python script allows configuration of start time, duration, repetitions, as well as the network interface and storage directory. Capture results are saved as .pcap files. Supports automatic repetition and creates the storage directory if it doesn't exist.

⚙️ **Key Features**

User Input Configuration: Takes user input to define start time, duration, number of repetitions, network interface, and storage directory.
Capture Result Storage: Saves network capture results in .pcap format for further analysis.
Automatic Repetition: Performs multiple captures automatically based on user configuration.
Automatic Directory Creation: Allows for the creation of the storage directory if it doesn’t exist.

🔧 **Technologies Used**

Python: Main programming language for script development.
Tshark: Network packet capture tool to capture traffic on the specified interface.
os, subprocess, datetime: Python modules for file management, running system commands, and handling time.

🚀 **How to Use**

Install Tshark
Make sure tshark is installed on your system. You can install it by running:


`sudo apt-get install tshark`

Clone the Repository

```
git clone https://github.com/ZyudentRyu/S3R4P4cket.git
cd S3R4P4cket
```

Run the Script
Execute the Python script to start capturing network packets:

`python3 S3R4P4cket.py`


Enter User Input
Follow the prompts in the terminal to specify the start time, duration, repetition count, network interface, and storage directory.

📚 Full Documentation
For further documentation, including additional configuration options and troubleshooting, check the documentation.

🔗 Contributing
Contributions to enhance functionality or add new features are welcome! To contribute:

Fork this repository.
Create a new branch for the changes you want to make.
Submit a pull request with a description of the changes you've made.
📈 Project Status

Latest Version: v1.0.0
Upcoming Updates: Improving error handling and adding support for a graphical interface.
