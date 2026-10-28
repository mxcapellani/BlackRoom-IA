#!/usr/bin/env python3
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from validate import ROOT, REQUIRED, validate, validate_prompt

class NestedContractTests(unittest.TestCase):
    def setUp(self):
        self.sample = json.loads((ROOT / "examples/casual-selfie.json").read_text())
    def test_package(self):
        self.assertEqual(validate(), [])
    def test_sample(self):
        self.assertEqual(validate_prompt(json.dumps(self.sample)), [])
    def test_template(self):
        self.assertEqual(validate_prompt((ROOT / "examples/output-template.json").read_text()), [])
    def test_missing_top_key(self):
        del self.sample["cena"]
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_missing_nested_key(self):
        del self.sample["assunto"]["pose"]["mao"]
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_extra_nested_key(self):
        self.sample["meta"]["unwanted"] = "extra"
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_array_type(self):
        self.sample["cena"]["ambiente"] = "not array"
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_array_item_type(self):
        self.sample["cena"]["ambiente"] = [123]
        self.assertTrue(validate_prompt(json.dumps(self.sample)))
    def test_empty_unknown(self):
        self.sample["assunto"]["pose"]["mao"] = ""
        self.assertEqual(validate_prompt(json.dumps(self.sample)), [])
    def test_duplicates(self):
        self.assertTrue(validate_prompt('{"meta":{},"meta":{}}'))
    def test_invalid_json(self):
        self.assertTrue(validate_prompt('{"meta":{},}'))
    def test_nonstandard_number(self):
        self.assertTrue(validate_prompt('{"meta":NaN}'))
    def test_missing_skill(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "repo"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns("__pycache__", ".git", ".venv"))
            (root / REQUIRED[0]).unlink()
            self.assertTrue(validate(root))

if __name__ == "__main__":
    unittest.main()
