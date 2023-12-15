# Python Encryption Algorithm Usage

The `EncryptionAlgoSaif` class in Python provides a simple encryption algorithm for a given phrase using a passphrase. This algorithm involves manipulating characters in the phrase based on the passphrase.

## Usage

1. **Import the Required Libraries:**
   - Make sure you have the necessary libraries installed. You can install NumPy using:
     ```bash
     pip install numpy
     ```

2. **Instantiate the EncryptionAlgoSaif Class:**
   - Create an instance of the `EncryptionAlgoSaif` class by providing a phrase and a secure passphrase.
     ```python
     import numpy as np
     from hashlib import md5
     from your_file_name import EncryptionAlgoSaif

     # Replace 'your_file_name' with the actual name of your Python file
     phrase = "Just testing my newest"
     secure_passphrase = "tryyy"
     solution = EncryptionAlgoSaif(phrase, secure_passphrase)
     ```

3. **Process Encryption Hash:**
   - Generate a hash from the secure passphrase using MD5.
     ```python
     solution.process_enc_hash()
     ```

4. **Process Encryption:**
   - Execute the encryption algorithm on the provided phrase.
     ```python
     solution.process_enc()
     ```

5. **Populate Matrice:**
   - Retrieve the encrypted string and format it into a matrix-like structure.
     ```python
     encrypted_matrix = solution.populate_matrice()
     ```

6. **View the Encrypted Matrix:**
   - Print or use the encrypted matrix as needed.
     ```python
     print(encrypted_matrix)
     ```

## Example

```python
import numpy as np
from hashlib import md5
from your_file_name import EncryptionAlgoSaif

phrase = "Just testing my newest"
secure_passphrase = "tryyy"
solution = EncryptionAlgoSaif(phrase, secure_passphrase)

solution.process_enc_hash()
solution.process_enc()
encrypted_matrix = solution.populate_matrice()

print(encrypted_matrix)
