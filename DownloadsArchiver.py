import os
import shutil
import datetime

# Get the current user's home directory
# Make sure that you have permissions.
home_directory = os.path.expanduser('~')

# Set the directory to the Downloads folder
downloads_directory = os.path.join(home_directory, 'Downloads')

# Get the current date
today = datetime.datetime.today()

# Create the name for the new folder
folder_name = 'Archive' + today.strftime('%m%d%y')

# Create the new folder
os.mkdir(os.path.join(downloads_directory, folder_name))

# Iterate through all files in the Downloads folder
for file in os.listdir(downloads_directory):
    # Check if the file is not in a subfolder
    if os.path.isdir(os.path.join(downloads_directory, file)):
        continue
    # Move the file to the new folder
    shutil.move(os.path.join(downloads_directory, file), os.path.join(downloads_directory, folder_name))
