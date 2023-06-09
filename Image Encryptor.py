from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from PIL import Image

# Encrypt an image using AES encryption
def encrypt_image(input_image_path, output_image_path, key):
    # Read the image file
    image = Image.open(input_image_path)

    # Convert the image to bytes
    image_bytes = image.tobytes()

    # Generate a random initialization vector (IV)
    iv = get_random_bytes(AES.block_size)

    # Create a counter object for AES-CTR mode
    counter = Counter.new(AES.block_size * 8, initial_value=int.from_bytes(iv, byteorder='big'))

    # Create the AES cipher object in CTR mode
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)

    # Encrypt the image bytes
    encrypted_data = cipher.encrypt(pad(image_bytes, AES.block_size))

    # Write the encrypted data and IV to the output image file
    with open(output_image_path, 'wb') as f:
        f.write(iv + encrypted_data)

    print("Image encryption complete.")

# Example usage:
# Provide the paths to the input image file, output encrypted image file, and encryption key
input_image_path = "input_image.png"
output_image_path = "encrypted_image.png"
encryption_key = b'ThisIsASecretKey123'

# Call the encrypt_image function
encrypt_image(input_image_path, output_image_path, encryption_key)
