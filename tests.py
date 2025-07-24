import unittest
from functions import *
class TestProject(unittest.TestCase):
  def test_perevod_error1(self):
    error,text = perevod("",16,10)  
    self.assertEqual(error, False)
    self.assertEqual(text, "Пустая строка")
  def test_perevod_error2(self):
    error,text = perevod("ФЫВА",11,10)  
    self.assertEqual(error, False)
    self.assertEqual(text, "Неверное число или система счисления")
  def test_perevod_error3(self):
    error,text = perevod("!!123456!!!",11,10)  
    self.assertEqual(error, False)
    self.assertEqual(text, "Неверное число или система счисления")
  def test_perevod_error4(self):
    error,text = perevod("1234",37,10)  
    self.assertEqual(error, False)
    self.assertEqual(text, "Система не поддерживается. Максимальное значение 36")
  def test_perevod_error_5(self):
    error,text = perevod("1234",1,10)  
    self.assertEqual(error, False)
    self.assertEqual(text, "Основание системы счисления не может быть меньше 2")
  def test_perevod_error_6(self):
    error,text = perevod("26",45,10)  
    self.assertEqual(error, False)
    self.assertEqual(text, "Система не поддерживается. Максимальное значение 36")
  def test_perevod_to10_1(self):
    error,text = perevod("100",2,10)  
    self.assertEqual(error, True)
    self.assertEqual(text, "4")
  def test_perevod_to10_2(self):
    error,text = perevod("FF",16,10)  
    self.assertEqual(error, True)
    self.assertEqual(text, "255")
  def test_perevod_to10_3(self):
    error,text = perevod("10",8,10)  
    self.assertEqual(error, True)
    self.assertEqual(text, "8")
  def test_perevod_to10_4(self):
    error,text = perevod("AA",30,10)  
    self.assertEqual(error, True)
    self.assertEqual(text, "310") 
  def test_perevod_to10_5(self):
    error,text = perevod("0000000022",8,10)  
    self.assertEqual(error, True)
    self.assertEqual(text, "18")
  def test_perevod_todr_1(self):
    error,text = perevod("23",4,3)  
    self.assertEqual(error, True)
    self.assertEqual(text, "102")
  def test_perevod_todr_2(self):
    error,text = perevod("134",5,16)  
    self.assertEqual(error, True)
    self.assertEqual(text, "2C")
  def test_perevod_todr_3(self):
    error,text = perevod("2126",7,19)  
    self.assertEqual(error, True)
    self.assertEqual(text, "21E")
  def test_perevod_todr_4(self):
    error,text = perevod("Z",36,10)  
    self.assertEqual(error, True)
    self.assertEqual(text, "35")
  def test_perevod_todr_5(self):
    error,text = perevod("13",10,16)  
    self.assertEqual(error, True)
    self.assertEqual(text, "D")
  def test_perevod_todr_6(self):
    error,text = perevod("21",2,16)  
    self.assertEqual(error, False)
    self.assertEqual(text, "Неверное число или система счисления")
  def test_calculator_error1(self):
    error,text = calculator(5,6,'7',8)
    self.assertEqual(error,False)
    self.assertEqual(text,"Неподдерживаемая операция")
  def test_calculator_error2(self):
    error,text =calculator("ФЫВА","tuu","+",4)
    self.assertEqual(error,False)
    self.assertEqual(text, "Неверное число или система счисления")
  def test_calculator_error3(self):
    error,text = calculator("123","0","//",4)
    self.assertEqual(error,False)
    self.assertEqual(text, "НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!")
  def test_calculator1(self):
    error,text = calculator("2355","4536","+",7)
    self.assertEqual(error,True)
    self.assertEqual(text, '10224')
  def test_calculator2(self):
    error,text = calculator("2ADL","456","*",35)
    self.assertEqual(error,True)
    self.assertEqual(text, "9IF4BL")
  def test_calculator3(self):
    error,text = calculator("2087","67","+",9)
    self.assertEqual(error,True)
    self.assertEqual(text, '2165')
  def test_calculator4(self):
    error,text = calculator("FEA","AEF","//",20)
    self.assertEqual(error,True)
    self.assertEqual(text, "1")
  def test_calculator5(self):
    error,text = calculator("01010001","0101","-",2)
    self.assertEqual(error,True)
    self.assertEqual(text, '1001100')
  def test_calculator6(self):
    error,text = calculator("27895","A4","*",11)
    self.assertEqual(error,True)
    self.assertEqual(text, "26098A9")
  def test_calculator7(self):
    error,text = calculator("ABFD","A23DF","+",16)
    self.assertEqual(error,True)
    self.assertEqual(text, 'ACFDC')
  def test_calculator8(self):
    error,text = calculator("30453","453","//",7)
    self.assertEqual(error,True)
    self.assertEqual(text, "43")
  def test_calculator9(self):
    error,text = calculator("ASDFGHJKL","QWERTYUIOP","+",36)
    self.assertEqual(error,True)
    self.assertEqual(text, "R7759FC29A")
  def test_calculator10(self):
    error,text = calculator("777777777777777","888888888888888","+",32)
    self.assertEqual(error,True)
    self.assertEqual(text, "FFFFFFFFFFFFFFF")
  def test_calculator11(self):
    error,text = calculator("45","MNBV","+",18)
    self.assertEqual(error,False)
    self.assertEqual(text,"Неверное число или система счисления")
  def test_calculator12(self):
    error,text = calculator("1","A","+",16)
    self.assertEqual(error,True)
    self.assertEqual(text,"B") 
    
if __name__ == "__main__":
 unittest.main()