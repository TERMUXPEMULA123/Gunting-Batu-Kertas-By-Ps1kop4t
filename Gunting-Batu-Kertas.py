#!/bin/python
#coding:utf-8

# module/library
import sys, random
from os import system
from time import sleep as s

# slow print
def sl(a):
  for e in a+'\n':
    sys.stdout.write(e)
    sys.stdout.flush()
    s(0.06)

if sys.version_info.major<3:
  sl('Tools ini menggunakan python 3');s(1)
  sl('Jalankan: python main.py');s(1);exit()

def nanya():
  nanya=input(' {?} Mau main lagi?[Y/T]: ')
  if nanya=='y' or nanya=='Y':
    game()
  elif nanya=='t' or nanya=='T':
    exit();
  else:
    print(f'Tidak ada pilihan {nanya}')

def game():
  system('clear')
  print('            [ By MR PS1KOP4T ]')
  print('+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+')
  print(' {1} Batu')
  print(' {2} Gunting')
  print(' {3} Kertas')
  print('+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+')
  pil=input(' {+} Pilih: ')
  kom=random.choice(['batu','gunting','kertas'])
  if pil=='1':
    print(' {•} Kamu     : batu')
    print(' {•} Komputer :',kom)
    if kom=='batu':
      print(' {•} Imbang')
    if kom=='gunting':
      print(' {√} Kamu menang')
    if kom=='kertas':
      print(' {×}Kamu kalah')
    nanya()
  elif pil=='2':
    print(' {•} Kamu     : gunting')
    print(' {•} Komputer :',kom)
    if kom=='batu':
      print(' {×} Kamu kalah')
    if kom=='gunting':
      print(' {•} Imbang')
    if kom=='kertas':
      print(' {√} Kamu menang')
    nanya()
  elif pil=='3':
    print(' {•} Kamu     : kertas')
    print(' {•} Komputer :',kom)
    if kom=='batu':
      print(' {√} Kamu menang')
    if kom=='gunting':
      print(' {×} Kamu kalah')
    if kom=='kertas':
      print(' {•} Imbang')
    nanya()
if __name__=='__main__':
  game()
# kopiraig bai Rendi Noober
