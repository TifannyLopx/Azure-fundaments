from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes
from azure_authenticate import ml_client

my_path = './Datos' ##ruta del archivo que se va a subir a azure

my_data = Data(
    path=my_path,
    type=AssetTypes.URI_FOLDER,
    description="primera carpeta URI con un archivo csv",
    name="carpeta_uri_test1",
    version='1'
)

ml_client.data.create_or_update(my_data)