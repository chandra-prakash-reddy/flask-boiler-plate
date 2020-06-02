import base64
import pyaes


class CryptoAES:
    """
    This class will be helpful in encryption and decryption
    of data using AES Algorithm
    """

    def __init__(self):
        self.key = "Kalkse@&kjdsh%^!ksd683nds%&789n!".encode('utf-8')
        pass

    def encrypt(self, plaintext):
        """
        This method will encrypt the plaintext provied
        :param plaintext: expects plaintext in str format
        :return: AES encrypted ciphertext
        """
        return base64.b64encode(pyaes.AESModeOfOperationCTR(self.key).encrypt(plaintext))

    def decrypt(self, ciphertext):
        """
        This method will decrypt the ciphertext provied
        :param ciphertext: expects ciphertext in str format
        :return: AES decrypted plaintext
        """
        return pyaes.AESModeOfOperationCTR(self.key).decrypt(base64.b64decode(ciphertext)).decode('utf-8')
