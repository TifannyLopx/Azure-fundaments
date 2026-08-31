from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    DefaultAzureCredential(), "4a25e6a5-5e1c-491a-a0f4-e5ffc575dc1b", "1primer_test_azure", 
"test1"
)