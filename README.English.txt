A script that sets time to Android device.

NOTICE:
This script can be executed with the device that can launch its shell on
its root permission.

1. How to use.

  1. Connect Android device to PC.

  2. Open a console on PC.
    
  3. If you set the current time to the devide, execute the below on
     the console.
     (These example are on bash)

    ./set_android_date.py now

     If you set the time to the device, execute the below on the console.
     (This example set time as 2011/05/19 23:57 on PC)

    ./set_android_date.py 20110519.2357

  For detail, execute the below.
  
    ./set_android_date.py -h

2. Requires

  This script requires the below softwares.

  * Python 2.7 (http://www.python.org/)
  * Android SDK (http://developer.android.com/sdk/)

  PATH environment variable must contain the path of the directory tha has "adb"
  in Android SDK.

3. Limitation

  1. This script cannot set time zone on the device.

  2. On Android emurator, this script set the time but the console displays
     "settimeofday failed Invalid argument".

