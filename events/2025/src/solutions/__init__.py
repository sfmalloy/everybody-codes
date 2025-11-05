# auto import all quests
import importlib
import pkgutil

for quest in pkgutil.iter_modules(__path__):
    importlib.import_module(f'.{quest.name}', package='solutions')
