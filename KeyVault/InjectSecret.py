import base64
from azure.identity import AzureCliCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError

from optparse import OptionParser

parser = OptionParser()
parser.add_option("--vault_url", dest="vault_url", help="")
parser.add_option("--secret_name", dest="secret_name", help="")
parser.add_option("--path_to_file", dest="path_to_file", help="")
(options, args) = parser.parse_args()

# Read file contents and encode in Base64
try:
    with open(options.path_to_file, 'rb') as file:
        file_content = file.read()
        base64_content = base64.b64encode(file_content).decode('utf-8')
except FileNotFoundError:
    print(f'File "{options.path_to_file}" not found.')
except Exception as ex:
    print('An error occurred while reading the file:')
    print(ex)

credential = AzureCliCredential()
secret_client = SecretClient(vault_url=options.vault_url, credential=credential)

if __name__ == '__main__':
    try:
        secret = secret_client.set_secret(options.secret_name, base64_content)
        print(f'{secret.properties.version} | {options.secret_name} [✓]')
    except AzureError as ex:
        print('An error occurred while uploading the secret to Azure Key Vault:')
        print(ex)