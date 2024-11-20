import os
import json

SETTINGS_PATH = "cache/"


class Settings:
    def __init__(self, path=SETTINGS_PATH):
        os.makedirs(path, exist_ok=True)
        self.path = path
        self.settings = self._read_settings()

    def get(self, key: str) -> str:
        try:
            return self.settings[key]
        except KeyError:
            return None

    def set(self, key: str, value: str) -> None:
        self.settings[key] = value
        self._write_settings()

    def _read_settings(self) -> object:
        try:
            local_settings_file = open(self.path + "settings.json")
        except FileNotFoundError:
            return {}
        return json.load(local_settings_file)

    def _write_settings(self) -> None:
        local_settings_file = open(self.path + "settings.json", "w")
        json.dump(self.settings, local_settings_file)
        local_settings_file.close()
