# Azure KeyVault | InjectSecret 

⚠️ ***Keep in mind you have to be authorized to access KeyVault at runtime (either by azcli, exporting env variables etc ...)*** ⚠️

<br>


This script is a solution for a CICD pipelines to inject multiple secrets into multiple keyvaults at runtime.

Final secret that is injected into the KeyVault is base64 encoded string (to maintain compatibility especially with multiline secrets.
```yaml
 - name: "myKeyVaultSecret02"
    endpoint: "https://exampleKeyVault02.vault.azure.net/"
    value: |
      {
       "Key": "Value02",
       "Key": "Value03"
      }
```

Application / Script that will read the secrets needs to handle the base64 decode to get the readable content


## Prerequisites 
```
azure-identity 
azure-keyvault-secrets 
azure-core 
pyyaml
```

## Run
```
python3.10 ${WORKDIR}/package/python/azure/InjectSecret.py --path_to_file="${WORKDIR}/secret_file"
```

## Example shell script

- Create config.yml ([Example config](config.yml))
- Run:
```bash
#!/usr/bin/env bash

WORKDIR=$(pwd)
python3.10 -m pip install azure-identity azure-keyvault-secrets azure-core pyyaml
python3.10 ${WORKDIR}/InjectSecret.py --path_to_file="${WORKDIR}/config.yml"
```
