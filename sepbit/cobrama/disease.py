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

import json
import datetime
from urllib.request import Request, urlopen


def mask_date(timestamp):
    '''
    Mask date
    '''
    timestamp = datetime.datetime.fromtimestamp(timestamp/1000.0)
    timestamp = timestamp.strftime('%d/%m/%Y %H:%M:%S')
    return timestamp


def mask_money(value):
    '''
    Mask money
    '''
    value = '{:,d}'.format(value)
    return str(value.replace(',', '.'))


def brazil():
    '''
    Brazil statistic
    See https://disease.sh
    '''
    request = Request(
        'https://disease.sh/v3/covid-19/countries/brazil',
        headers={
            'User-Agent': 'Mozilla/5.0'
        }
    )
    with urlopen(request) as response:
        response = response.read()

    date = json.loads(response)
    message = 'Atualização: ' + mask_date(date['updated'])
    message += ' UTC\nCasos: ' + mask_money(date['cases'])
    message += '\nCasos hoje: ' + mask_money(date['todayCases'])
    message += '\nMortes: ' + mask_money(date['deaths'])
    message += '\nMortes hoje: ' + mask_money(date['todayDeaths'])
    message += '\nRecuperados: ' + mask_money(date['recovered'])
    message += '\nAtivos: ' + mask_money(date['active'])
    message += '\nCríticos: ' + mask_money(date['critical'])
    message += '\nCasos por um milhão: ' + str(date['casesPerOneMillion'])
    message += '\nMortes por um milhão: ' + str(date['deathsPerOneMillion'])
    message += '\nTestes: ' + mask_money(date['tests'])
    message += '\nTestes por um milhão: ' + str(date['testsPerOneMillion'])
    message += '\n\n#bot #covid #COVID19 #coronavirus #Brasil'
    return message


def world():
    '''
    World statistic
    '''
    request = Request(
        'https://disease.sh/v3/covid-19/all',
        headers={
            'User-Agent': 'Mozilla/5.0'
        }
    )
    with urlopen(request) as response:
        response = response.read()

    date = json.loads(response)
    message = 'Atualização: ' + mask_date(date['updated'])
    message += ' UTC\nCasos: ' + mask_money(date['cases'])
    message += '\nCasos hoje: ' + mask_money(date['todayCases'])
    message += '\nMortes: ' + mask_money(date['deaths'])
    message += '\nMortes hoje: ' + mask_money(date['todayDeaths'])
    message += '\nRecuperados: ' + mask_money(date['recovered'])
    message += '\nAtivos: ' + mask_money(date['active'])
    message += '\nCríticos: ' + mask_money(date['critical'])
    message += '\nCasos por um milhão: ' + str(date['casesPerOneMillion'])
    message += '\nMortes por um milhão: ' + str(date['deathsPerOneMillion'])
    message += '\nTestes: ' + mask_money(date['tests'])
    message += '\nTestes por um milhão: ' + str(date['testsPerOneMillion'])
    message += '\nPaíses afetados: ' + mask_money(date['affectedCountries'])
    message += '\n\n#bot #covid #COVID19 #coronavirus'
    return message
