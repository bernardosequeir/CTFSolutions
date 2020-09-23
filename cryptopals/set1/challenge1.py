from enum import Enum

b64_encoding_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


class Status(Enum):
    """Represents possible status of the converter"""
    START_NEW = 0
    TAKE_2 = 1
    TAKE_4 = 2


def hex_to_b64(hexdata):
    """returns b64 of hex str"""
    b64data = ""  # Encoding to return

    sixbits = 0
    status = Status.START_NEW

    for hexchar in hexdata:
        dec = int(hexchar, 16)

        if status == Status.START_NEW:
            sixbits = dec
            status = Status.TAKE_2
        elif status == Status.TAKE_2:
            sixbits = (sixbits << 2) | (dec >> 2)
            b64data += b64_encoding_table[sixbits]
            sixbits = (dec & 0x3)
            status = Status.TAKE_4
        elif status == Status.TAKE_4:
            sixbits = (sixbits << 4) | dec
            b64data += b64_encoding_table[sixbits]
            status = Status.START_NEW
    if status == Status.TAKE_2:
        sixbits <<= 2
        b64data = b64_encoding_table[sixbits]
        b64data += "="
    elif status == Status.TAKE_4:
        sixbits <<= 4
        b64data += b64_encoding_table[sixbits]
        b64data += "=="

    return b64data


def main():
    # Asserting encoding
    assert hex_to_b64(
        "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


if __name__ == "__main__":
    main()
