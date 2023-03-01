from aad_groups import AADGroup

BATCH_SIZE = 10

groups = AADGroup()

print("[")

for i in range(1, BATCH_SIZE+1):
    group_name = f"Test Group {i}"
    
    id = groups.get_group_id(group_name)

    print(f"'{id}'")

print("]")


