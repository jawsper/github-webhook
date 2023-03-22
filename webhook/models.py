from typing import Any, Literal

from pydantic import BaseModel


class OwnerModel(BaseModel):
    avatar_url: str | None
    deleted: bool | None
    email: str | None
    events_url: str | None
    followers_url: str | None
    following_url: str | None
    gists_url: str | None
    gravatar_id: str | None
    html_url: str | None
    id: int
    login: str
    name: str | None
    node_id: str | None
    organizations_url: str | None
    received_events_url: str | None
    repos_url: str | None
    site_admin: bool | None
    starred_url: str | None
    subscriptions_url: str | None
    type: Literal["Bot", "User", "Origanization"] | None
    url: str | None


class TagModel(BaseModel):
    name: str
    digest: str


class ContainerMetadataModel(BaseModel):
    tag: TagModel


class PackageVersionModel(BaseModel):
    author: OwnerModel | None
    body: str | dict | None
    body_html: str | None
    container_metadata: ContainerMetadataModel | None
    created_at: str | None
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
    created_at: str | None
    description: str | None
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: OwnerModel | None
    package_type: str
    package_version: PackageVersionModel | None
    registry: Any | None
    updated_at: str | None


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
    enterprise: Any | None
    installation: Any | None
    organization: Any | None
    package: PackageModel
    repository: Any | None
    sender: OwnerModel
    # TODO: implement other types, though this app won't need them
