# Files parsing
This project contains test task from Dell Technologies and its solution.

# Task
Write a command or set of commands by using bash OR powershell OR python OR perl and perform both tasks 1 & 2.
The script must be working and give correct output when launched in the same directory with the files *messages.txt* and *vmax.txt*

1  
  - Count all messages with <err<err>> in *messages.txt*  
  - For each line with <err<err>> count total number of messages happened on each unique date
	
2
  - Parse *vmax.txt* to extract disk IDs (like 002A9) and paste each of them to command:
		*symaccess list -type stor -dev DISKID -sid 723*

# Execution
In order to be executed, python script must be launched it in the same directory with the files *messages.txt* and *vmax.txt* using the following command:  
#### python FilesParsing.py

# Result
As a result, *symaccess list -type stor -dev DISKID -sid 723* command is executed and *output.txt* file, containing answer for the first task, is created.
