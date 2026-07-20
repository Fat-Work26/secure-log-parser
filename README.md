# Simple Log Parser

This is a simple python Tool to analyze server log files.
It helpe to fine and count failed login attempts to make servers more secure.

------

# Features

1. Save Memory: It reads big files line by line using Python Generators ('yield').
2. Find IPs: It uses Regular Expressions ('re') to find and extract IP Addresses from text.
3. Count Attack: It uses Python Dictionaries '{}' to count how many times each IP faild to log in.
4. Check File: It checks if the file path is correct before opening it using the 'os' module and os.path.isfile().

------

 # Concepts Used

 * Python Generators(`yield`)
 * Regular Expressions(`re`)
 * Python Dictionaries (`{}`)
 * File Input/Output (`I/O`).

------

# How To Run It

 Run the script in your terminal:
 ``` python index.py ```

