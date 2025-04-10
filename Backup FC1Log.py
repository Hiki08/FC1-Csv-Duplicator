# %%
import shutil
import os
import datetime

# %%
# Set the source and destination folders
src_folder = '//192.168.2.19/general/INSPECTION-MACHINE/FC1'
dst_folder = '//192.168.2.19/general/INSPECTION-MACHINE/Backups'

# Create a timestamp for the backup folder
timestamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
backup_folder = os.path.join(dst_folder, f'FC1_{timestamp}')

# Create the backup folder if it doesn't exist
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Walk through the source folder and copy all files and subfolders
for root, dirs, files in os.walk(src_folder):
    for file in files:
        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, src_folder)
        dst_path = os.path.join(backup_folder, rel_path)
        dst_dir = os.path.dirname(dst_path)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        shutil.copy2(file_path, dst_path)

print(f'Backup completed: {backup_folder}')


