# -*- coding: utf-8 -*-

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

largura = 17
altura  = 12.0

print 'largura/2 = %d' %(largura / 2), type(largura / 2)
print 'largura/2.0 = %2.1f' %(largura / 2.0), type(largura / 2.0)
print 'altura/3 = %d' %(altura / 3), type(altura / 3)
print '4.1 + 2 * 5', type(4.1 + 2 * 5)

