import cv2
import numpy as np

# ==============================
# Encryption Function
# ==============================
def encrypt_image(image_path, key):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    encrypted = img ^ key
    encrypted = np.roll(encrypted, shift=key, axis=0)
    encrypted = np.roll(encrypted, shift=key, axis=1)

    cv2.imwrite("encrypted.png", encrypted)
    print("Encrypted image saved as encrypted.png")


# ==============================
# Decryption Function
# ==============================
def decrypt_image(image_path, key):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    decrypted = np.roll(img, shift=-key, axis=0)
    decrypted = np.roll(decrypted, shift=-key, axis=1)
    decrypted = decrypted ^ key

    cv2.imwrite("decrypted.png", decrypted)
    print("Decrypted image saved as decrypted.png")


# ==============================
# Main Menu
# ==============================
if __name__ == "__main__":
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = int(input("Enter choice: "))
    path = input("Enter image path: ")
    key = int(input("Enter key (0-255): "))

    if choice == 1:
        encrypt_image(path, key)
    elif choice == 2:
        decrypt_image(path, key)
    else:
        print("Invalid choice!")
