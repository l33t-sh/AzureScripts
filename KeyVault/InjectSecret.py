import base64
import yaml
from azure.identity import AzureCliCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError
from optparse import OptionParser



parser = OptionParser()
parser.add_option("--path_to_file", dest="path_to_file", help="Please specify a path to the file.yml that needs to be injected as secret")
(options, args) = parser.parse_args()

try:
    with open(options.path_to_file, 'rb') as file:
        local_config = yaml.safe_load(file)
except FileNotFoundError:
    print(f'File "{options.path_to_file}" not found.')
except yaml.YAMLError as exc:
            print(exc)
except Exception as ex:
    print('An error occurred while reading the file.yml:')
    print(ex)

credential = AzureCliCredential()

if __name__ == '__main__':
    for secret in local_config['secrets']:
        try:
            secret_client = SecretClient(vault_url=secret['endpoint'], credential=credential)
            enc_secret = secret_client.set_secret(secret['name'], base64.b64encode(secret['value'].encode()).decode())
            print(f"{enc_secret.properties.version} | {secret['name']} [✓]")
        except AzureError as ex:
            print('An error occurred while uploading the secret to Azure Key Vault:')
            print(ex)