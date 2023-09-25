import machine
import ssd1306

# Define pin assignments
scl_pin = machine.Pin(18)  # GPIO 18 for SCL
sda_pin = machine.Pin(19)  # GPIO 19 for SDA
res_pin = machine.Pin(20)  # GPIO 20 for RES
dc_pin = machine.Pin(21)   # GPIO 21 for DC
cs_pin = machine.Pin(22)   # GPIO 22 for CS

spi = machine.SPI(0, baudrate=8000000, sck=scl_pin, mosi=sda_pin)

oled = ssd1306.SSD1306_SPI(128, 64, spi, dc_pin, res_pin, cs_pin)

oled.fill(1)
oled.show()

padding_left = 3

oled.text("Automate Africa", padding_left, 10, 0)
oled.text("Efficiency", padding_left, 30, 0)
oled.text("Productivity", padding_left, 40, 0)
oled.show()