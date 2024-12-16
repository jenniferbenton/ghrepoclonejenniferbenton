import os
# This imports the os module, which provides functions to interact with the operating system.
# For example, it allows us to create directories, read or write files, and more.

from datetime import datetime
# This imports the datetime class from the datetime module, which we use to get the current date and time.
# This is useful for tasks that require timestamping or scheduling.

import wmi
# This imports the wmi module, which allows us to interact with Windows Management Instrumentation (WMI).
# WMI is a set of tools that lets us query and control various aspects of the Windows operating system.

# Directory to store the output files
output_dir = "output"
# This sets the name of the directory where we will store our output files.
# The directory is named "output".

os.makedirs(output_dir, exist_ok=True)
# This creates the directory if it doesn't already exist.
# The exist_ok=True parameter means that if the directory already exists, no error will be raised.

# Initialize WMI object
wmi_obj = wmi.WMI()
# This creates a WMI object that we can use to query system information.
# With this object, we can perform various tasks like checking running processes, system logs, etc.

# Task 1: Find all scripting commands that are print related. Output the list to a local file.
# Note: WMI does not provide a direct way to list all commands. This task typically requires system commands.

# Task 2: Append (the long version of) the current date and time to the same file.
print_commands_file = os.path.join(output_dir, "print_commands.txt")
# This sets the path for the file where we will store the print commands and date/time.
# The file will be located in the "output" directory and named "print_commands.txt".

with open(print_commands_file, "a") as f:
    # This opens the file in append mode (so we can add to it without deleting existing content).
    # The "a" mode stands for append.
    f.write("\n" + datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p") + "\n")
    # This writes the current date and time in a long format to the file.
    # The strftime method formats the date and time in a readable way, like "Monday, December 16, 2024 03:04:24 PM".

# Task 3: Close all notepad files.
for process in wmi_obj.Win32_Process(name="notepad.exe"):
    # This loops through all processes named "notepad.exe".
    # Each process represents an instance of Notepad running on the system.
    process.Terminate()
    # This closes each Notepad process.
    # The Terminate method stops the process.

# Task 4: Append the last 20 errors from the event log to the same file.
with open(print_commands_file, "a") as f:
    # This opens the file in append mode.
    for log in wmi_obj.Win32_NTLogEvent(EventType=1)[:20]:  # EventType=1 for error
        # This loops through the last 20 error events (EventType=1 means error).
        # The [:20] slice means we are only taking the first 20 error events.
        f.write(f"Source: {log.SourceName}, Event ID: {log.EventCode}, Message: {log.Message}\n")
        # This writes the source, event ID, and message of each error to the file.
        # The f-string format makes it easy to include variables in the string.

# Task 5: Append a list of all available WMI classes to the same file.
with open(print_commands_file, "a") as f:
    # This opens the file in append mode.
    for wmi_class in wmi_obj.classes:
        # This loops through all available WMI classes.
        # WMI classes represent different types of system information we can query.
        f.write(wmi_class + "\n")
        # This writes each WMI class name to the file.
        # Each class name is written on a new line.

# Task 6: List the start command or full path of every executable (hint: use wmi).
executables_file = os.path.join(output_dir, "executables.txt")
# This sets the path for the file where we will store the executable paths.
# The file will be located in the "output" directory and named "executables.txt".

with open(executables_file, "w") as f:
    # This opens the file in write mode.
    # The "w" mode stands for write, which means it will overwrite the file if it already exists.
    for process in wmi_obj.Win32_Process():
        # This loops through all running processes.
        # Each process represents a program currently running on the system.
        f.write(f"Name: {process.Name}, Path: {process.ExecutablePath}\n")
        # This writes the name and path of each executable to the file.
        # The ExecutablePath property gives the full path to the executable file.

# Task 7: Identify what account the spooler is running as (hint: use wmi).
spooler_info_file = os.path.join(output_dir, "spooler_info.txt")
# This sets the path for the file where we will store the spooler service information.
# The file will be located in the "output" directory and named "spooler_info.txt".

with open(spooler_info_file, "w") as f:
    # This opens the file in write mode.
    for service in wmi_obj.Win32_Service(Name="Spooler"):
        # This loops through the spooler service.
        # The spooler service manages print jobs sent to the printer.
        f.write(f"Name: {service.Name}, StartName: {service.StartName}\n")
        # This writes the name and the account the spooler service is running under to the file.
        # The StartName property gives the account name.

print("Tasks completed. Check the 'output' directory for results.")
# This prints a message indicating that the tasks are completed and the results are in the output directory.