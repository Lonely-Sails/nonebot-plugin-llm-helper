import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from nonebot.plugin import PluginMetadata, _managers


@dataclass
class Param:
    optional: bool
    description: str


@dataclass
class Command:
    command: str
    description: str
    usage: str
    example: str
    params: dict[str, Param] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.params = {
            key: Param(**param) if not isinstance(param, Param) else param
            for key, param in self.params.items()
        }


@dataclass
class Plugin:
    name: str
    path: Optional[Path]
    meta: Optional[PluginMetadata]
    helper: list[Command] = field(default_factory=list)

    def __hash__(self):
        return hash(self.name)

    def __post_init__(self) -> None:
        self.helper = [
            Command(**command) if not isinstance(command, Command) else command
            for command in self.helper
        ]


def search_plugins() -> set[Plugin]:
    plugins = set()
    for manager in _managers:
        for plugin_id in manager.plugins:
            if plugin_module := sys.modules.get(plugin_id, None):
                plugin_meta: PluginMetadata | None = getattr(plugin_module, '__plugin_meta__', None)
                if plugin_meta and plugin_meta.type == 'library':
                    continue
                if plugin_module.__file__:
                    path = Path(plugin_module.__file__)
                    plugins.add(Plugin(name=plugin_id, meta=plugin_meta, path=path.parent))
                continue
            plugins.add(Plugin(name=plugin_id, meta=None, path=None))
    return plugins
