# Segundo parcial

## Descripcion

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag.

## Pistas (Si hay)

1.- Try using a tool like Wireshark.

2.- How can you decrypt the TLS stream?

## Solución

``` Bash

Nos entregaran una captura de paquetes donde algunos TLS estaran encriptados, abriremos WireShark y editaremos los protocolos de TLS con la llave que nos da en el reto para desencriptar los mismos. Al momento de hacer una busqueda en los detalles de los paquetes encontraremos la llave

picoCTF{nongshim.shrimp.crackers}

```

## Referencias