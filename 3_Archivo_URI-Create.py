from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes
from azure_authenticate import ml_client

my_path = './Datos/datos.csv' 

my_data = Data(
    path=my_path,
    type=AssetTypes.URI_FILE, 
    description="primera creaciónn de archivo URI",
    name="datos_test_1",
    version="1"
)

ml_client.data.create_or_update(my_data)