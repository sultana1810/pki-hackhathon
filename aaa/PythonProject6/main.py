from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime

def check_certificate_validity(pem_file_path):
    # Read the certificate file
    with open(pem_file_path, 'rb') as f:
        pem_data = f.read()

    # Load the certificate
    cert = x509.load_pem_x509_certificate(pem_data, default_backend())

    # Get current UTC time
    current_time = datetime.utcnow()

    # Get certificate validity period
    not_before = cert.not_valid_before
    not_after = cert.not_valid_after

    print(f"Certificate validity period:")
    print(f"  Not Before: {not_before}")
    print(f"  Not After : {not_after}")
    print(f"  Current UTC Time: {current_time}")

    # Check if the certificate is currently valid
    if current_time < not_before:
        print("The certificate is not yet valid.")
    elif current_time > not_after:
        print("The certificate has expired.")
    else:
        print("The certificate is currently valid.")

# Example usage
check_certificate_validity('certificate.pem')
