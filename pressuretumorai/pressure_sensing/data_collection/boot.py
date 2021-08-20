# type: ignore

# This file is executed on every boot (including wake-boot from deepsleep)

import uos, machine
import gc
import network

gc.collect()

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('NetZenisys', '45106567711#')
    while not sta_if.isconnected():
        pass
    print('network config:', sta_if.ifconfig())

import network_transmission