# %%
from Imports import *

# %%
isProcess1Readed = False
isProcess2Readed = False
isProcess3Readed = False
isProcess4Readed = False
isProcess5Readed = False
isProcess6Readed = False

isDuplicated = False

process1OrigFile = ""
process2OrigFile = ""
process3OrigFile = ""
process4OrigFile = ""
process5OrigFile = ""
process6OrigFile = ""

process1CurrentFile = ""
process2CurrentFile = ""
process3CurrentFile = ""
process4CurrentFile = ""
process5CurrentFile = ""
process6CurrentFile = ""

readCount = 0

# %%
def duplicateCsv():
    src_folder = '//192.168.2.10/csv/Ai Csv/Process'
    dst_folder = '//192.168.2.19/ai_team/AI Program/Outputs'

    # Create a timestamp for the backup folder
    timestamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
    backup_folder = os.path.join(dst_folder, f'FC1 CSV')

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


# %%
os.system('echo -ne "\033]0;CSV DUPLICATOR\007"')

#Reading Original File
process1OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT1\log000_1.csv")
process2OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT2\log000_2.csv")
process3OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT3\log000_3.csv")
process4OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT4\log000_4.csv")
process5OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT5\log000_5.csv")
process6OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT6\log000_6.csv")

while True:
    #Checking Changes In PiCompiled Using Forced Reading Of Csv
    while not isProcess1Readed:
        try:
            process1CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT1\log000_1.csv")
            isProcess1Readed = True
        except:
            print("Failed Reading Of Process1 Trying Again In 1 Seconds")
            pass

    while not isProcess2Readed:
        try:
            process2CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT2\log000_2.csv")
            isProcess2Readed = True
        except:
            print("Failed Reading Of Process2 Trying Again In 1 Seconds")
            pass

    while not isProcess3Readed:
        try:
            process3CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT3\log000_3.csv")
            isProcess3Readed = True
        except:
            print("Failed Reading Of Process3 Trying Again In 1 Seconds")
            pass

    while not isProcess4Readed:
        try:
            process4CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT4\log000_4.csv")
            isProcess4Readed = True
        except:
            print("Failed Reading Of Process4 Trying Again In 1 Seconds")
            pass

    while not isProcess5Readed:
        try:
            process5CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT5\log000_5.csv")
            isProcess5Readed = True
        except:
            print("Failed Reading Of Process5 Trying Again In 1 Seconds")
            pass

    while not isProcess6Readed:
        try:
            process6CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\Ai Csv\Process\VT6\log000_6.csv")
            isProcess6Readed = True
        except:
            print("Failed Reading Of Process6 Trying Again In 1 Seconds")
            pass

    isProcess1Readed = False
    isProcess2Readed = False
    isProcess3Readed = False
    isProcess4Readed = False
    isProcess5Readed = False
    isProcess6Readed = False

    #If Changes Detected In File
    if process1CurrentFile != process1OrigFile or process2CurrentFile != process2OrigFile or process3CurrentFile != process3OrigFile or process4CurrentFile != process4OrigFile or process5CurrentFile != process5OrigFile or process6CurrentFile != process6OrigFile:
        print("Changes Detected")

        while not isDuplicated:
            try:
                duplicateCsv()
                isDuplicated = True
            except:
                pass
        isDuplicated = False

        #Setting The Original File Onto Current File
        process1OrigFile = process1CurrentFile
        process2OrigFile = process2CurrentFile
        process3OrigFile = process3CurrentFile
        process4OrigFile = process4CurrentFile
        process5OrigFile = process5CurrentFile
        process6OrigFile = process6CurrentFile

    print("Waiting For Changes In PiCompiled")
    time.sleep(1)
    
    readCount += 1
    if readCount >= 10:
        os.system('cls')
        readCount = 0


