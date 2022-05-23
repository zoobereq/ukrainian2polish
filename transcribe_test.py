#!/usr/bin/env python
"""
Test based on the names and correct transcriptions of 30 Ukrainian politicians (past and present) 
from wikipedia:  https://pl.wikipedia.org/wiki/Kategoria:Ukraińscy_politycy.
"""


import unittest
import transcribe


class TranscribeTest(unittest.TestCase):

    def rewrites(self, string, expected_string):
        transcribed_string = transcribe.ukr2pl(string)
        self.assertEqual(transcribed_string, expected_string)

    def test_1(self):
        self.rewrites("Олексій Миколайович Арестович", "Ołeksij Mykołajowycz Arestowycz")
    
    def test_2(self):
        self.rewrites("Ростислав Володимирович Бабійчук", "Rostysław Wołodymyrowycz Babijczuk")
    
    def test_3(self):
        self.rewrites("Володимир Багазій", "Wołodymyr Bahazij")

    def test_4(self):
        self.rewrites("Олег Романович Бахматюк", "Ołeh Romanowycz Bachmatiuk")
    
    def test_5(self):
        self.rewrites("Іван Багряний", "Iwan Bahriany")
    
    def test_6(self):
        self.rewrites("Геннадій Вікторович Балашов", "Hennadij Wiktorowycz Bałaszow")
    
    def test_7(self):
        self.rewrites("Ярослава Бандера", "Jarosława Bandera")
    
    def test_8(self):
        self.rewrites("Степан Андрійович Бандера", "Stepan Andrijowycz Bandera")
    
    def test_9(self):
        self.rewrites("Олександр Барвінський", "Ołeksandr Barwinski")
    
    def test_10(self):
        self.rewrites("Дмитро Іванович Донцов", "Dmytro Iwanowycz Doncow")
    
    def test_11(self):
        self.rewrites("Леонтій Іванович Форостівський", "Łeontij Iwanowycz Forostiwski")
    
    def test_12(self):
        self.rewrites("Тимофій Сергійович Милованов", "Tymofij Serhijowycz Myłowanow")
    
    def test_13(self):
        self.rewrites("Володимир Олександрович Зеленський", "Wołodymyr Ołeksandrowycz Zełenski")
    
    def test_14(self):
        self.rewrites("Денис Анатолійович Шмигаль", "Denys Anatolijowycz Szmyhal")
    
    def test_15(self):
        self.rewrites("Микола Ганкевич", "Mykoła Hankewycz")
    
    def test_16(self):
        self.rewrites("Антон Юрійович Геращенко", "Anton Jurijowycz Heraszczenko")
    
    def test_17(self):
        self.rewrites("Валерія Олексіївна Гонтарева", "Wałerija Ołeksijiwna Hontarewa")
    
    def test_18(self):
        self.rewrites("Борис Дмитрович Грінченко", "Borys Dmytrowycz Hrinczenko")
    
    def test_19(self):
        self.rewrites("Іван Адамович Чайківський", "Iwan Adamowycz Czajkiwski")
    
    def test_20(self):
        self.rewrites("Василь Яворський", "Wasyl Jaworski")
    
    def test_21(self):
        self.rewrites("Валентин Арсентійович Згурський", "Wałentyn Arsentijowycz Zhurski")
    
    def test_22(self):
        self.rewrites("Ірина Валентинівна Венедіктова", "Iryna Wałentyniwna Wenediktowa")
    
    def test_23(self):
        self.rewrites("Василь Степанович Градовий", "Wasyl Stepanowycz Hradowy")
    
    def test_24(self):
        self.rewrites("Микола Антонович Швець", "Mykoła Antonowycz Szweć")
    
    def test_25(self):
        self.rewrites("Олександр Якович Шумський", "Ołeksandr Jakowycz Szumski")
    
    def test_26(self):
        self.rewrites("Тимотей Старух", "Tymotej Staruch")
    
    def test_27(self):
        self.rewrites("Олександр Павлович Попов", "Ołeksandr Pawłowycz Popow")
    
    def test_28(self):
        self.rewrites("Андрій Мельник", "Andrij Melnyk")
    
    def test_29(self):
        self.rewrites("Микола Кулеба", "Mykoła Kułeba")

    def test_30(self):
        self.rewrites("Євген Григорович Олесницький", "Jewhen Hryhorowycz Ołesnycki")
    
if __name__ == "__main__":
    unittest.main()