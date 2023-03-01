from aad_groups import AADGroup

BATCH_SIZE = 10

groups = AADGroup()

for i in range(1, BATCH_SIZE+1):
    group_name = f"Test Group {i}"
    group_description = f"A test group {i}" 
    group_mail_nickname = f"test-group-{i}"

    groups.delete_group(group_name)
