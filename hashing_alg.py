import hashlib
import random as rd
import string

list_of_strings = []

passwd = ""

def list_str(list_of_strings):
    for x in range(len(string.ascii_letters)):
        list_of_strings.append(string.ascii_letters[x])
    for y in range(1, 11):
        list_of_strings.append(str(y))
    list_of_strings = rd.shuffle(list_of_strings)


def salt_func(l):
    st = ""
    global sl
    sl = ""
    for i in range(5):
        st = rd.choice(l)
        sl = sl + st


def passwd_hash(passwd):
    global hashed_passwd
    list_str(list_of_strings)
    salt_func(list_of_strings)
    if bool(rd.getrandbits(1)) == True:
        passwd += sl
    elif bool(rd.getrandbits(1)) == False:
        passwd = sl + passwd
    hashed_passwd = hashlib.sha512(bytes(passwd, 'utf8')).hexdigest()
    passwd = None
    return hashed_passwd

passwd_hash(passwd)
