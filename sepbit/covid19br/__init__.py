"""
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
"""

__author__ = 'Vitor Guia <contato@vitor.guia.nom.br>'
__credits__ = 'https://gitlab.com/sepbit/covid19br'

from .world import world
from .brazil import brazil
from .br_utils import br_date, br_mask

__all__ = ['world', 'brazil', 'br_date', 'br_mask']
