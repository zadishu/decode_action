
import base64, zlib, lzma, bz2, gzip
exec((lambda cjR:compile(cjR,'<string>','exec'))(zlib.decompress(lzma.decompress(bz2.decompress(gzip.decompress(base64.b64decode('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'))))).decode()))
