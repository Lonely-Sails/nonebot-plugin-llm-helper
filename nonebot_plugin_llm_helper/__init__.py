import asyncio
from nonebot import get_driver, require
from nonebot.log import logger
from nonebot.plugin import PluginMetadata
require('nonebot_plugin_alconna')
from nonebot_plugin_alconna import Command, Args

from .config import Config
from .generate import generate_plugins_help
from .plugin import Plugin, search_plugins
from .data import load_helper

__plugin_meta__ = PluginMetadata(
    name='LLM-Helper',
    description='一个基于 LLM 解析 Github 仓库或代码的 NoneBot 插件。',
    usage='可以通过命令 /help 或 /llm-help 进行查询。',
    homepage='https://github.com/Lonely-Sails/nonebot-plugin-llm-helper',
    type='application',
    config=Config,
)

plugins: set[Plugin] = set()
adapter = get_driver()
alconna_matcher = (
    Command('llm-help')
    .alias('help')
)

@adapter.on_startup
async def _():
    plugins = search_plugins()
    all_count = len(plugins)
    none_meta_count = sum(plugin.meta is None for plugin in plugins)
    logger.info(f'搜索插件完毕：共 {all_count} 个有效的用户插件，{none_meta_count} 个插件未找到元数据与路径已忽略。')
    load_helper(plugins)
    asyncio.create_task(generate_plugins_help(plugins))
