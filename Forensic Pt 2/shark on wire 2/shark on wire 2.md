# Segundo parcial

## Descripcion

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.

## Pistas (Si hay)



## Solución

``` Bash

Terminal 1



Terminal 2

┌──(root㉿kali)-[~]
└─# python3 -m pip install scapy
Requirement already satisfied: scapy in /usr/lib/python3/dist-packages (2.4.4)
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
                                                                                                                     
┌──(root㉿kali)-[~]
└─# nano exp.py                 
                                                                                                                     
┌──(root㉿kali)-[~]
└─# cd ..     
                                                                                                                     
┌──(root㉿kali)-[/]
└─# cd home/kali/picoCTF/Forensic\ Pt\ 2/shark\ on\ wire\ 2 
                                                                                                                     
┌──(root㉿kali)-[/home/kali/picoCTF/Forensic Pt 2/shark on wire 2]
└─# nano exp.py
                                                                                                                     
┌──(root㉿kali)-[/home/kali/picoCTF/Forensic Pt 2/shark on wire 2]
└─# python3 exp.py                                         
<capture.pcap: TCP:138 UDP:614 ICMP:0 Other:574>
                                                                                                                     
┌──(root㉿kali)-[/home/kali/picoCTF/Forensic Pt 2/shark on wire 2]
└─# nano exp.py                                            
                                                                                                                     
┌──(root㉿kali)-[/home/kali/picoCTF/Forensic Pt 2/shark on wire 2]
└─# nano exp.py
                                                                                                                     
┌──(root㉿kali)-[/home/kali/picoCTF/Forensic Pt 2/shark on wire 2]
└─# nano exp.py   
                                                                                                                     
┌──(root㉿kali)-[/home/kali/picoCTF/Forensic Pt 2/shark on wire 2]
└─# nano exp.py   
                                                                                                                     
┌──(root㉿kali)-[/home/kali/picoCTF/Forensic Pt 2/shark on wire 2]
└─# python3 exp.py
picoCTF{p1LLf3r3d_data_v1a_st3g0}

```

## Referencias