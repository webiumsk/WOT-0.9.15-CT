# 2016.05.01 15:29:54 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/encodings/cp869.py
""" Python Character Mapping Codec generated from 'VENDORS/MICSFT/PC/CP869.TXT' with gencodec.py.

"""
import codecs

class Codec(codecs.Codec):

    def encode(self, input, errors = 'strict'):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors = 'strict'):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return codecs.charmap_encode(input, self.errors, encoding_map)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final = False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='cp869', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({128: None,
 129: None,
 130: None,
 131: None,
 132: None,
 133: None,
 134: 902,
 135: None,
 136: 183,
 137: 172,
 138: 166,
 139: 8216,
 140: 8217,
 141: 904,
 142: 8213,
 143: 905,
 144: 906,
 145: 938,
 146: 908,
 147: None,
 148: None,
 149: 910,
 150: 939,
 151: 169,
 152: 911,
 153: 178,
 154: 179,
 155: 940,
 156: 163,
 157: 941,
 158: 942,
 159: 943,
 160: 970,
 161: 912,
 162: 972,
 163: 973,
 164: 913,
 165: 914,
 166: 915,
 167: 916,
 168: 917,
 169: 918,
 170: 919,
 171: 189,
 172: 920,
 173: 921,
 174: 171,
 175: 187,
 176: 9617,
 177: 9618,
 178: 9619,
 179: 9474,
 180: 9508,
 181: 922,
 182: 923,
 183: 924,
 184: 925,
 185: 9571,
 186: 9553,
 187: 9559,
 188: 9565,
 189: 926,
 190: 927,
 191: 9488,
 192: 9492,
 193: 9524,
 194: 9516,
 195: 9500,
 196: 9472,
 197: 9532,
 198: 928,
 199: 929,
 200: 9562,
 201: 9556,
 202: 9577,
 203: 9574,
 204: 9568,
 205: 9552,
 206: 9580,
 207: 931,
 208: 932,
 209: 933,
 210: 934,
 211: 935,
 212: 936,
 213: 937,
 214: 945,
 215: 946,
 216: 947,
 217: 9496,
 218: 9484,
 219: 9608,
 220: 9604,
 221: 948,
 222: 949,
 223: 9600,
 224: 950,
 225: 951,
 226: 952,
 227: 953,
 228: 954,
 229: 955,
 230: 956,
 231: 957,
 232: 958,
 233: 959,
 234: 960,
 235: 961,
 236: 963,
 237: 962,
 238: 964,
 239: 900,
 240: 173,
 241: 177,
 242: 965,
 243: 966,
 244: 967,
 245: 167,
 246: 968,
 247: 901,
 248: 176,
 249: 168,
 250: 969,
 251: 971,
 252: 944,
 253: 974,
 254: 9632,
 255: 160})
decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\ufffe\ufffe\ufffe\ufffe\ufffe\ufffe\u0386\ufffe\xb7\xac\xa6\u2018\u2019\u0388\u2015\u0389\u038a\u03aa\u038c\ufffe\ufffe\u038e\u03ab\xa9\u038f\xb2\xb3\u03ac\xa3\u03ad\u03ae\u03af\u03ca\u0390\u03cc\u03cd\u0391\u0392\u0393\u0394\u0395\u0396\u0397\xbd\u0398\u0399\xab\xbb\u2591\u2592\u2593\u2502\u2524\u039a\u039b\u039c\u039d\u2563\u2551\u2557\u255d\u039e\u039f\u2510\u2514\u2534\u252c\u251c\u2500\u253c\u03a0\u03a1\u255a\u2554\u2569\u2566\u2560\u2550\u256c\u03a3\u03a4\u03a5\u03a6\u03a7\u03a8\u03a9\u03b1\u03b2\u03b3\u2518\u250c\u2588\u2584\u03b4\u03b5\u2580\u03b6\u03b7\u03b8\u03b9\u03ba\u03bb\u03bc\u03bd\u03be\u03bf\u03c0\u03c1\u03c3\u03c2\u03c4\u0384\xad\xb1\u03c5\u03c6\u03c7\xa7\u03c8\u0385\xb0\xa8\u03c9\u03cb\u03b0\u03ce\u25a0\xa0'
encoding_map = {0: 0,
 1: 1,
 2: 2,
 3: 3,
 4: 4,
 5: 5,
 6: 6,
 7: 7,
 8: 8,
 9: 9,
 10: 10,
 11: 11,
 12: 12,
 13: 13,
 14: 14,
 15: 15,
 16: 16,
 17: 17,
 18: 18,
 19: 19,
 20: 20,
 21: 21,
 22: 22,
 23: 23,
 24: 24,
 25: 25,
 26: 26,
 27: 27,
 28: 28,
 29: 29,
 30: 30,
 31: 31,
 32: 32,
 33: 33,
 34: 34,
 35: 35,
 36: 36,
 37: 37,
 38: 38,
 39: 39,
 40: 40,
 41: 41,
 42: 42,
 43: 43,
 44: 44,
 45: 45,
 46: 46,
 47: 47,
 48: 48,
 49: 49,
 50: 50,
 51: 51,
 52: 52,
 53: 53,
 54: 54,
 55: 55,
 56: 56,
 57: 57,
 58: 58,
 59: 59,
 60: 60,
 61: 61,
 62: 62,
 63: 63,
 64: 64,
 65: 65,
 66: 66,
 67: 67,
 68: 68,
 69: 69,
 70: 70,
 71: 71,
 72: 72,
 73: 73,
 74: 74,
 75: 75,
 76: 76,
 77: 77,
 78: 78,
 79: 79,
 80: 80,
 81: 81,
 82: 82,
 83: 83,
 84: 84,
 85: 85,
 86: 86,
 87: 87,
 88: 88,
 89: 89,
 90: 90,
 91: 91,
 92: 92,
 93: 93,
 94: 94,
 95: 95,
 96: 96,
 97: 97,
 98: 98,
 99: 99,
 100: 100,
 101: 101,
 102: 102,
 103: 103,
 104: 104,
 105: 105,
 106: 106,
 107: 107,
 108: 108,
 109: 109,
 110: 110,
 111: 111,
 112: 112,
 113: 113,
 114: 114,
 115: 115,
 116: 116,
 117: 117,
 118: 118,
 119: 119,
 120: 120,
 121: 121,
 122: 122,
 123: 123,
 124: 124,
 125: 125,
 126: 126,
 127: 127,
 160: 255,
 163: 156,
 166: 138,
 167: 245,
 168: 249,
 169: 151,
 171: 174,
 172: 137,
 173: 240,
 176: 248,
 177: 241,
 178: 153,
 179: 154,
 183: 136,
 187: 175,
 189: 171,
 900: 239,
 901: 247,
 902: 134,
 904: 141,
 905: 143,
 906: 144,
 908: 146,
 910: 149,
 911: 152,
 912: 161,
 913: 164,
 914: 165,
 915: 166,
 916: 167,
 917: 168,
 918: 169,
 919: 170,
 920: 172,
 921: 173,
 922: 181,
 923: 182,
 924: 183,
 925: 184,
 926: 189,
 927: 190,
 928: 198,
 929: 199,
 931: 207,
 932: 208,
 933: 209,
 934: 210,
 935: 211,
 936: 212,
 937: 213,
 938: 145,
 939: 150,
 940: 155,
 941: 157,
 942: 158,
 943: 159,
 944: 252,
 945: 214,
 946: 215,
 947: 216,
 948: 221,
 949: 222,
 950: 224,
 951: 225,
 952: 226,
 953: 227,
 954: 228,
 955: 229,
 956: 230,
 957: 231,
 958: 232,
 959: 233,
 960: 234,
 961: 235,
 962: 237,
 963: 236,
 964: 238,
 965: 242,
 966: 243,
 967: 244,
 968: 246,
 969: 250,
 970: 160,
 971: 251,
 972: 162,
 973: 163,
 974: 253,
 8213: 142,
 8216: 139,
 8217: 140,
 9472: 196,
 9474: 179,
 9484: 218,
 9488: 191,
 9492: 192,
 9496: 217,
 9500: 195,
 9508: 180,
 9516: 194,
 9524: 193,
 9532: 197,
 9552: 205,
 9553: 186,
 9556: 201,
 9559: 187,
 9562: 200,
 9565: 188,
 9568: 204,
 9571: 185,
 9574: 203,
 9577: 202,
 9580: 206,
 9600: 223,
 9604: 220,
 9608: 219,
 9617: 176,
 9618: 177,
 9619: 178,
 9632: 254}
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\encodings\cp869.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:29:54 St�edn� Evropa (letn� �as)
