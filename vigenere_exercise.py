def vig_exe_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts plaintext using the Vigenère cipher with the given key.

    Args:
        plaintext (str): Input text (plaintext).
        key (str): The encryption key.

    Returns:
        str: Transformed text.
    """
    result = []
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % key_length]) - ord('a')

            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)

            key_index += 1
        else:
            result.append(char)

    return ''.join(result)

def vig_exe_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts ciphertext using the Vigenère cipher with the given key.

    Args:
        ciphertext (str): Input text (ciphertext).
        key (str): The decryption key.

    Returns:
        str: Transformed text.
    """
    return ciphertext