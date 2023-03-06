# Bicep Samples

To use add a custom parameter files to a parameters directory.

## Resource Groups

See the [bicep definition here](https://learn.microsoft.com/en-us/azure/templates/microsoft.resources/resourcegroups?pivots=deployment-language-bicep)

```sh
az deployment sub what-if --template-file .\deploy.bicep --parameters .\parameters\parameters.json -l <LOCATION>
```

```sh
az deployment sub create --template-file .\deploy.bicep --parameters .\parameters\parameters.json -l <LOCATION>
```