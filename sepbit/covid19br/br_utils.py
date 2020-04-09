"""
Covid19BR - Report COVID-19 Brasil on Mastodon
Copyright (C) 2020  Sepbit

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import datetime

def br_date(timestamp):
    """
    Set Locale Brazil
    """
    timestamp = datetime.datetime.fromtimestamp(timestamp/1000.0)
    timestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")
    return timestamp

def br_mask(value):
    """
    Mask value
    """
    value = '{:,d}'.format(value)
    return str(value.replace(',', '.'))
