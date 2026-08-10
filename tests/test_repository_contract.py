# Configuration:
# - REPOSITORY_ROOT resolves to the repository containing this test.
# - REQUIRED_PATHS defines the publication baseline.
# - PRIVATE_PATTERNS blocks common confidential values and machine-local paths.

import json
import logging
import re
import unittest
from pathlib import Path

LOGGER = logging.getLogger(__name__)
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = (
    "README.md",
    "README.pt-BR.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "AGENTS.md",
    "PROJECT_MAP.md",
    "docs/ARCHITECTURE_V0.md",
    "docs/MODEL_ROUTING.md",
    "docs/MULTI_ACCOUNT_OPERATIONS.md",
    "docs/ORCHESTRATION_CONTRACTS.md",
    "docs/EVIDENCE_AND_GATES.md",
    "docs/SECURITY_AND_ISOLATION.md",
    "docs/OPERATIONS.md",
    "docs/MODEL_BENCHMARKS.md",
    "docs/DECISIONS.md",
    "docs/ROADMAP.md",
    "schemas/handoff.schema.json",
    "schemas/review-verdict.schema.json",
    "screenshots/README.md",
)
PRIVATE_PATTERNS = {
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.IGNORECASE),
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "assigned secret": re.compile(
        r"(?i)\b(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|password)\b\s*[:=]\s*['\"][^'\"]{8,}"
    ),
}


class RepositoryContractTests(unittest.TestCase):
    def test_required_paths_exist(self) -> None:
        missing = [path for path in REQUIRED_PATHS if not (REPOSITORY_ROOT / path).is_file()]
        self.assertEqual([], missing, f"Missing publication paths: {missing}")

    def test_json_schemas_are_valid_json(self) -> None:
        for path in sorted((REPOSITORY_ROOT / "schemas").glob("*.json")):
            with self.subTest(path=path.name):
                parsed = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual("object", parsed.get("type"))
                self.assertIn("$schema", parsed)

    def test_tracked_text_is_sanitized(self) -> None:
        failures: list[str] = []
        text_suffixes = {".md", ".json", ".py", ".svg", ".txt", ".yml", ".yaml"}
        for path in sorted(REPOSITORY_ROOT.rglob("*")):
            if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in text_suffixes:
                continue
            content = path.read_text(encoding="utf-8")
            for label, pattern in PRIVATE_PATTERNS.items():
                if pattern.search(content):
                    failures.append(f"{path.relative_to(REPOSITORY_ROOT)}: {label}")
        LOGGER.info("sanitization_scan_complete", extra={"files_with_findings": len(failures)})
        self.assertEqual([], failures, "Potential confidential content found: " + "; ".join(failures))

    def test_documentation_only_boundary_is_explicit(self) -> None:
        readme = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("does not contain or run the builder", readme)
        self.assertFalse((REPOSITORY_ROOT / "src").exists())
        self.assertFalse((REPOSITORY_ROOT / "hermes_builder").exists())


if __name__ == "__main__":
    unittest.main()
