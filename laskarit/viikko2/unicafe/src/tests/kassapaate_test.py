import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_oikea_rahamaara_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_edullisia_myyty_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaita_myyty_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_kateismyynti_tasarahalla(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)
    
    def test_maukkaan_kateismyynti_tasarahalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
    
    def test_edullisen_kateismyynti_vaihtoraha(self):
        self.kassapaate.syo_edullisesti_kateisella(340)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)
    
    def test_maukkaan_kateismyynti_vaihtoraha(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
    
    def test_edullisen_onnistunut_kateismyynti_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukkaan_onnistunut_kateismyynti_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullisen_kateismyynti_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_maukkaan_kateismyynti_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_edullisen_epaonnistunut_kateismyynti_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaan_epaonnistunut_kateismyynti_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_edullinen_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 7.60)
    
    def test_korttiosto_maukas_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 6)
    
    def test_korttiosto_edullisten_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_maukkaiden_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_edullisten_lounaiden_maara_ei(self):
        kortti = Maksukortti(200)

        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_maukkaiden_lounaiden_maara_ei(self):
        kortti = Maksukortti(200)

        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_korttiosto_edullinen_True(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_korttiosto_maukas_True(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_korttiosto_edullinen_False(self):
        kortti = Maksukortti(200)
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
    
    def test_korttiosto_maukas_False(self):
        kortti = Maksukortti(200)
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
    
    def test_korttiosto_ei_muuta_korttia_edullinen(self):
        kortti = Maksukortti(200)

        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 2)
    
    def test_korttiosto_ei_muuta_korttia_maukas(self):
        kortti = Maksukortti(200)

        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo_euroina(), 2)
    
    def test_korttiosto_ei_muuta_kassapaatetta_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_korttiosto_ei_muuta_kassapaatetta_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_kortin_lataaminen_nostaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11)
    
    def test_kortin_lataaminen_laskee_kassapaatteen_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001)
    
    def test_kortin_lataaminen_negatiivisella_maaralla_kortti(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
    
    def test_kortin_lataaminen_negatiivisella_maaralla_kassapaate(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
    
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)