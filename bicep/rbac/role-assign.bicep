// only supports resource group currently

@sys.description('Required. The Principal or Object ID of the Security Principal (User, Group, Service Principal, Managed Identity).')
param principalId string

// TODO review this param
@sys.description('Required. Name of the Resource Group to assign the RBAC role to. If not provided, will use the current scope for deployment.')
param resourceGroupName string

@sys.description('Optional. The description of the role assignment.')
param description string = ''

@sys.description('Required. Id of the Azure RBAC role')
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

@sys.description('This is the built-in VM user role')
resource vmUserRoleDefinition 'Microsoft.Authorization/roleDefinitions@2018-01-01-preview' existing = {
  scope: subscription()
  name: 'fb879df8-f326-4884-b1cf-06f3ad86be52'
}

resource roleAssignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(resourceGroupName, roleId, principalId)
  scope: resourceGroup()  // TODO add other scopes
  properties: {
    principalId: principalId
    roleDefinitionId: vmUserRoleDefinition.id
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
