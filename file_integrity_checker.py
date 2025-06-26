import hashlib

# Function to calculate the SHA-256 hash of a file
def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path.strip('"'), 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print("File not found:", file_path)
        return None

# Function to check integrity by comparing hashes
def check_integrity(original_hash, file_path):
    current_hash = calculate_hash(file_path)
    if current_hash is None:
        return

    if current_hash == original_hash:
        print("✔ File is intact. No changes detected.")
    else:
        print("✖ WARNING: File has been modified!")

# Main program
def main():
    file_path = input("Enter the file path to monitor: ")
    print("Calculating original hash...")
    original_hash = calculate_hash(file_path)

    if original_hash:
        print("Original SHA-256 Hash:", original_hash)
        input("Make any changes to the file and press Enter to continue...")
        print("Re-checking file integrity...")
        check_integrity(original_hash, file_path)

if __name__ == "__main__":
    main()
