# Bicep Samples

Tos use add custom parameter files to the parameters directory.

## Role Assignments

See the [role assignment documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/scenarios-rbac) and the [bicep definition here](https://learn.microsoft.com/en-us/azure/templates/microsoft.authorization/roleassignments?pivots=deployment-language-bicep)

```sh
az deployment group what-if --resource-group <RG-NAME> --template-file .\deploy.bicep --parameters .\parameters\parameters.json
```

```sh
az deployment create --resource-group <RG-NAME> --template-file .\deploy.bicep --parameters .\parameters\parameters.json
```