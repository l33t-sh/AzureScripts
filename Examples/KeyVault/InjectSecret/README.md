# KeyVault | InjectSecret 

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