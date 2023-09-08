from django.test import TestCase
from common.helpers import convert_bytes, replace_quotes


class HelpersTest(TestCase):
    def test_replace_quotes(self):
        """ Test replace quotes """

        req = 'ООО "Производственная компания "ПК"'
        res = replace_quotes(req)
        self.assertEqual(res, 'ООО «Производственная компания «ПК»')

        req = 'ООО Производственная компания "ПК"'
        s = replace_quotes(req)
        self.assertEqual(s, 'ООО Производственная компания «ПК»')

        req = 'ООО Производственная компания ПК'
        s = replace_quotes(req)
        self.assertEqual(s, 'ООО Производственная компания ПК')

        req = 'ООО "Производственная компания" "ПК"'
        s = replace_quotes(req)
        self.assertEqual(s, 'ООО "Производственная компания" "ПК"')

    def test_convert_bytes(self):
        """ Test convert bytes """

        res = convert_bytes(100)
        self.assertEqual(res, '100.0 Б')

        res = convert_bytes(1024)
        self.assertEqual(res, '1.0 КБ')

        res = convert_bytes(1024*1024)
        self.assertEqual(res, '1.0 МБ')

