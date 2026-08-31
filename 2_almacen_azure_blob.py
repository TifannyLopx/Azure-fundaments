from azure.ai.ml.entities import AzureBlobDatastore
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    credential=DefaultAzureCredential(),
     suscription_id= "4a25e6a5-5e1c-491a-a0f4-e5ffc575dc1b",
      resource_group_name= "1primer_test_azure",
      workspace_name= "test1"
)

store = AzureBlobDatastore(
    name="Test1",
    description="Estoy aprendiendo a crear almacenes de datos y este es el primero",
    account_name="tifannylopx",
    container_name="test1"
)

ml_client.create_or_update(store)