See the MS graph api documentation here <https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0>

Directory permissions required for service principal are `Group.ReadWrite.All`
Use with a .env file as follows:

```
CLIENT_ID="<your-client-id>"
CLIENT_SECRET="<your-client-secret>"
TENANT_ID="<your-tenant-id>"
```

Run `pip install -r requirements.txt` and test using the `main.py` file.