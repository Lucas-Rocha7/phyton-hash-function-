def simple_hash(input_string):
    # Inicializando a variável hash
    hash_value = 0
    
    # Percorre cada caractere da string de entrada
    for i, char in enumerate(input_string):
        # Obtém o valor ASCII do caractere
        ascii_value = ord(char)
        
        # Multiplica o valor ASCII pela posição do caractere na string
        # Faz um cálculo de mod para evitar valores de hash muito grandes
        hash_value = (hash_value + (ascii_value * (i + 1))) % 1000
    
    # Retorna o valor de hash final
    return hash_value

# Testando a função de hash com diferentes entradas
print(f"Hash de 'exemplo': {simple_hash('exemplo')}")
print(f"Hash de 'Hello World': {simple_hash('Hello World')}")
print(f"Hash de 'Cibersegurança': {simple_hash('Cibersegurança')}")
print(f"Hash de 'Segurança de Informação': {simple_hash('Segurança de Informação')}")

import hashlib

def sha256_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

# Testando a funcao SHA-256
print(f"SHA-256 Hash de 'exemplo': {sha256_hash('exemplo')}")