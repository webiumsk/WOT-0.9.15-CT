# 2016.05.01 15:29:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/encodings/iso2022_jp_2004.py
import _codecs_iso2022, codecs
import _multibytecodec as mbc
codec = _codecs_iso2022.getcodec('iso2022_jp_2004')

class Codec(codecs.Codec):
    encode = codec.encode
    decode = codec.decode


class IncrementalEncoder(mbc.MultibyteIncrementalEncoder, codecs.IncrementalEncoder):
    codec = codec


class IncrementalDecoder(mbc.MultibyteIncrementalDecoder, codecs.IncrementalDecoder):
    codec = codec


class StreamReader(Codec, mbc.MultibyteStreamReader, codecs.StreamReader):
    codec = codec


class StreamWriter(Codec, mbc.MultibyteStreamWriter, codecs.StreamWriter):
    codec = codec


def getregentry():
    return codecs.CodecInfo(name='iso2022_jp_2004', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\encodings\iso2022_jp_2004.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:29:56 St�edn� Evropa (letn� �as)
