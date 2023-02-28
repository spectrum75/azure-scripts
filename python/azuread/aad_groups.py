import requests
from auth import get_token_header

class AADGroup:
    def __init__(self):
        self.url = "https://graph.microsoft.com/v1.0/groups"


    def create_update_group(self, group_name, group_description, group_mail_nickname):
        """
        Creates or updates a security-enabled Active Directory group with the specified name, description, and mail nickname.
        """

        headers = get_token_header()

        # Check if the group already exists
        params = {"$filter": f"displayName eq '{group_name}'"}
        response = requests.get(self.url, headers=headers, params=params)

        if response.ok:
            results = response.json().get("value")

            if len(results) > 1:
                raise ValueError(f"Group {group_name} found {len(results)} times.")

            if len(results) > 0:
                group_id = results[0].get("id")
                print(f"Group '{group_name}' already exists with ID: {group_id}")

                # Update the group properties using a PATCH request
                payload = {"description": group_description}

                update_url = f"{self.url}/{group_id}"
                update_response = requests.patch(update_url, headers=headers, json=payload)

                if update_response.ok:
                    print(f"Group '{group_name}' updated successfully.")
                else:
                    print(f"Failed to update group '{group_name}'. Status code: {update_response.status_code}")
            else:
                # Create the JSON payload for the new group
                payload = {
                    "displayName": group_name,
                    "description": group_description,
                    "mailNickname": group_mail_nickname,
                    "groupTypes": [],  # security type aad group, not office 365
                    "mailEnabled": False,
                    "securityEnabled": True,
                }

                # Send the request to create the group
                response = requests.post(self.url, headers=headers, json=payload)

                # Check the status code of the response to ensure the group was created successfully
                if response.ok:
                    print(f"Group '{group_name}' created successfully.")
                else:
                    print("Failed to create group. Status code: ", response.status_code)
                    print("Failed to create group. Status code: ", response.content)
        else:
            print(f"Failed to get group '{group_name}'. Status code: {response.status_code}")


    def delete_group(self, group_name):
        """
        Deletes the security-enabled Active Directory group with the specified name.
        """

        headers = get_token_header()

        # Check if the group already exists
        params = {"$filter": f"displayName eq '{group_name}'"}
        response = requests.get(self.url, headers=headers, params=params)

        if response.ok:
            results = response.json().get("value")

            if len(results) > 1:
                raise ValueError(f"Group {group_name} found {len(results)} times.")

            if len(results) > 0:
                group_id = results[0].get("id")

                # Send the request to delete the group
                delete_url = f"{self.url}/{group_id}"
                delete_response = requests.delete(delete_url, headers=headers)

                # Check the status code of the response to ensure the group was deleted successfully
                if delete_response.ok:
                    print(f"Group '{group_name}' deleted successfully.")
                else:
                    print(f"Failed to delete group '{group_name}'. Status code: {delete_response.status_code}")
                    print(f"Failed to delete group '{group_name}'. Response: {delete_response.content}")
            else:
                print(f"No group found with name '{group_name}'.")
        else:
            print(f"Failed to get group '{group_name}'. Status code: {response.status_code}")


    def get_group_id(self, group_name):
            """
            Gets the id of a security-enabled Active Directory group with the specified name.
            """

            headers = get_token_header()

            # Check if the group already exists
            params = {"$filter": f"displayName eq '{group_name}'"}
            response = requests.get(self.url, headers=headers, params=params)

            if response.ok:
                results = response.json().get("value")

                if len(results) > 1:
                    raise ValueError(f"Group {group_name} found {len(results)} times.")

                if len(results) > 0:
                    return results[0].get("id")
            
            print(f"No group found with name '{group_name}'.")
            