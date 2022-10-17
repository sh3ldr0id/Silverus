from base64 import b64encode

Silverus = open("Main.py", "r").read().encode()

obfSilverus = b64encode(
    Silverus
)

open(
    "Silverus.py",
    "w"
).write(
    "from base64 import b64decode"
    f"\neval(compile(b64decode({obfSilverus}).decode(), '<string>', 'exec'))"
)