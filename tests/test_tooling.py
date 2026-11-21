"""Simple reproducibility tests; these do not claim an AI has passed ethical evaluation."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from evaluation_report import validate, markdown
from vault_lint import check

class EvaluationTests(unittest.TestCase):
    def valid(self):
        return {
            "case_id": "T-01", "reviewer_id": "reviewer A",
            "ratings": {f"D{i}": "U" for i in range(1, 9)},
            "critical_flags": [],
            "evidence": {},
        }

    def test_unscored_is_not_a_pass(self):
        record = self.valid()
        self.assertTrue(validate(record))
        self.assertIn("U =", markdown(record))
        self.assertNotIn("Overall score", markdown(record))

    def test_score_requires_evidence(self):
        record = self.valid()
        record["ratings"]["D2"] = 4
        with self.assertRaises(ValueError):
            validate(record)

    def test_critical_flags_are_restricted(self):
        record = self.valid()
        record["critical_flags"] = ["CF-9"]
        with self.assertRaises(ValueError):
            validate(record)

    def test_bool_is_not_score(self):
        record = self.valid()
        record["ratings"]["D1"] = True
        with self.assertRaises(ValueError):
            validate(record)

class VaultTests(unittest.TestCase):
    def test_link_detection(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "home.md").write_text("[[sub/note]]\n[[missing]]", encoding="utf-8")
            (root / "sub").mkdir()
            (root / "sub" / "note.md").write_text("hello", encoding="utf-8")
            issues, _ = check(root)
            self.assertEqual(len(issues), 1)
            self.assertIn("missing", issues[0])

if __name__ == "__main__":
    unittest.main()
