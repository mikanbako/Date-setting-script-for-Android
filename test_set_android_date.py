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

import unittest
import time
import calendar
import set_android_date

class TestParsingDate(unittest.TestCase):
    u"""
    Test parsing string to seconds from the UNIX epoch.
    """

    def test_invalid_date(self):
        u"""
        Test when invalid date.

        ValueError is thrown.
        """
        with self.assertRaises(ValueError):
            set_android_date.parse_date('abcde')

    @classmethod
    def get_current_time(cls):
        u"""
        Get the current time (seconds).
        """
        return int(time.time())

    def test_now(self):
        u"""
        Test parsing a string that represents now.

        Seconds represents parsing time.
        """
        previous_called_time = self.get_current_time()
        seconds = set_android_date.parse_date(set_android_date.DATE_NOW)
        after_called_time = self.get_current_time()

        self.assertTrue(previous_called_time <= seconds) 
        self.assertTrue(seconds <= after_called_time)

    @classmethod
    def convert_to_string(cls, seconds, date_format):
        u"""
        Convert seconds to a string that represents its date.
        """
        return time.strftime(date_format, time.gmtime(seconds))

    def check_converting_seconds(self, date_string, date_format):
        u"""
        Check a string that represents date and its converted seconds
        are equal.
        """
        seconds = set_android_date.parse_date(date_string)
        
        self.assertEquals(date_string,
                self.convert_to_string(seconds, date_format))

    def test_date_yyyymmdd_hhmmss(self):
        u"""
        Test with a date that is formatted "YYYYMMDD.hhmmss".
        """
        self.check_converting_seconds(
                '20110510.020202', set_android_date.DATE_FORMAT_FULL)

    def test_date_yyyymmdd_hhmm(self):
        u"""
        Test with a date that is formatted "YYYYMMDD.hhmm".
        """
        self.check_converting_seconds(
                '20110510.0202', set_android_date.DATE_FORMAT_WITHOUT_SECONDS)

    def test_date_yyyymmdd_hh(self):
        u"""
        Test with a date that is formatted "YYYYMMDD.hh".

        ValueError is thrown because its format is invalid.
        """
        with self.assertRaises(ValueError):
            set_android_date.parse_date('20110510.02')

if __name__ == '__main__':
    unittest.main()

