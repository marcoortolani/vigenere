def casear_encrypt(text, shift):
    # Simple Caesar cipher example
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts plaintext using the Vigenère cipher with the given key.
    """
    return _vig(plaintext, key, mode="encrypt")


def decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts ciphertext using the Vigenère cipher with the given key.
    """
    return _vig(ciphertext, key, mode="decrypt")


def _vig(text: str, key: str, mode: str) -> str:
    """
    Core Vigenère cipher logic.

    Args:
        text (str): Input text (plaintext or ciphertext).
        key (str): The encryption/decryption key.
        mode (str): Either 'encrypt' or 'decrypt'.

    Returns:
        str: Transformed text.
    """
    result = []
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % key_length]) - ord('a')

            if mode == "decrypt":
                shift = -shift

            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)

            key_index += 1
        else:
            result.append(char)

    return ''.join(result)

