import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    # Kassapäätteen alustus
    def test_kassan_saldo_on_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_myytyjen_edullisten_maara_on_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassan_myytyjen_maukkaiden_maara_on_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Syö edullisesti käteisellä
    def test_edullinen_kateisella_kassan_saldo_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_kateisella_vaihtoraha_on_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_edullinen_kateisella_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_kateisella_rahamaara_ei_riittava_oikein(self):
        syo = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(syo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # Syö maukkaasti käteisellä
    def test_maukas_kateisella_kassan_saldo_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukas_kateisella_vaihtoraha_on_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maukas_kateisella_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 3)

    def test_maukas_kateisella_rahamaara_ei_riittava_oikein(self):
        syo = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(syo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Syö edullisesti kortilla
    def test_edullinen_kortilla_veloitus_on_oikein(self):
        veloita = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(veloita, True)

    def test_edullinen_kortilla_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 2)

    def test_edullinen_rahamaara_ei_riittava_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        syo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 40)
        self.assertEqual(self.kassapaate.edulliset, 4)
        self.assertEqual(syo, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Syö maukkaasti kortilla
    def test_maukas_kortilla_veloitus_on_oikein(self):
        veloita = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(veloita, True)

    def test_maukas_kortilla_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_rahamaara_ei_riittava_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        syo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.maukkaat, 2)
        self.assertEqual(syo, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Kortin saldon lataus
    def test_lataa_kortille_saldoa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_lataa_kortille_saldoa_kassan_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_lataa_kortille_negatiivinen_saldo_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)
        self.assertEqual(self.maksukortti.saldo, 1000)
