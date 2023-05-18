import unittest
from utils.mx_checker import MXCheck
from utils.syntax_checker import SyntaxCheck
from utils.smtp_checker import check_email_smtp 

class TestClass(unittest.TestCase):
    def testall(self):
        # Use test case given by hackathon
        emailList = [
            "alesiaconover@cox.net",
            "magormley1@cox.net",
            "lwoodard@cox.net",
            "stondreau@cox.net",
            "lhutfles@cox.net",
            "bolivarfamily@cox.net",
            "ageecrew@cox.net",
            "0cimei@cox.net",
            "123aloop1@cox.net",
            "1350tw@cox.net",
            "1slgoodman62@cox.net",
            "187thepigs@cox.net",
            "2katz2meny@cox.net",
            "jkaine1994@cox.net",
            "3boyzmom@cox.net",
        ]
        length = len(emailList)
        result = [
            False, 
            False, 
            False, 
            True, 
            True, 
            False, 
            False, 
            False, 
            False, 
            False,
            False,
            False,
            False,
            True,
            True
            ]
        for i in range(length):
            check = MXCheck(emailList[i]) and SyntaxCheck(emailList[i]) and check_email_smtp(emailList[i])
            self.assertEqual(check, result[i])
    
    def testSyntax(self):
        emailList = [
            "alan.teng2003@gmail.com",
            "hackathon@zerobounce.net"
            "f.le.an@yahoo.ca"
            ".dowexi5377@aicogz.com"
            "info@advancetravel.gtmail.co.uk"
            "brucelee.@outlook.ca"
            "info@24-7response.org"
            "info@24-7_response.org"
        ]
        result = [
            True,
            True,
            True,
            False,
            False,
            True,
            False,
            True,
            False
        ]
        length = len(emailList)
        for i in range(length):
            check = MXCheck(emailList[i])
            self.assertEqual(check, result[i])

    def MXTest(self):
        self.assertEqual(MXCheck("alan.teng2003@gmail.com"), True)
        self.assertEqual(MXCheck("alan@viveveeve.org"), False)
        # Note: Can't find any emails that uses A/AAAA as MX

    def SmtpTest(self):
        # TODO: develop test scenarios for SMTPCheck
        pass
if __name__ == '__main__':
    unittest.main()

