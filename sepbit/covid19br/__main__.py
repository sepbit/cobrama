#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Covid19BR - Report COVID-19 Brasil on Mastodon
Copyright (C) 2020 Vitor Guia

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
'''

import time
from os import environ
from sepbit.covid19br.mastodon import statuses
from sepbit.covid19br.disease import brazil, world

def main():
    '''
    Entry point
    '''
    environ['TZ'] = 'America/Sao_Paulo'
    time.tzset()

    statuses(
        environ['INSTANCE'],
        environ['TOKEN'],
        data = {
            'spoiler_text' : 'Atualização COVID-19 Brasil',
            'status': brazil(),
            'language': 'por',
            'visibility': 'public'
        }
    )

    statuses(
        environ['INSTANCE'],
        environ['TOKEN'],
        data = {
            'spoiler_text' : 'Atualização COVID-19 Mundo',
            'status': world(),
            'language': 'por',
            'visibility': 'public'
        }
    )


if __name__ == '__main__':
    main()
