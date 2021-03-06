from databricks_cli.sdk import ApiClient

from takeoff.azure.credentials.keyvault_credentials_provider import KeyVaultCredentialsMixin
from takeoff.util import current_filename


class Databricks(KeyVaultCredentialsMixin):
    def api_client(self, config: dict) -> ApiClient:
        credential_kwargs = super()._transform_key_to_credential_kwargs(
            config["azure"]["keyvault_keys"][current_filename(__file__)]
        )
        return ApiClient(**credential_kwargs)
