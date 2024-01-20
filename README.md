# FTP-Password-Cracker
# Now, let's analyze what we did here.

# On line 3, we imported the ftplib module for use by our FTP cracker.

# on Line 5 , we print the banner of our script and it's optional.

# On line 15, we ask the user what IP address that want to try to crack and that data is placed in a variable named "server".

# On line 19, we ask the user what user that want to attempt to crack the password for and place that data into a variable "username".

# On line 23, we prompt the user for the path and filename of their password list and place it in a variable named "passwordlist".

# On line 26, we begin a try/except block. This block will attempt some code and if it fails or has an error, will fall out and go to the except clause below.

# On line 25, we begin a looping structure "with". This looping structure continues as long as the condition after it evaluates to true. In this case, we use the function open to open a password list and this loop will continue as long as this file is # open or it hits an end of file.

# On line 27, we begin a for loop that will iterate through each password and remove any leading and trailing spaces using the strip function.

# On line 36, we come to the heart of our password cracking. Here, first we connect to the FTP server.

# ftp=ftplib.FTP(server)

# Then, we begin a try/except clause to try each password word for the username the user input above.

# ftp.login(username, word)

# If the username and password creates a successful connection, the "Success!" 
# statement prints with the password and the connection is closed. 
# If it fails, it falls out to the except clause below.

# When it finds the password and successfully connects to the FTP server, it will print 
# the message "Success! You have connected to the FTP Server.
# The password is <password>"

# keep in mind that this is just a basic ftp password cracker you can modify iy more and make it work with http and https
