#1
a = 5
print(str(a), type(str(a)))
#2
print("Unicode of character \'m\' is {}".format(ord('m')))
#3
print("Character of unicode \'100\' is {}".format(chr(100)))
#4
print(5,bin(5))
#5
print(10,oct(10))
#6
print(15,hex(15))
#7
a = "0b1100101"
print("{} in decimal format is {}".format(a,int(a,2)))
#8
a = "0x2F"
print("{} in octal format is {}".format(a,oct(int(a,16))))
#9
a = "0o125"
print("{} in binary format is {}".format(a,bin(int(a,8))))
#10
a,b = "0o25", "0x39"
print(bin(int(a,8)+int(b,16)))