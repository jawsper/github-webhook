from typing import Any, Literal, Optional, Union

from pydantic import BaseModel


class OwnerModel(BaseModel):
    avatar_url: Optional[str] = None
    deleted: Optional[bool] = None
    email: Optional[str] = None
    events_url: Optional[str] = None
    followers_url: Optional[str] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    gravatar_id: Optional[str] = None
    html_url: Optional[str] = None
    id: int
    login: str
    name: Optional[str] = None
    node_id: Optional[str] = None
    organizations_url: Optional[str] = None
    received_events_url: Optional[str] = None
    repos_url: Optional[str] = None
    site_admin: Optional[bool] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[str] = None
    type: Optional[Literal["Bot", "User", "Organization"]] = None
    url: Optional[str] = None


class TagModel(BaseModel):
    name: str
    digest: str


class ContainerMetadataModel(BaseModel):
    tag: TagModel


class PackageVersionModel(BaseModel):
    author: Optional[OwnerModel] = None
    body: Optional[Union[str, dict]] = None
    body_html: Optional[str] = None
    container_metadata: Optional[ContainerMetadataModel] = None
    created_at: Optional[str] = None
    description: str
    html_url: str
    id: int
    installation_command: str
    metadata: list[dict[str, Any]]
    name: str
    package_files: list[Any]
    summary: str
    version: str


class PackageModel(BaseModel):
    created_at: Optional[str] = None
    description: Optional[str] = None
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: Optional[OwnerModel]
    package_type: str
    package_version: Optional[PackageVersionModel] = None
    registry: Optional[Any] = None
    updated_at: Optional[str] = None


class RegistryModel(BaseModel):
    about_url: str
    name: str
    type: str
    url: str
    vendor: str


class PingBody(BaseModel):
    zen: str
    hook_id: int
    # TODO: add rest of model


class PackageBody(BaseModel):
    action: Literal["published", "updated"]
    enterprise: Optional[Any] = None
    installation: Optional[Any] = None
    organization: Optional[Any] = None
    package: PackageModel
    repository: Optional[Any] = None
    sender: OwnerModel
    # TODO: implement other types, though this app won't need them
