# def Ch3cking(check)
    # check = 0
    # # ISITDTU
    # ord(flag[0]) + 52 == ord(flag[-1])
    # ord(flag[-1]) - 2 == ord(flag[7])
    # flag[:7] == "ISITDTU"
    # flag[9] == flag[14]
    # flag[14] == flag[19]
    # flag[19] == flag[24]
    # flag[8] == 49
    # flag[8] == flag[16]
    # flag[10:14] == 'd0nT'
    # int(flag[18]) + int(flag[23]) + int(flag[28]) == 9
    # flag[18] == flag[28]
    # flag[15] == 'L'
    # ord(flag[17]) ^ -10 == -99  # (0xf6) (0x9d) letter k
    # # 25
    # ord(flag[20]) + 2 == ord(flag[27])
    # ord(flag[27]) < 123 # IF > TRUE bad
    # ord(flag[20]) > 97
    # # 27
    # ord(flag[27]) % 100 == 0

    # # 29
    # flag[25] == 'C'
    # # 31
    # ord(flag[26]) % 2 == 0
    # ord(flag[26]) % 3 == 0
    # ord(flag[26]) % 4 == 0
    # flag[26].isdigit() == True
    # # 33
    # int(flag[23]) == '3'
    # flag[22] == flag[13].lower()
    # # 34

    # tmp = 0
    # for i in flag:
        # tmp += ord(i)

    # tmp == 2441

flag = [' '] * 30


flag[0] = 'I'
flag[1] = 'S'
flag[2] = 'I'
flag[3] = 'T'
flag[4] = 'D'
flag[5] = 'T'
flag[6] = 'U'
flag[7] = '{'
flag[8] = '1'
flag[9] = '_' # NO rule
flag[10] = 'd'
flag[11] = '0'
flag[12] = 'n'
flag[13] = 'T'
flag[14] = '_' # NO rule
flag[15] = 'L'
flag[16] = '1'
flag[17] = 'k'
flag[18] = '3'
flag[19] = '_' # No rule
flag[20] = 'b'

flag[21] = ':' # NO RULE

flag[22] = 't'
flag[23] = '3'
flag[24] = '_' # No rule
flag[25] = 'C'

flag[26] = '0'
flag[27] = 'd'
flag[28] = '3'
flag[29] = '}'

# same

# same

tmp = 0
for i in flag:
    tmp += ord(i)

print tmp

# print flag

print ''.join(flag)




