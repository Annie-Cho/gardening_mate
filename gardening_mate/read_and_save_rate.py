import spidev
import time
import csv
import datetime

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0) #bus, device
spi.max_speed_hz = 1000000

# Open CSV file
start_time = datetime.datetime.now()
start_timestamp = start_time.strftime("%Y%m%d_%H:%M:%S")
end_time = start_time + datetime.timedelta(minutes=1)
file = open(f"./csv/{start_timestamp}.csv", 'w', newline='\n')

# Read data from MCP3208 chip
def read_adc(channel):
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be 0~7")

    # first byte(start bit) = 00000001
    # second byte(single/diff) = 0b1000 = 8(dec)) | channel(max 0b111)  << 4(to MSB)
    # third byte = don't care
    buff = spi.xfer2([1, (0b1000 | channel) << 4, 0])
    # buff[1] LSB 4 bit(0x0F) and shift 8 to or buff[2](8bit)
    data = ((buff[1] & 0x0F) << 8) | buff[2]
    return data

# 0~1023 value가 들어옴. 1023이 수분함량 min값
def convertPercent(data):
  return 100.0-round(((data*100)/float(1023)),1)
  
try:
    while True:
        adc_channel = 0
        data = read_adc(adc_channel)
        percent = convertPercent(data)
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