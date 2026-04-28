"""Parse pytest test output into per-test result mappings."""
import re


def parse_log(log: str) -> dict[str, str]:
    """Parse test runner output into per-test results.

    Args:
        log: Full stdout+stderr output of ``bash run_test.sh 2>&1``.

    Returns:
        Dict mapping test_id to status.
        - test_id: pytest native format, e.g.
          ``tests/foo.py::TestClass::test_func[param]``
        - status: one of "PASSED", "FAILED", "SKIPPED", "ERROR"
    """
    # Strip ANSI escape codes
    log = re.sub(r'\x1b\[[0-9;]*m', '', log)

    results: dict[str, str] = {}

    # Inline progress line:  "tests/foo.py::bar PASSED [ 12%]"
    # The test_id may contain spaces (parametrize), so anchor on the status
    # word followed by optional text and a percentage marker.
    inline_re = re.compile(
        r'^(\S+::\S+.*?)\s+(PASSED|FAILED|SKIPPED|ERROR)(?:\s.*?)?\s+\[\s*\d+%\]',
        re.MULTILINE,
    )
    for m in inline_re.finditer(log):
        test_id, status = m.group(1).strip(), m.group(2)
        results.setdefault(test_id, status)

    # Short-form summary lines (e.g. "PASSED tests/foo.py::bar - reason")
    summary_re = re.compile(
        r'^(PASSED|FAILED|SKIPPED|ERROR)\s+(\S+::\S+)',
        re.MULTILINE,
    )
    for m in summary_re.finditer(log):
        status, test_id = m.group(1), m.group(2).rstrip('-').strip()
        results.setdefault(test_id, status)

    # Collection errors: "ERROR tests/foo.py" (no "::")
    collection_re = re.compile(
        r'^ERROR\s+(tests/\S+\.py)\s*$',
        re.MULTILINE,
    )
    for m in collection_re.finditer(log):
        results.setdefault(m.group(1), 'ERROR')

    return results


if __name__ == '__main__':
    log = open('test_output.log').read()
    results = parse_log(log)
    print(f"Parsed {len(results)} tests")
    print(f"Status distribution: { {s: sum(1 for v in results.values() if v == s) for s in set(results.values())} }")

