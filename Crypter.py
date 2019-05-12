def write_to_file(filename, cryptoFn, buffer_size=16):
    with open(filename, 'r+b') as _file:
        raw_value = _file.read(buffer_size)
        while raw_value:
            ciphered_value = cryptoFn(raw_value)
            #COMPARA O TAMANHO DO BLOCO

            if (len(raw_value) != len(ciphered_value)):
                raise ValueError('O valor cifrado {} é diferente do valor plano: {}'.format(len(ciphered_value), len(raw_value)))

                _file.seek(- len(raw_value), 1)
                _file.write(ciphered_value)
                raw_value = _file.read(buffer_size)


    
