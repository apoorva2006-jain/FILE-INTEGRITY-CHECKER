# FILE-INTEGRITY-CHECKER

"COMPANY" : CODTECH IT SOLUTIONS

"NAME" : APOORVA S

"INTERN ID" : CT12DG815

"DOMAIN" : CYBER SECURITY AND ETHICAL HACKING 

"DURATION" : 12 WEEKS

"MENTOR" : NEELA SANTOSH KUMAR 

## File Integrity Checker – Python Project
Project Overview:

The File Integrity Checker is a Python tool used to monitor file changes by calculating and comparing their hash values. If a file is changed, deleted, or a new file is added in the folder, the script detects and reports it. This helps ensure the integrity and security of important files.

This project was built using Python and run using the Thonny IDE, a beginner-friendly Python environment. The script was written in Thonny and uploaded to GitHub using the browser, making the project simple and accessible for students.

Tools & Technologies Used:

Language: Python 3.11

Editor/IDE: Thonny (for writing and executing the script)

Operating System: Windows 10

Code Hosting Platform: GitHub (via browser)

Python Libraries Used:

hashlib – for creating SHA-256 hash values

os – for navigating folders and files

json – for saving and comparing file hashes

Purpose of the Project:
 
The aim of this project is to track and report any changes in files using secure hash functions. It helps detect:

 Modified files (file content has changed)

 Deleted files (missing files)

 New files (recently added to the folder)

It is useful for:

Protecting sensitive files

Verifying backups

Detecting unauthorized access or tampering

Learning cybersecurity basics

How It Works:

The script scans all files in a selected folder.

It generates a SHA-256 hash for each file.

These hash values are saved in a file called hashes.json.

On later execution, it recalculates hashes and compares them with the saved ones.

It shows:

[MODIFIED] if the file’s content changed

[DELETED] if the file is missing

[NEW FILE] if a new file has appeared

Key Features:
 
Simple to understand and run in Thonny

Uses only built-in Python modules

Clear output showing changes

Works with any folder

Beginner-friendly and educational

Conclusion:

This project demonstrates the use of hashing and file tracking in Python. Built using the Thonny IDE and managed on GitHub, it’s ideal for learning how programming can solve real-life problems like file monitoring and data protection. It’s a practical, easy-to-build project with real cybersecurity relevance.
