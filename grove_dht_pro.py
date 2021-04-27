#!/usr/bin/env python
#
# GrovePi Example for using the Grove Temperature & Humidity Sensor Pro 
# (http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor_Pro)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  
# You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
import grovepi
import math
import time
# Grove Temperature & Humidity Sensor Pro を デジタルポート D3 に接続します。
# このサンプルでは、白い色のセンサーを使用しています。
# SIG,NC,VCC,GND
sensor = 3  # センサーの接続先はデジタルポート 3

# temp_humidity_sensor_type
blue = 0    # 青色のセンサーを使用
white = 1   # 白色のセンサーを使用

i = 0

while i < 10:
    try:
        # 第１引数は接続ポート、第２引数はセンサー種別
        [temp,humidity] = grovepi.dht(sensor,white)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity), flush=True)
    except IOError:
        print ("Error")
    finally:
        i += 1
        time.sleep(1)