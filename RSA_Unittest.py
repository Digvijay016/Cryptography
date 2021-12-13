import unittest
import RSA


class GreatestCommonDivisorTests(unittest.TestCase):

    def test_any_number_and__one_returns_one(self):
        self.assertEqual(RSA.egcd(1, 1), (1,1,0))
        self.assertEqual(RSA.egcd(2, 1), (1,0,1))
        self.assertEqual(RSA.egcd(3, 1), (1,0,1))

    def test_primes_are_divided_by_one(self):
        self.assertEqual(RSA.egcd(3, 2), (1,1,-1))
        self.assertEqual(RSA.egcd(5, 3), (1,-1,2))
        self.assertEqual(RSA.egcd(7, 3), (1,1,-2))
        self.assertEqual(RSA.egcd(11, 7), (1,2,-3))
        self.assertEqual(RSA.egcd(13, 5), (1,2,-5))
        self.assertEqual(RSA.egcd(17, 2), (1,1,-8))

    def test_coprimes_are_divided_by_one(self):
        self.assertEqual(RSA.egcd(9, 8), (1,1,-1))

    def test_not_coprime(self):
        self.assertNotEqual(RSA.egcd(10, 20), 1)

    def test_modular_inverse(self):
        self.assertEqual(RSA.modinv(3,23),8)

    def test_encrypt(self):
        #(msg, n, k)
        self.assertEqual(RSA.encrypt(44,2963881346,37411),59917500)

    def test_decrypt(self):
        #(en_msg, phi_n , n, k)
        self.assertEqual(RSA.decrypt(793308751,3036011644,3036131869,377),9812)
        self.assertEqual(RSA.decrypt(19932097, 300676612, 300725641, 581), 69)


if __name__ == '__main__':
    unittest.main()