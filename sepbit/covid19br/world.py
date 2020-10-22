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

import configparser
import json
from urllib.request import Request, urlopen
from mastodon import Mastodon
from .br_utils import br_date, br_mask

def world(file_config):
    """
    World report
    """
    config = configparser.ConfigParser()
    config.read(file_config)

    endpoint = config['GENERAL']['endpoint'] + '/all'
    req = Request(endpoint, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as res:
        res = res.read()

    obj = json.loads(res)

    report = "Atualização: " + br_date(obj['updated'])
    report += "\nCasos: " + br_mask(obj['cases'])
    report += "\nCasos hoje: " + br_mask(obj['todayCases'])
    report += "\nMortes: " + br_mask(obj['deaths'])
    report += "\nMortes hoje: " + br_mask(obj['todayDeaths'])
    report += "\nRecuperados: " + br_mask(obj['recovered'])
    report += "\nAtivos: " + br_mask(obj['active'])
    report += "\nCríticos: " + br_mask(obj['critical'])
    report += "\nCasos por um milhão: " + str(obj['casesPerOneMillion'])
    report += "\nMortes por um milhão: " + str(obj['deathsPerOneMillion'])
    report += "\nTestes: " + br_mask(obj['tests'])
    report += "\nTestes por um milhão: " + str(obj['testsPerOneMillion'])
    report += "\nPaíses afetados: " + br_mask(obj['affectedCountries'])
    report += "\n\n#bot #covid #COVID19 #coronavirus"

    mastodon = Mastodon(
        access_token=config['MASTODON']['access_token'],
        api_base_url=config['MASTODON']['api_base_url']
    )
    mastodon.status_post(report, spoiler_text='Atualização COVID-19 Mundo')
