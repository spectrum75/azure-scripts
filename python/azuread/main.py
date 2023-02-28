from aad_groups import AADGroup

group_name = "Test Group"
group_description = "A test group"
group_mail_nickname = "test-group"

groups = AADGroup()

print(groups.get_group_id("Test Group"))

# Example usage of the create_update_group function
groups.create_update_group(group_name, group_description, group_mail_nickname)

# Example usage of the delete_group function
# groups.delete_group(group_name)