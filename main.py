import numpy as np
import hashlib
from hashlib import md5

class EncryptionAlgoSaif:
    def __init__(self, phrase, secure_Pass):
        self.phrase = phrase
        self.used_space = self.phrase.split(" ")
        self.new_string = ""
        self.security = secure_Pass
        # Remove the matrix initialization from here
    def process_enc_hash(self):
        m = hashlib.md5()
        m.update((self.security))
        self.security =m.digest()
       
    def process_enc(self):
        for i in range(len(self.phrase)):
            if self.phrase[i] == " ":
                for j in range(len(self.used_space)):
                    for k in range(len(self.used_space[j])):
                        for i in range(len(self.security)):
                            x = float(ord(self.security[i]))
                            self.new_string += str(float(ord(self.used_space[j][k])*2.5)/len(self.phrase)*x) + "$"
            else:
                for i in range(len(self.security)):
                    x = float(ord(self.security[i]))
                    self.new_string += str(float(ord(self.phrase[i])*2.5)/len(self.phrase)*x) + "$"

        # Move matrix initialization here, after constructing new_string
        self.Matrice = np.zeros((len(self.new_string.split("$")), 2), dtype=object)
        return self.new_string

    def populate_matrice(self):
        new_string =""
        new_split = self.new_string.split("$")
        for i in range(len(new_split)):
            new_string += new_split[i] + "$"+ " "
            

        return new_string
    
    



solution = EncryptionAlgoSaif("Just testing my newest","tryyy")
solution.process_enc()
print(solution.populate_matrice())
