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

import json
from urllib.request import Request, urlopen
from sepbit.covid19br.br_utils import br_date, br_money

def brazil():
    '''
    Brazil report
    See https://disease.sh
    '''
    req = Request(
        'https://disease.sh/v3/covid-19/countries/brazil',
        headers={
            'User-Agent': 'Mozilla/5.0'
        }
    )
    with urlopen(req) as res:
        res = res.read()

    obj = json.loads(res)

    report = 'Atualização: ' + br_date(obj['updated'])
    report += '\nCasos: ' + br_money(obj['cases'])
    report += '\nCasos hoje: ' + br_money(obj['todayCases'])
    report += '\nMortes: ' + br_money(obj['deaths'])
    report += '\nMortes hoje: ' + br_money(obj['todayDeaths'])
    report += '\nRecuperados: ' + br_money(obj['recovered'])
    report += '\nAtivos: ' + br_money(obj['active'])
    report += '\nCríticos: ' + br_money(obj['critical'])
    report += '\nCasos por um milhão: ' + str(obj['casesPerOneMillion'])
    report += '\nMortes por um milhão: ' + str(obj['deathsPerOneMillion'])
    report += '\nTestes: ' + br_money(obj['tests'])
    report += '\nTestes por um milhão: ' + str(obj['testsPerOneMillion'])
    report += '\n\n#bot #covid #COVID19 #coronavirus #Brasil'

    return report


def world():
    '''
    World report
    '''
    req = Request(
        'https://disease.sh/v3/covid-19/all',
        headers={
            'User-Agent': 'Mozilla/5.0'
        }
    )
    with urlopen(req) as res:
        res = res.read()

    obj = json.loads(res)

    report = 'Atualização: ' + br_date(obj['updated'])
    report += '\nCasos: ' + br_money(obj['cases'])
    report += '\nCasos hoje: ' + br_money(obj['todayCases'])
    report += '\nMortes: ' + br_money(obj['deaths'])
    report += '\nMortes hoje: ' + br_money(obj['todayDeaths'])
    report += '\nRecuperados: ' + br_money(obj['recovered'])
    report += '\nAtivos: ' + br_money(obj['active'])
    report += '\nCríticos: ' + br_money(obj['critical'])
    report += '\nCasos por um milhão: ' + str(obj['casesPerOneMillion'])
    report += '\nMortes por um milhão: ' + str(obj['deathsPerOneMillion'])
    report += '\nTestes: ' + br_money(obj['tests'])
    report += '\nTestes por um milhão: ' + str(obj['testsPerOneMillion'])
    report += '\nPaíses afetados: ' + br_money(obj['affectedCountries'])
    report += '\n\n#bot #covid #COVID19 #coronavirus'

    return report
