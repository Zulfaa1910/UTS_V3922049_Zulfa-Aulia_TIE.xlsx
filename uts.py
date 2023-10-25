# Fungsi untuk mencari invers modulo dari a terhadap m
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Fungsi untuk melakukan enkripsi menggunakan Affine Cipher
def affine_encrypt(plain_text, key_a, key_b):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            char_idx = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            encrypted_idx = (key_a * char_idx + key_b) % 26
            encrypted_char = chr(encrypted_idx + ord('A')) if char.isupper() else chr(encrypted_idx + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk melakukan dekripsi menggunakan Affine Cipher
def affine_decrypt(encrypted_text, key_a, key_b):
    key_a_inv = mod_inverse(key_a, 26)
    if key_a_inv is None:
        return "Kunci tidak valid."

    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            char_idx = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            decrypted_idx = (key_a_inv * (char_idx - key_b)) % 26
            decrypted_char = chr(decrypted_idx + ord('A')) if char.isupper() else chr(decrypted_idx + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Fungsi untuk melakukan enkripsi menggunakan Vigenere Cipher
def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    encrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(plain_text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk melakukan dekripsi menggunakan Vigenere Cipher
def vigenere_decrypt(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    decrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Fungsi utama program
def main():
    print("Program Enkripsi dan Dekripsi")

    while True:
        choice = input("Pilih metode:\nA. Affine Cipher\nB. Vigenere Cipher\nPilihan (A/B): ")
        
        if choice not in ['A', 'B']:
            print("Pilihan tidak valid. Silakan pilih A atau B.")
            continue

        if choice == 'A':
            key_a = 1
            key_b = 9
            plain_text = input("Masukkan teks yang ingin dienkripsi: ")
            encrypted_text = affine_encrypt(plain_text, key_a, key_b)
        else:
            key = "zulfa"
            plain_text = input("Masukkan teks yang ingin dienkripsi: ")
            encrypted_text = vigenere_encrypt(plain_text, key)

        decrypted_text = ""
        if choice == 'A':
            decrypted_text = affine_decrypt(encrypted_text, key_a, key_b)
        else:
            decrypted_text = vigenere_decrypt(encrypted_text, key)
        
        print("Teks terenkripsi:", encrypted_text)
        print("Teks terdekripsi:", decrypted_text)
        
        another = input("Lakukan operasi lainnya? (y/n): ")
        if another.lower() != 'y':
            break

if _name_ == "_main_":
    main()