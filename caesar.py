def caesar_encrypt(text: str, shift: int) -> str:
    """
    Encrypts the input text using the Caesar cipher.

    Each letter in the text is shifted forward in the alphabet by the specified
    number of positions. Non-alphabetic characters remain unchanged.

    Parameters:
    ----------
    text : str
        The input string to be encrypted.
    shift : int
        The number of positions to shift each letter (positive or negative integer).

    Returns:
    -------
    str
        The encrypted string after applying the Caesar cipher.
    """
    
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text: str, shift: int) -> str:
    """
    Decrypts a Caesar cipher-encrypted string.

    Each letter in the input text is shifted backward in the alphabet by the
    specified number of positions. Non-alphabetic characters remain unchanged.
    Note: Caesar cipher decryption is just encryption with the negative shift

    Parameters:
    ----------
    text : str
        The encrypted string to be decrypted.
    shift : int
        The number of positions originally used to encrypt each letter (positive or negative integer).

    Returns:
    -------
    str
        The decrypted string after reversing the Caesar cipher shift.
    """
        
    return caesar_encrypt(text, -shift)