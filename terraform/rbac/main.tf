provider "azurerm" {
  features {}
}

# resource "azurerm_role_assignment" "example" {
#   scope              = "/subscriptions/<subscription_id>/resourceGroups/<resource_group_name>"
#   role_definition_id = var.role_definition_id
#   principal_id       = var.principal_id
# }

resource "azurerm_resource_group" "example" {
  name     = "example-resource-group"
  location = "West US"
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageaccount"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "dev"
  }
}

output "storage_account_primary_blob_endpoint" {
  value = azurerm_storage_account.example.primary_blob_endpoint
}
