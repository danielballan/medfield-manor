# CircuitPython NeoPixel Color Picker Example

import board
import neopixel

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket 
# from adafruit_bluefruit_connect.button_packet import ButtonPacket

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
uart_service = UARTService()
advertisement = ProvideServicesAdvertisement(uart_service)

pixels = neopixel.NeoPixel(board.D6, 4 * 8, brightness=0.1)

import math
import flicker

flicker_gen = flicker.flicker(5)

color = (0, 0, 0)


def f(color, pixels):
    flicker_brightness = next(flicker_gen)
    color_ = tuple(
        [math.ceil(flicker_brightness * ch)
            for ch in color])
    pixels.fill(color_)


while True:
    print('waiting')
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        f(color, pixels)
    ble.stop_advertising()
    print('connected', ble)
    while ble.connected:
        f(color, pixels)
        if uart_service.in_waiting:
            packet = Packet.from_stream(uart_service)
            print('packet', packet)
            if isinstance(packet, ColorPacket):
                color = packet.color
