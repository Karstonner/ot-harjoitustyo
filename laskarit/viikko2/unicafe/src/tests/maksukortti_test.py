import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 15.00)
    
    def test_vaheneminen_kun_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.00)
    
    def test_vaheneminen_kun_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
    
    def test_riittivat_True(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_eivat_riittaneet_False(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)