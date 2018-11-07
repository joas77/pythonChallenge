# solution to challenge 1 in
# http://www.pythonchallenge.com/pc/def/map.html

encoded_msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def decode(c):
    not_chars = " '.,()/?"
    decoded_sym = ""
    if c in not_chars:
        decoded_sym = c
    elif c == "y":
        decoded_sym = "a"
    elif c == "z":
        decoded_sym = "b"
    else:
        decoded_sym = chr( ord(c) + 2 )

    return decoded_sym


def decode_msg(msg):
    decoded_msg = map(decode, msg)
    return "".join(decoded_msg)


print( decode_msg(encoded_msg) )

url = "http://www.pythonchallenge.com/pc/def/map.html"

print("applying function to url string...")
print( decode_msg(url) )
