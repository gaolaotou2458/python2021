import struct
ret = struct.pack('i',1023800976) # i 转成 byte类型  i:int
print(ret,len(ret))

num = struct.unpack('i',ret)
print(num)
