#!/usr/bin/env python
# -*- coding: utf-8 -*-
# alarmklok version 1.0 stable spesial 1 subscribe :v
# Author by: @pemulabelajar
# My Github: https://github.com/pemulabelajar/alarmklok

import sys, os, subprocess
from time import sleep
from time import strftime as tm

banner = """
\033[93;1m          dP                           dP       dP               dP
\033[93;1m          88                           88       88               88
\033[93;1m .d8888b. 88 .d8888b. d888P d888bd888b 88  .dP  88      .d8888b. 88  .dP
\033[93;1m 88'  `88 88 88'  `88 88    88  88  88 88888"   88      88'  `88 88888"
\033[93;1m 88.  .88 88 88.  .88 88    88  88  88 88  `8b. 88      88.  .88 88  `8b.
\033[93;1m `88888P8 88 `88888P8 88    88  88  88 88   `YP `88888b `888888' 88   `YP

\033[96;1m Version 1.0 dibuat oleh @pemulabelajar ( spesial 1 subscribe ) """

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    os.getcwd()

def loads():
    o = [' .   ',' ..  ',' ... ']
    for i in o:
        print('\r\033[0m[\033[96m●\033[0m] Mengaktifkan alarm'+i,end=''),;sys.stdout.flush();sleep(1)

def start():
    try:
        while True:
            waktu = tm('%I:%M:%S %p')
            if waktu == alarm:
                while True:
                    print()
                    print()
                    print('\033[0m[\033[93;1m^\033[0m] ALARM SUDAH BERBUNYI\033[0m')
                    print()
                    print('\033[0m[\033[101;97;1m Pesan \033[0m] '+messg)
                    print()
                    print('\033[0m[\033[91;1m-\033[0m] Tekan CTRL + C untuk menunda\033[0m\n')
                    subprocess.call('mpv .sound/calm',shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
                    restart()
                    break
            else:
                print('\r\033[0m[\033[92;1m#\033[0m] Sekarang pukul\033[91;1m',waktu,end=''),;sys.stdout.flush();sleep(0.5)
                str(waktu)
    except KeyboardInterrupt:
        print()
        print()
        print('\033[0m[\033[91;1m!\033[0m] \033[97;1mBerhenti\033[0m')
        print()
        sleep(1)
        restart()

if (__name__=='__main__'):
    print(banner)
    print()
    h = input('\033[0m[\033[101;97;1m  Jam  \033[0m] ')
    m = input('\033[0m[\033[103;30;1m Menit \033[0m] ')
    s = input('\033[0m[\033[104;97;1m Detik \033[0m] ')
    print()
    o = input('\033[0mAktifkan format waktu \033[92;1mAM\033[0m / \033[92;1mPM\033[0m: ').upper()
    print()
    messg = input('\033[0m[\033[95;1m+\033[0m] \033[97;1mMasukan pesan: \033[0m')
    alarm = h+':'+m+':'+s+' '+o
    print()
    loads()
    sleep(3)
    os.system('clear')
    print(banner)
    print()
    print('\n\033[0mAlarm di atur pada: \033[92;1m'+h+':'+m+' '+o+' | Tanggal '+tm('%d %B %Y'))
    print()
    start()
