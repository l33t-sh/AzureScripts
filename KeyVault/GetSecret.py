from azure.keyvault.secrets import SecretClient
from azure.identity import AzureCliCredential
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--keyVaultUrl", dest="KEYVAULT_URL", help="")
parser.add_option("--secretName", dest="SECRET_NAME", help="")
(options, args) = parser.parse_args()

credential = AzureCliCredential()
client = SecretClient(vault_url=options.KEYVAULT_URL, credential=credential)

if __name__ == '__main__':
    retrieved_secret = client.get_secret(options.SECRET_NAME)
    print(retrieved_secret.value)
