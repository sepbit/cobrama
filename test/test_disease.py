"""
Cobrama - Estatísticas da COVID-19 no Brasil para Mastodon
Copyright (C) 2020-2022  Vitor Guia

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

import unittest
from sepbit.cobrama.disease import brazil, world, mask_date, mask_money


class DiseaseTest(unittest.TestCase):
    """
    Test disease module
    """

    def test_mask_date(self):
        """
        Test mask_date function
        """
        self.assertEqual(mask_date(1603547325550), '24/10/2020 13:48:45')


    def test_mask_money(self):
        """
        Test mask_money function
        """
        self.assertEqual(mask_money(5355650), '5.355.650')


    def test_brazil(self):
        """
        Test brazil function
        """
        self.assertTrue(brazil())


    def test_world(self):
        """
        Test world function
        """
        self.assertTrue(world())


if __name__ == '__main__':
    unittest.main()
