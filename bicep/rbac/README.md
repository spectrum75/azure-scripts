# Bicep Samples

Tos use add custom parameter files to the parameters directory.

## Role Assignments

See documentation <https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/scenarios-rbac> and the bicep defincition here <https://learn.microsoft.com/en-us/azure/templates/microsoft.authorization/roleassignments?pivots=deployment-language-bicep>

```sh
az deployment group what-if --resource-group <RG-NAME> --template-file .\role-assign.bicep --parameters .\parameters\role-assign.parameters.json
```

```sh
az deployment create what-if --resource-group <RG-NAME> --template-file .\role-assign.bicep --parameters .\parameters\role-assign.parameters.json
```