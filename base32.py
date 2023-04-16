//insertone kodin qetu






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
