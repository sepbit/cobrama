#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

import os
import time
import sys
from sepbit.covid19br import brazil, world

def main():
    """
    Entry point
    """
    os.environ['TZ'] = 'America/Sao_Paulo'
    time.tzset()

    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        print('Covid19BR  Copyright (C) 2020  Sepbit')
        print("This program comes with ABSOLUTELY NO WARRANTY;")
        print('This is free software, and you are welcome to redistribute it')
        print("under certain conditions; See <https://www.gnu.org/licenses/>.")
        print('')
        print('$ covid19br /path/config.ini')
        sys.exit(0)

    elif len(sys.argv) == 2:
        world(sys.argv[1])
        brazil(sys.argv[1])
        sys.exit(0)

    else:
        print('type --help for help')
        sys.exit(0)


if __name__ == '__main__':
    main()
