from typing import Any, Literal, Optional, Union

from pydantic import BaseModel


class OwnerModel(BaseModel):
    avatar_url: Optional[str]
    deleted: Optional[bool]
    email: Optional[str]
    events_url: Optional[str]
    followers_url: Optional[str]
    following_url: Optional[str]
    gists_url: Optional[str]
    gravatar_id: Optional[str]
    html_url: Optional[str]
    id: int
    login: str
    name: Optional[str]
    node_id: Optional[str]
    organizations_url: Optional[str]
    received_events_url: Optional[str]
    repos_url: Optional[str]
    site_admin: Optional[bool]
    starred_url: Optional[str]
    subscriptions_url: Optional[str]
    type: Optional[Literal["Bot", "User", "Organization"]]
    url: Optional[str]


class TagModel(BaseModel):
    name: str
    digest: str


class ContainerMetadataModel(BaseModel):
    tag: TagModel


class PackageVersionModel(BaseModel):
    author: Optional[OwnerModel]
    body: Optional[Union[str, dict]]
    body_html: Optional[str]
    container_metadata: Optional[ContainerMetadataModel]
    created_at: Optional[str]
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
    created_at: Optional[str]
    description: Optional[str]
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: Optional[OwnerModel]
    package_type: str
    package_version: Optional[PackageVersionModel]
    registry: Optional[Any]
    updated_at: Optional[str]


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
    enterprise: Optional[Any]
    installation: Optional[Any]
    organization: Optional[Any]
    package: PackageModel
    repository: Optional[Any]
    sender: OwnerModel
    # TODO: implement other types, though this app won't need them
