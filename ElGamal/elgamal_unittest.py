import unittest
import ElGamal


class GreatestCommonDivisorTests(unittest.TestCase):

    # def test_zero(self):
    #     self.assertEqual(ElGamal.gcd(0, 0), 0)

    def test_any_number_and__one_returns_one(self):
        self.assertEqual(ElGamal.gcd(1, 1), 1)
        self.assertEqual(ElGamal.gcd(2, 1), 1)
        self.assertEqual(ElGamal.gcd(3, 1), 1)

    def test_primes_are_divided_by_one(self):
        self.assertEqual(ElGamal.gcd(3, 2), 1)
        self.assertEqual(ElGamal.gcd(5, 3), 1)
        self.assertEqual(ElGamal.gcd(7, 3), 1)
        self.assertEqual(ElGamal.gcd(11, 7), 1)
        self.assertEqual(ElGamal.gcd(13, 5), 1)
        self.assertEqual(ElGamal.gcd(17, 2), 1)

    def test_coprimes_are_divided_by_one(self):
        self.assertEqual(ElGamal.gcd(9, 8), 1)

    def test_not_coprime(self):
        self.assertNotEqual(ElGamal.gcd(10, 20), 1)

    def test_modular_inverse(self):
        self.assertEqual(ElGamal.modinv(3,23),8)

    def test_encrypt(self):
        #(msg, bh, g, x, q):
        self.assertEqual(ElGamal.encrypt(114,32,184,5,457),84)

    def test_decrypt(self):
        #(en_msg, ah, y, q)
        self.assertEqual(ElGamal.decrypt(368078788,8365427,1,271),44)
        self.assertEqual(ElGamal.decrypt(84, 179, 6, 457), 114)


if __name__ == '__main__':
    unittest.main()