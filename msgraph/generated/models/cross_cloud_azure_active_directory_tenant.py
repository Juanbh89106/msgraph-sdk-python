from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_source = lazy_import('msgraph.generated.models.identity_source')

class CrossCloudAzureActiveDirectoryTenant(identity_source.IdentitySource):
    @property
    def cloud_instance(self,) -> Optional[str]:
        """
        Gets the cloudInstance property value. The cloudInstance property
        Returns: Optional[str]
        """
        return self._cloud_instance
    
    @cloud_instance.setter
    def cloud_instance(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudInstance property value. The cloudInstance property
        Args:
            value: Value to set for the cloudInstance property.
        """
        self._cloud_instance = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CrossCloudAzureActiveDirectoryTenant and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.crossCloudAzureActiveDirectoryTenant"
        # The cloudInstance property
        self._cloud_instance: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossCloudAzureActiveDirectoryTenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossCloudAzureActiveDirectoryTenant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossCloudAzureActiveDirectoryTenant()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cloud_instance": lambda n : setattr(self, 'cloud_instance', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("cloudInstance", self.cloud_instance)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

