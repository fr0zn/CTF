'''
We are given an IP and port. Once connected simple arithmetic operations are
shown in ascii art. The objective is to parse and interpret those operations
and send back the solution to the server. Example:

#        #####           #####
#    #  #     #  #   #  #     #
#    #        #   # #   #     #    #####
#    #   #####  #######  #####
#######       #   # #   #     #    #####
     #  #     #  #   #  #     #
     #   #####           #####
>>> 344
'''

from pwn import *

times = '''
 #   #
  # #
#######
  # #
 #   #


'''

minus = '''

#####




'''

equal = '''

   #####

   #####



'''

plus = '''
  #
  #
#####
  #
  #

'''

zero = '''  ###
 #   #
#     #
#     #
#     #
 #   #
  ###

'''

one = '''  #
 ##
# #
  #
  #
  #
#####

'''

two = ''' #####
#     #
      #
 #####
#
#
#######

'''

three = ''' #####
#     #
      #
 #####
      #
#     #
 #####

'''

four = '''#    #
#    #
#    #
#######
     #
     #

'''

five = '''#######
#
#
######
      #
#     #
 #####

'''

six = ''' #####
#     #
#
######
#     #
#     #
 #####

'''

seven  = '''#######
#    #
    #
   #
  #
  #
  #

'''

eight = ''' #####
#     #
#     #
 #####
#     #
#     #
 #####

'''

nine = ''' #####
#     #
#     #
 ######
      #
#     #
 #####

'''

def split_multiple(s, index):
    return [s[i:j] for i,j in zip(index, index[1:]+[None])]

def get_chunks(text):
    MAX = 50
    chunks = [0]
    lines = text.splitlines()
    is_chunk = True
    for i in range(MAX):
        _maps = []
        for line in lines:
            try:
                _maps.append(line[i])
            except:
                continue
        if len(set(_maps)) <= 1:
            chunks.append(i)

    splited_chunks = []
    for line in lines:
        splited_chunks.append(split_multiple(line, chunks))

    nums = zip(*splited_chunks)

    return nums


DIGITS = []

for num in [zero, one, two ,three, four, five, six, seven,eight, nine]:
    DIGITS.append(num.split('\n'))

DIGITS.append(plus.split('\n'))
DIGITS.append(times.split('\n'))
DIGITS.append(minus.split('\n'))
DIGITS.append(equal.split('\n'))

DIGITS_STR_MAP = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '*', '-', '=']

def most_common (lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]

r = remote('104.154.120.223', 8083)

times =0
while True:
    if times == 100:
        r.recvuntil('Good job, this is your flag:')
        print r.recvuntil('}')
        break

    text = '\n'.join(r.recvuntil('>>>').split('\n')[1:-1])

    print text

    chunks = get_chunks(text)

    op = ''

    for chunk in chunks:
        chunk = list(chunk)
        if len(set(chunk)) <= 1:
            continue
        potential = []
        for cli, chunk_line in enumerate(chunk):
            for numi, num in enumerate(DIGITS):
                if chunk_line.strip() == num[cli].strip():
                    potential.append(numi)
        n = most_common(potential)
        op += DIGITS_STR_MAP[n]

    print op
    result = str(eval(op.replace('=', '')))

    times += 1


    r.sendline(result)

