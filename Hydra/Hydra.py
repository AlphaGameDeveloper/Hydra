
#    Hydra, basic text encryption; and more!
#    Copyright (C) 2022  Damien Boisvert (AlphaGameDev)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#   +-----------------------------------------------+
#   |   DO NOT REMOVE NEXT LINE OR THIS.            |
#   |More info: https://alphagame.dev/hydra/        |
#   +-----------------------------------------------+
#   
#   Version: b1.0 PRERELEASE.


import random
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import os
import subprocess
import sys
import hashlib
import alphagamelib
import tempfile
from art import tprint
from cryptography.fernet import Fernet
subprocess.call("title Hydra, by Damien B. (https://alphagame.dev/); Version: b1.0  BETA RELEASE!", shell=True) # Customize the terminal title (Windows only!)
# Write the LICENSE file on startup.
# We can't have people not knowing it ;)
with open("LICENSE", "w") as f:
    f.write(alphagamelib._LICENSE)

# Write the INFO file on startup.
# Just made it to rickroll someone ;)
with open("INFO", "w") as f:
    f.write("""
+--------------------------+
|   Hydra,                 |
|        By Damien B.      |
+--------------------------+

Info:
    Read the file "LICENSE" for more info on licensing...
    Never gonna give you up ;)
""")

