# stockholm


## Description :
A small program capable of encrypting files recursively inside a directory.

It will only act on a ```infection``` folder in the user’s HOME directory

The program will act only on files with the extensions that were affected by Wannacry.

The program will rename all the files in the mentioned folder adding the ".ft" extension.


## Usage :

    usage: stockholm.py [-h] [-v | -r key] [-s]

    RANSOMWARE

    options:
    -h, --help            show this help message and exit
    -v                    Display the version of the program and exit
    -r key, -reverse key  Reverse the infection using the key provided as argument
    -s, -silent           silence the program, no output

### Example :
    # To encrypt all files inside $HOME/infection/
    python3 stockholm.py

    # To decrypt
    python3 stockholm.py -r $(cat ransom_key)

