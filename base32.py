//Arbnora
import base64
def base32_encode(string):
    """Encodes a string to Base32"""
    string_bytes = string.encode('utf-8')
    encoded_bytes = base64.b32encode(string_bytes)
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string






//Xhemajli
def base32_decode(encoded_string):
    """Decodes a Base32-encoded string"""
    encoded_bytes = encoded_string.encode('utf-8')
    decoded_bytes = base64.b32decode(encoded_bytes)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string
//Arditi
encoded_string = base32_encode("Ky eshte projekti i dyte")
print(encoded_string)
//Erblini
decoded_string = base32_decode(encoded_string)
print(decoded_string)