#Main function for NOGUI mode.
def nogui(prevScrn=None):
    """
    No GUI (Graphical User Interface) mode for Hydra.
    Written by AlphaGameDev (Damien Boisvert)
    https://alphagame.dev/hydra
    """
    #This is just to make it so that, if there is an existing Tcl/Tk (Tkinter) window open, close it.
    if prevScrn == None:
        pass
    elif prevScrn == tk.Tk:
        prevScrn.destroy()
    #-------------------------

    # Print the basic licensing on startup.
    # Required by the GNU GPL v3.0 License.
    print("""
    Hydra  Copyright (C) 2022  Damien Boisvert (AlphaGameDev)
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

    More info can be found in the "LICENSE" file.
    Thank you for using ;)
    """)
    input("Press ENTER to accept and start the program.")
    alphagamelib.clear()
    #Main menu.
    tprint("Hydra")
    print("""
    [-- Options --]
        1 ------ Encrypt
        2 ------ Decrypt
        3 ------ Create new encryption key (Note: your previous encryptions will need the old key to be decrypted.)
        4 ------ More
        5 ------ Switch to GUI mode.
        6 ------ Exit.
        """)
    ch = alphagamelib.intInput(1, 6)
    if ch == 1:
        alphagamelib.clear()
        tprint("Encrypt")
        print("""
    [-- Options --]
        1 ------ Encrypt from text entered in console (No external file needed)
        2 ------ Encrypt from text entered in external file (External file needed)
        """)
        ch = alphagamelib.intInput(1, 2)
        if ch == 1:
            alphagamelib.clear()
            text = input("Enter text: ")
            key  = input("Enter / drag and drop key file path:  ")
            print("     Checking if KeyPath is a valid path...")
            if os.path.isfile(key) == False:
                print("     FATAL: KeyPath is not a valid directory.  Restarting the program.")
                input("Press ENTER to continue...")
                alphagamelib.clear()
                nogui()
            else:
                print("     Success.")
            print("Please enter if you want to dump encrypted data to file (y/n)")
            dump = alphagamelib.ynInput()
            print("I will now encrypt the text...")
            f = Fernet(open(key).read())
            encrypted = f.encrypt(bytes(text, "utf-8"))
            print("Encrypted text: " + str(encrypted))
            if dump == True:
                with open(input("Please enter the output path: "), 'wb') as file:
                    file.write(encrypted)
            print("Do you want to restart the program? (y/n)")
            restart = alphagamelib.ynInput()
            if restart == True:
                alphagamelib.clear()
                nogui()
            else:
                exit(0)
        if ch == 2:
            textP = input("Please enter / drag + drop text file.")
            print("     Checking if TextP is valid.")
            if os.path.isfile(textP) == False:
                print("     TextP is invalid.  This program will now self-distruct (Not really, it will simply restart ;]).")
                input("Press ENTER to continue...")
                alphagamelib.clear()
                nogui()
            else:
                print("     Success.")
            keyP = input("Please enter / drag and drop key file.")
            if os.path.isfile(keyP) == False:
                print("     keyP is invalid.  This program will now self-distruct (Not really, it will simply restart ;]).")
                input("Press ENTER to continue...")
                alphagamelib.clear()
                nogui()
            else:
                print("     Success.")
            print("Please enter if you want to dump encrypted data to file (y/n)")
            dump = alphagamelib.ynInput()
            print("I will now encrypt the text...")
            f = Fernet(open(keyP).read())
            encrypted = f.encrypt(bytes(open(textP).read(), "utf-8"))
            print("Encrypted text: " + str(encrypted))
            if dump == True:
                with open("output.txt", "wb") as file:
                    file.write(encrypted)
            print("Do you want to restart the program? (y/n)")
            restart = alphagamelib.ynInput()
            if restart == True:
                alphagamelib.clear()
                nogui()
            else:
                exit(0)
    elif ch == 2:
        alphagamelib.clear()
        tprint("Decrypt")
        print("""
[-- Options --]
    1 ------ Decrypt from text entered in terminal
    2 ------ Decrypt from text in external file.
        """)
        ch    = alphagamelib.intInput(1, 2)
        if ch == 1:
            encrypted = bytes(input("Please copy and paste the encrypted text: "))
            keyP      = input("Please enter / drag and drop the encrypted text key: ")
            if os.path.isfile(keyP) == False:
                print("     FATAL: KeyPath is not a valid directory.  Restarting the program.")
                input("Press ENTER to continue...")
                alphagamelib.clear()
                nogui()
            else:
                print("     Success.")
            f = Fernet(open(keyP).read())
            decrypted = f.decrypt(encrypted)
            print("Decrypted text: " + str(decrypted))
            print("Do you want to restart the program? (y/n)")
            restart = ynInput()
            if restart == True:
                alphagamelib.clear()
                nogui()
            else:
                exit(0)
        if ch == 2:
            encryptedP = input("Please enter the path for the encrypted data file: ")
            keyP       = input("Please enter the path for the encryption key file: ")
            print("Validating inputs...")
            if os.path.isfile(encryptedP) == True:
                print("Validating encryptedP... Success.")
            else:
                print('Error: the "encryptedP" path is INVALID; Restarting.')
                input("Press ENTER to continue...")
                alphagamelib.clear()
                nogui()
            if os.path.isfile(keyP) == True:
                print("Validating keyP... Success.")
            else:
                print('Error: the "kepP" path is INVALID; Restarting.')
                input("Press ENTER to continue...")
                alphagamelib.clear()
                nogui()
            print("Decrypting...")
            f = Fernet(open(keyP).read())
            decrypted = f.decrypt(bytes(open(encryptedP).read(), "utf-8"))
            print("Decrypted text: " + str(decrypted))
            print("Restarting...")
            input("Press ENTER to continue...")
            alphagamelib.clear()
            nogui()
    elif ch == 3:
        alphagamelib.clear()
        tprint("New Enc Key")
        p = input("Please enter the path for the new encryption key: must be in a valid directory. ")
        key = Fernet.generate_key()
        print("Here is your key; DO NOT SHARE WITH ANYONE; or they can decrypt your text...")
        print(key)
        with open(p, 'wb') as f:
            f.write(key)
        input("Press ENTER to continue...")
        alphagamelib.clear()
        nogui()
    elif ch == 4:
        alphagamelib.clear()
        tprint("More")
        print("""
[-- Options --]

    1 ------ Hash text (CAN NOT BE DECRYPTED)
    2 ------ Checksum file (This can be used to see if a file has been modified)
    3 ------ Compare checksums (Again, checks if file has been modified; and compares the checksum with another file to see if they are the same.)

            """)
        ch = alphagamelib.intInput(1, 3)
        if ch == 1:
            alphagamelib.clear()
            text = input("Enter text: ")
            print("""
Enter the number corresponding to the hash algorithm you want to use...
[-- Options --]
    1 ------ md5
    2 ------ sha1
    3 ------ sha224
    4 ------ sha256 <-- Most commonly used.
    5 ------ sha384
    6 ------ sha512 <-- Most secure.

            """)
            ch = alphagamelib.intInput(1, 6)
            print("Loading hasher object...  ", end="")
            if ch == 1:
                hasher = hashlib.md5()
            elif ch == 2:
                hasher = hashlib.sha1()
            elif ch == 3:
                hasher = hashlib.sha224()
            elif ch == 4:
                hasher = hashlib.sha256()
            elif ch == 5:
                hasher = hashlib.sha384()
            elif ch == 6:
                hasher = hashlib.sha512()
            print("Done.")
            print("Updating hasher with entered text...  ", end="")
            hasher.update(text.encode('utf-8'))
            print("Done.")
            print("The generated hash is:")
            hash = hasher.hexdigest()
            print(hash)
            print("Do you want to export the hash to a file? (y/n)")
            output = alphagamelib.ynInput()
            if output == True:
                with open("hash-output.txt", 'w') as f:
                    f.write(hash)
            print("Restarting...")
            input("Press ENTER to continue...")
            nogui()
        elif ch == 2:
            alphagamelib.clear()
            path = input("Enter path to file: ")
            if os.path.isfile(path) == True:
                print("Valid path.")
            else:
                print("Invalid path.")
                print("Restarting...")
                input("Press ENTER to continue...")
                nogui()
            with open(path, 'rb') as file:
                fileBytes = file.read()
            print("""
Enter the number corresponding to the hash algorithm you want to use...
[-- Options --]
    1 ------ md5
    2 ------ sha1
    3 ------ sha224
    4 ------ sha256 <-- Most commonly used.
    5 ------ sha384
    6 ------ sha512 <-- Most secure.

            """)
            ch = alphagamelib.intInput(1, 6)
            print("Loading hasher object...  ", end="")
            if ch == 1:
                hasher = hashlib.md5()
            elif ch == 2:
                hasher = hashlib.sha1()
            elif ch == 3:
                hasher = hashlib.sha224()
            elif ch == 4:
                hasher = hashlib.sha256()
            elif ch == 5:
                hasher = hashlib.sha384()
            elif ch == 6:
                hasher = hashlib.sha512()
            print("Done.")
            hasher.update(fileBytes)
            hash = hasher.hexdigest()
            print("Result")
            print(hash)
            output = alphagamelib.ynInput()
            if output == True:
                with open("hash-output.txt", 'w') as f:
                    f.write(hash)
            print("Restarting...")
            input("Press ENTER to continue...")
            nogui()
        elif ch == 3:
            f1 = input("Please input the path to the 1st file: ")
            f2 = input("Please input the path to the 2nd file: ")
            print("Validating inputs...")
            print("Checking input 1 validity...  ", end="")
            if os.path.isfile(f1) == True:
                print("Done.  Valid.")
            else:
                print("\nInvalid path for: input 1...")
                print("Restarting...")
                input("Press ENTER to continue...")
                nogui()
            print("Checking input 2 validity...  ", end="")
            if os.path.isfile(f2) == True:
                print("Done.  Valid.")
            else:
                print("\nInvalid path for: input 2...")
                print("Restarting...")
                input("Press ENTER to continue...")
                nogui()
            print("""
Enter the number corresponding to the hash algorithm you want to use...
[-- Options --]
    1 ------ md5
    2 ------ sha1
    3 ------ sha224
    4 ------ sha256 <-- Most commonly used.
    5 ------ sha384
    6 ------ sha512 <-- Most secure.

            """)
            ch = alphagamelib.intInput(1, 6)
            print("Loading hasher objects...  ", end="")
            if ch == 1:
                hasher_f1 = hashlib.md5()
                hasher_f2 = hashlib.md5()
            elif ch == 2:
                hasher_f1 = hashlib.sha1()
                hasher_f2 = hashlib.sha1()
            elif ch == 3:
                hasher_f1 = hashlib.sha224()
                hasher_f2 = hashlib.sha224()
            elif ch == 4:
                hasher_f1 = hashlib.sha256()
                hasher_f2 = hashlib.sha256()
            elif ch == 5:
                hasher_f1 = hashlib.sha384()
                hasher_f2 = hashlib.sha384()
            elif ch == 6:
                hasher_f1 = hashlib.sha512()
                hasher_f2 = hashlib.sha512()
            print("Done.")
            with open(f1, 'rb') as f: f1_b = f.read()
            with open(f2, 'rb') as f: f2_b = f.read()
            hasher_f1.update(f1_b)
            hasher_f2.update(f2_b)
            f1_h = hasher_f1.hexdigest()
            h2_h = hasher_f2.hexdigest()
            print("Checksum for file 1: " + str(f1_h))
            print("Checksum for file 2: " + str(f2_h))
            if f1_h == f2_h:
                print("Result: Match.")
            else:
                print("Result: No match.")
            print("Restarting...")
            input("Press ENTER to continue...")
            nogui()
    elif ch == 5:
        alphagamelib.clear()
        print("The GUI mode is actively being worked on...")
        input("Press ENTER to continue...")
        alphagamelib.clear()
        nogui()
    elif ch == 6:
        exit(0)

#   Okay, so the rest of the functions are for Tcl/Tk, as tkinter buttons only support functions to execute.
#   So, what can you do? ¯\_(ツ)_/¯
#   When the imposter is suuuus!!! ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ

#def setIcon(screen):
#    """Sets a Tcl/Tk icon (Used to set the Hydra icon.)"""
#    _, ICON_PATH = tempfile.mkstemp()  #Since <tempfile.mkstemp()> returns tuple; <_> is unused.
#    with open(ICON_PATH, 'wb') as icon_file:
#        icon_file.write(icon._ICON)
#    screen.iconbitmap(default=ICON_PATH)

#I ended there for the GUI mode; I am still working on it. ;)

if __name__ == "__main__":
    try:
        nogui()
    except Exception as err:
        alphagamelib.clear()
        print("Error!")
        print(err)