FILE = 'animdata.txt'

MAX  = 50*1024  # 50Kb  - max chapter size
BUF  = 50*1024*1024  # 50Mb   - memory buffer size

chapters = 0
uglybuf  = ''
with open(FILE, 'rb') as src:
  while True:
    tgt = open(FILE + '.%03d' % chapters, 'wb')
    written = 0
    while written < MAX:
      if len(uglybuf) > 0:
        tgt.write(uglybuf)
      tgt.write(src.read(min(BUF, MAX - written)))
      written += min(BUF, MAX - written)
      uglybuf = src.read(1)
      if len(uglybuf) == 0:
        break
    tgt.close()
    if len(uglybuf) == 0:
      break
    chapters += 1