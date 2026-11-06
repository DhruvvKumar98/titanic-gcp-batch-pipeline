"""Smoke test: DAG file is valid Python and has expected structure.

Runs without Airflow installed — uses AST parsing only.
For a full DAG-load test, install apache-airflow and its GCP providers.
"""
import ast
from pathlib import Path

DAG_FILE = Path(__file__).parent / "titanic_dag.py"


def test_dag_parses_as_valid_python():
    source = DAG_FILE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(DAG_FILE))
    assert isinstance(tree, ast.Module)


def test_dag_id_present():
    source = DAG_FILE.read_text(encoding="utf-8")
    assert "dag_id='Titanic_DAG'" in source


def test_expected_task_ids():
    source = DAG_FILE.read_text(encoding="utf-8")
    for task_id in [
        "start_task_id",
        "read_csv_file",
        "clean_data_task",
        "rename_columns_task",
        "calculate_statistics_task",
        "visualization_query_task",
        "bigquery_validation_task",
        "end_task_id",
    ]:
        assert task_id in source, f"Missing task_id: {task_id}"


def test_no_hardcoded_project_id():
    source = DAG_FILE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "PROJECT_ID":
                    if isinstance(node.value, ast.Constant):
                        assert node.value.value == "", (
                            "PROJECT_ID should be empty or env-driven, not hardcoded"
                        )


if __name__ == "__main__":
    test_dag_parses_as_valid_python()
    test_dag_id_present()
    test_expected_task_ids()
    test_no_hardcoded_project_id()
    print("All DAG tests passed.")
