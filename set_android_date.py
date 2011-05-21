#!/usr/bin/env python

# The MIT License
# 
# Copyright (c) 2011 Keita Kita
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# 
# THE SOFTWARE.

import argparse
import calendar
import re
import time
import subprocess
import sys

# String that represents now.
DATE_NOW = 'now'

# Pattern that represents full date.
DATE_PATTERN_FULL = re.compile(r'\d{4}\d{2}\d{2}\.\d{2}\d{2}\d{2}')

# Format that represents full date.
DATE_FORMAT_FULL = '%Y%m%d.%H%M%S'

# Pattern that represents date without seconds.
DATE_PATTERN_WITHOUT_SECONDS = re.compile(r'\d{4}\d{2}\d{2}\.\d{2}\d{2}')

# Format that represents date without seconds.
DATE_FORMAT_WITHOUT_SECONDS = '%Y%m%d.%H%M'

def parse_date(date_string):
    u"""Parse string that represents date.

    Arguments:
        date_string : String that represents date.
    Return:
        Seconds from the UNIX epoch.
    Throws:
        ValueError : If the date_string does not represents date.
    """
    if date_string == DATE_NOW:
        return int(time.time())
    else:
        if DATE_PATTERN_FULL.match(date_string):
            struct_time = time.strptime(date_string, DATE_FORMAT_FULL)
        elif DATE_PATTERN_WITHOUT_SECONDS.match(date_string):
            struct_time = time.strptime(
                    date_string, DATE_FORMAT_WITHOUT_SECONDS)
        else:
            raise ValueError()

        return calendar.timegm(struct_time)

def set_android_date(seconds):
    u"""
    Set date to current Android device.

    Arguments:
        seconds : Seconds from the UNIX epoch.
    """

    subprocess.call(
            'adb shell su 0 /system/bin/date -u {sec}'.format(sec = seconds),
            shell = True, stderr = subprocess.STDOUT)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('date', help = 'now or YYYYMMDD.hhmm[ss]. ' + \
            'Set the current time if date is now. ' + \
            'Set given date if date is YYYYMMDD.hhmmss. "ss" is optional.')
    parsed_result = parser.parse_args()

    try:
        seconds = parse_date(parsed_result.date)
        set_android_date(seconds)
    except ValueError:
        print 'Invalid date format.'
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()

