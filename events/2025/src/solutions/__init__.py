# auto import all days
import importlib
import pkgutil

for quest in pkgutil.iter_modules(__path__):
    importlib.import_module(f'.{quest.name}', package='src.solutions')
