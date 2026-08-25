from bme280 import bme280

I2C_CH = 1
BME280_ADDR = 0x76

bme280.full_setup(I2C_CH, BME280_ADDR)
data = bme280.read_all()

print("Temperature:", round(data.temperature, 2))
print("Humidity:", round(data.humidity, 2))
print("Pressure:", round(data.pressure, 2))