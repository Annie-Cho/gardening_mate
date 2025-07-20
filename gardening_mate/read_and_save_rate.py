import spidev
import time
import csv
import datetime

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

# Define start and end time
start_time = datetime.datetime.now()
start_timestamp = start_time.strftime("%Y%m%d_%H:%M:%S")
end_time = start_time + datetime.timedelta(minutes=5)

# Open CSV file
file = open(f"./csv/{start_timestamp}.csv", 'w', newline='\n')

# Read data from MCP3208 chip
def read_adc(channel):
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be 0~7")

    # MCP3208 사양
    # first byte(start bit) = 00000001
    # second byte(single/diff) = 0b1000 = 8(dec)) | channel(max 0b111)  << 4(to MSB)
    # third byte = don't care
    buff = spi.xfer2([1, (0b1000 | channel) << 4, 0])

    # first byte = 유효한 데이터 없음(무시)
    # second byte = buff[1] LSB 4 bit(0x0F) and shift 8 = 4bit
    # third byte =  buff[2](8bit)
    data = ((buff[1] & 0x0F) << 8) | buff[2]
    return data

# 수분값 백분율로 계산하기(data : 0~4095, 4095가 MIN값)
def convert_to_percent(data):
  return 100.0-round(((data*100)/float(4095)),1)

try:
    while True:
        adc_channel = 0
        data = read_adc(adc_channel)
        percent = convert_to_percent(data)
        print(percent)

        # Write on CSV
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        row = [timestamp,str(percent)]
        writer = csv.writer(file)
        writer.writerow(row)

        # after 1minutes, finish communication
        if now >= end_time:
            spi.close()
            file.close()
            break;

        time.sleep(3)
except KeyboardInterrupt:
    spi.close()
    file.close()
    print("Keyboard Interrupted")