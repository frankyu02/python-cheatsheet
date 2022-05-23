#Python can read, Create, Update and delete files

#open file. If File does not exist, it will automatically create it
myFile = open('testfile.txt', 'w+') #'w' gives it write permissions

#Permissions you can give: 
# r: read permission only
# w: write permission. Any file opened will have its contents deleted
# r+: read and write permissions. The contents of the file WILL NOT be deleted on open
# w+: real and write permissions. The contents of the file WILL be deleted on open

#getting file information
print('File Name: ', myFile.name)
print('is closed: ', myFile.closed) #checks if file has been closed within the program.
print('Opening Mode: ', myFile.mode) 

#Writing to a file
myFile.write('fuck python but I mean this kinda cool I guess ')
myFile.write('This line will still be written on the same line though \n')
myFile.write('now this will be on a different line')

print(myFile.read(50)) #this will print nothing. Why? because myFile on initiation is a blank document as a result of 'w+' permission
myFile.close() #this will close the file

myFile = open('testfile.txt', 'r+')
#Read File
print(myFile.read(50)) #reads 50 characters of file