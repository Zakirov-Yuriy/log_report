# conftest.py

import sys
from pathlib import Path

# Добавил путь к корню проекта
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
