"""
Question 1
The create_python_script function creates a new python script in the current working directory,
adds the line of comments to it declared by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".
"""

import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename,"w+") as fhandle:
    fhandle.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))

"""
Question 2
The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory.
Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".
"""

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.makedirs(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename,"w+") as file:
    #file.write(" ")
    pass

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))

"""
3.
Question 3
Which of the following methods from the os module will create a new directory?

path.isdir()
listdir()
mkdir() - Correct Ans
chdir()
"""

"""
4.
Question 4
The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd.
Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.
"""

import os
import datetime,time

def file_date(filename):
  # Create the file in the current directory
  with open (filename,"w+") as file:
    pass
  timestamp = time.localtime(os.path.getmtime(filename))
  # Convert the timestamp into a readable format, then into a string
  """
  print(timestamp)
  print('Year: {:4d}'.format(date_created_obj.tm_year)) # Year: 2020
  print('Month: {:2d}'.format(date_created_obj.tm_mon)) # Month:  11
  print('Day: {:2d}'.format(date_created_obj.tm_mday)) # Day: 10
  """
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{:4d}-{:2d}-{:2d}".format(timestamp.tm_year,timestamp.tm_mon,
  timestamp.tm_mday))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd


"""
Question 5
The parent_directory function returns the name of the directory that's located just above the current working directory.
Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function.
"""

import os
def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  relative_parent = os.path.join("..", os.getcwd())

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())
