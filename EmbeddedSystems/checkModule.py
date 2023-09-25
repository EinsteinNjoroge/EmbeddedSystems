import importlib

try:
  importlib.import_module("board")
except ImportError:
  print("The `board` package is not installed.")
else:
  print("The `board` package is installed.")