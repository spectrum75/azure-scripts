// only supports resource group currently

@sys.description('Required. Array containing he Principal or Object ID of the Security Principal (User, Group, Service Principal, Managed Identity).')
param principalId string

@sys.description('Optional. The description of the role assignment.')
param description string = ''

@sys.description('Required. Uuid of the Azure RBAC role')
param roleId string

@sys.description('Optional. The principal type of the assigned principal ID.')
@allowed([
  'ServicePrincipal'
  'Group'
  'User'
  'ForeignGroup'
  'Device'
])
param principalType string = 'Group'

@sys.description('This is the built-in or custom role to assign')
resource roleDefinition 'Microsoft.Authorization/roleDefinitions@2018-01-01-preview' existing = {
  scope: subscription()
  name: roleId
}

resource roleAssignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(resourceGroup().name, roleDefinition.id, principalId)
  scope: resourceGroup()
  properties: {
    principalId: principalId
    roleDefinitionId: roleDefinition.id
    principalType: principalType
    description: !empty(description) ? description : null
  }
}

@sys.description('The GUID of the Role Assignment.')
output name string = roleAssignment.name

@sys.description('The resource ID of the Role Assignment.')
output resourceId string = roleAssignment.id

@sys.description('The name of the resource group the role assignment was applied at.')
output resourceGroupName string = resourceGroup().name

@sys.description('The scope this Role Assignment applies to.')
output scope string = resourceGroup().id
