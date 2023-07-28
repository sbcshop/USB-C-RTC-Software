# USB-C-RTC-Software

<img src ="https://github.com/sbcshop/USB-C-RTC-Software/blob/main/images/USB_C_RTC_BANNER.png"   />

The USB-C-RTC is a highly advanced device featuring an integrated DS3231 circuit; MCP2221, a USB-to-UART/I2C serial converter, which enables USB connectivity, in the processes that include a USB, UART(Serial), GPIO, and I2C interfaces & a C type USB which enables the user for the reversible plugin.
### Features
- DS3231; extremely accurate I2C real-time clock (RTC).
- MCP2221; USB to I2C/UART converter.
- Reversible Plugin.
- Integrated temperature-compensated crystal oscillator (TCXO)
- Incorporates a battery input of CR1220, 3v
- 16-pin, 300-mil SO package
- Automated Backup Power Supply
- Fast (400kHz) I2C Interface

### Specifications
- Accuracy ±2 ppm and ±3.5ppm respectively from 0°C to +40°C and from -40°C to +85°C.
- Digital Temp Sensor Output: ±3°C Accuracy
- Operating voltage of RTC: 2.3V -5.5V.
- Supply Voltage: 5V
- Operating Temperature Ranges: -40°C to +85°C
- Fast (400kHz) I2C Interface

### Pin Out
<img src ="https://github.com/sbcshop/USB-C-RTC-Software/blob/main/images/pinout.jpg"   />

__1) MCP2221__  

**2) Power LED**
     
**3) Type C USB**
   
**4) DS3231 RTC**
   
**5) Battery Holder**


## Getting Started

### Installation on Raspberry Pi

* Install the MCP2221 Library by running the below command on the terminal:

``` 
sudo pip3 install PyMCP2221A
```
              
* Connect USB-C-RTC to the USB Port of Raspberry Pi.
* Now clone/download USB-C-RTC Github Repository by running the below command:

```
git clone https://github.com/sbcshop/USB-C-RTC-Software
```

* Now, open the downloaded folder from home/pi or by running the below command:

``` 
cd USB-C-RTC-Software/examples
```

* Now run test.py file by running below command(Note : sudo should be added before running the file):

```
sudo python3 test.py
```

## Installation on Windows

* Install the MCP2221 Library by running the below command on the terminal:

``` 
pip install PyMCP2221A
```
              
* Connect USB-C-RTC to the USB Port of Windows USB Port.

* Now clone/download USB-C-RTC-Software Github Repository by running the below command:

```
git clone https://github.com/sbcshop/USB-C-RTC-Software
```

* By running the above command, this repository's folder (USB-C-RTC-Software) will be downloaded into your System.

* Now open the downloaded folder and run the test.py file by running the below command:

```python3 test.py ``` or directly run test.py in any python-supported IDE (like Thonny).

### Demo Examples
You may implement various [example](https://github.com/sbcshop/USB-C-RTC-Software/tree/main/examples) codes from the example folder like :
Some are given Below:

- **[Set time](https://github.com/sbcshop/USB-C-RTC-Software/blob/main/examples/Set_Time.py)**
  
- **[Temeparture Data](https://github.com/sbcshop/USB-C-RTC-Software/blob/main/examples/Temperature_data.py)**
  
Note: 
To modify Date & Time in Set Time example, **you have to change the last value of each line in hexadecimal form inside** 
```
def SetTime(address):
```
For Example : 
``` 
bus.write_byte_data(0x68, 0x00, 0x02) # set seconds and start clock
```
it will set second value as 02 second after executing function. 
```
SetTime(address)
```
To read time , you can call given Function.
```
ReadTime(address)
``` 
### Resources
- [SCHEMATIC](https://github.com/sbcshop/USB-C-RTC-Hardware/blob/main/Design%20Data/Schematic.pdf)

- [HARDWARE FILES](https://github.com/sbcshop/USB-C-RTC-Hardware)

- [STEP FILE](https://github.com/sbcshop/USB-C-RTC-Hardware/blob/main/Mechanical%20Data/Step%20File%20.step)

- [DS3231 RTC](https://github.com/sbcshop/USB-C-RTC-Software/blob/main/Documents/DS3231.pdf)

- [MCP2221 USB to I2C/UART Converter](https://github.com/sbcshop/USB-C-RTC-Software/blob/main/Documents/MCP2221.pdf)
  
## Related Products
* [USB RTC](https://shop.sb-components.co.uk/products/usb-rtc-for-raspberry-pi-1)

  <img src ="https://shop.sb-components.co.uk/cdn/shop/products/2_ad2ee31c-71ef-44dc-82d0-986541b065e5.jpg?v=1665636610"  width="400" />
  
* [SquaryPi](https://shop.sb-components.co.uk/products/squary?variant=40443840921683)

 ![SquaryPi](https://cdn.shopify.com/s/files/1/1217/2104/products/1_5874b3b5-2a2f-453e-bf54-abbf2a26acb9.png?v=1670307456&width=400)

* [EncroPi](https://shop.sb-components.co.uk/products/encropi?_pos=1&_sid=95f822d26&_ss=r)

 ![EncroPi](https://cdn.shopify.com/s/files/1/1217/2104/products/03_a6b155c1-da03-427d-ba6a-44730c56d73f.png?v=1668595812&width=400)

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>

