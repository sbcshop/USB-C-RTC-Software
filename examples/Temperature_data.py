from PyMCP2221A import SMBus
import time
import os

# DS3231 I2C address
DS3231_ADDR = 0x68

# DS3231 temperature register address
DS3231_TEMP_REG = 0x11

# Initialize I2C bus
bus = SMBus.SMBus()

def read_ds3231_temperature():
    # Read the temperature register (2 bytes)
    temp_data = bus.read_i2c_block_data(DS3231_ADDR, DS3231_TEMP_REG, 2)

    # Extract temperature data from the received bytes
    temp_integer = temp_data[0]
    temp_fraction = temp_data[1] >> 6  # Only the two most significant bits represent the fractional part

    # Calculate the temperature in Celsius
    temperature = temp_integer + (temp_fraction * 0.25)

    return temperature

try:
    while True:
        temperature = read_ds3231_temperature()
        print(f"Temperature: {temperature:.2f} °C")
        time.sleep(2)

except KeyboardInterrupt:
    print("Measurement stopped by the user.")
