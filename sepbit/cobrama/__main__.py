#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Cobrama - Estatísticas da COVID-19 no Brasil para Mastodon
Copyright (C) 2020-2022 Vitor Guia

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
from sepbit.cobrama.disease import brazil, world
from sepbit.sistamapy.statuses import Statuses


def main():
    '''
    Entry point
    '''
    environ['TZ'] = 'America/Sao_Paulo'
    time.tzset()

    toot = Statuses(
        environ['INSTANCE'],
        environ['TOKEN']
    )

    toot.post({
        'spoiler_text' : 'Atualização COVID-19 Brasil',
        'status': brazil(),
        'language': 'por',
        'visibility': 'public'
    })

    toot.post({
            'spoiler_text' : 'Atualização COVID-19 Mundo',
            'status': world(),
            'language': 'por',
            'visibility': 'public'
    })


if __name__ == '__main__':
    main()
