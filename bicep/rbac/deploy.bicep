@sys.description('Required. Array containing the Principal or Object ID of the Security Principal (User, Group, Service Principal, Managed Identity).')
param principalIds array

@sys.description('Required. Uuid of the Azure RBAC role')
param roleId string

module roleAssignments_rg 'resourceGroup/main.bicep' = [for principalId in principalIds: {
  name: '${uniqueString('${principalId}-${roleId}-${resourceGroup().id}')}-RoleAssignment-RG-Bicep'
  params: {
    principalId: principalId
    roleId: roleId
    description: 'Role assignment for principal ${principalId} deployed by bicep'
  }
}]

output roleAssignments array = [for (principalId, i) in principalIds: {
  assignmentName: roleAssignments_rg[i].name
  assignmentId: roleAssignments_rg[i].outputs.resourceId
}]
