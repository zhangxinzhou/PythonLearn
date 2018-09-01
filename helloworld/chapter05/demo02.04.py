verse = '野人无人舟自横'
code = 'GBK'
byte = verse.encode(code)
decode = byte.decode(code)
print("源字符串:" + verse)
print("转换后:", byte)
print("解码后:", decode)
