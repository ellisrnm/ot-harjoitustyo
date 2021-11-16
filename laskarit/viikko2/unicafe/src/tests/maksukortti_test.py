import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_asetettu_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortille_voi_ladata_saldoa(self):
        self.maksukortti.lataa_rahaa(90)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_saldo_vahenee_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.lataa_rahaa(190)
        self.maksukortti.ota_rahaa(150)
        self.assertEqual(str(self.maksukortti), "saldo: 0.5")

    def test_saldo_ei_muutu_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(150)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_true_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def test_false_jos_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), False)