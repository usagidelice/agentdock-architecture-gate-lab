import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.calculator import add
class FixtureTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
