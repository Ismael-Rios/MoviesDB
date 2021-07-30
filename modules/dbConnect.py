# -*- coding: utf-8 -*-

import hashlib

def checkCredential(uName, uPass):
    userName = hashlib.md5(uName.encode())
    userPass = hashlib.md5(uPass.encode())
    
    md5 = userName.hexdigest() + ";" + userPass.hexdigest()

    return(md5)
