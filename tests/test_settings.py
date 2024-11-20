import unittest
import shutil
from src.settings import Settings

SETTINGS_PATH = "tests/cache/"


class TestSettings(unittest.TestCase):
    def test_not_exists(self):
        settings = Settings(SETTINGS_PATH)
        self.assertIsNone(settings.get("test"))

    def test_save(self):
        settings = Settings(SETTINGS_PATH)
        settings.set("test_key", "test_value")
        file = open(f"{SETTINGS_PATH}settings.json", "r")
        content = file.read()
        file.close()
        self.assertEqual(content, '{"test_key": "test_value"}')

    def test_read(self):
        file = open(f"{SETTINGS_PATH}settings.json", "w")
        file.write('{"test_key": "test_value"}')
        file.close()
        settings = Settings(SETTINGS_PATH)
        self.assertEqual(settings.get("test_key"), "test_value")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(SETTINGS_PATH)


if __name__ == "__main__":
    unittest.main()
