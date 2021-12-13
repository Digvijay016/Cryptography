import unittest
import ElgamalEve


class ElGamalEveUnittest(unittest.TestCase):

    def test_bsgs(self):
        self.assertEqual(ElgamalEve.findxwithBSGS(2355,12613,4708,113),532)
        # self.assertEqual(ElGamal.decrypt(368078788, 8365427, 2, 443), 44)

    def test_decrypt(self):
        #(q, x, c1, c2)
        self.assertEqual(ElgamalEve.findMsg(12613,532,2996,136377),27)
        self.assertEqual(ElgamalEve.findMsg(827, 532, 2996, 136377), 27)
        # self.assertEqual(ElGamal.decrypt(368078788, 8365427, 2, 443), 44)


if __name__ == '__main__':
    unittest.main()