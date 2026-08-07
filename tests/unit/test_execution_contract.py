import sys
import unittest


class MockTask:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.status = "pending"
        self.metadata = {}


class MockQueue:

    def __init__(self, tasks):
        self.tasks = list(tasks)

    def empty(self):
        return len(self.tasks) == 0

    def pop(self):
        return self.tasks.pop(0)


class TestExecutionContract(unittest.TestCase):

    def setUp(self):
        from ados.execution.engine import ExecutionEngine
        self.engine_class = ExecutionEngine

    def test_execution_accepts_queue_and_handler(self):
        queue = MockQueue([])

        engine = self.engine_class(
            queue,
            handler=lambda task: task,
        )

        self.assertIs(engine.queue, queue)
        self.assertIsNotNone(engine.handler)
        self.assertIsNotNone(engine.executor)

    def test_pending_to_completed_with_handler(self):
        task = MockTask(1, "test")
        queue = MockQueue([task])

        def success_handler(task):
            self.assertEqual(task.status, "running")

        engine = self.engine_class(
            queue,
            handler=success_handler,
        )

        results = engine.run()

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].status, "completed")

    def test_handler_failure_to_failed_state(self):
        task = MockTask(1, "fail_test")
        queue = MockQueue([task])

        def fail_handler(task):
            raise ValueError("Simulated failure")

        engine = self.engine_class(
            queue,
            handler=fail_handler,
        )

        results = engine.run()

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].status, "failed")
        self.assertIn(
            "Simulated failure",
            results[0].metadata.get("error", ""),
        )

    def test_multiple_tasks_mixed_results(self):
        tasks = [
            MockTask(1, "t1"),
            MockTask(2, "t2"),
        ]

        queue = MockQueue(tasks)

        def handler(task):
            if task.id == 2:
                raise Exception("Error on 2")

        engine = self.engine_class(
            queue,
            handler=handler,
        )

        results = engine.run()

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].status, "completed")
        self.assertEqual(results[1].status, "failed")

    def test_execution_import_isolation(self):
        from pathlib import Path
        import ast

        engine_path = (
            Path(__file__).resolve().parents[2]
            / "python"
            / "ados"
            / "execution"
            / "engine.py"
        )

        tree = ast.parse(engine_path.read_text())

        imported_modules = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_modules.add(alias.name)

            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imported_modules.add(node.module)

        forbidden = {
            "ados.core.brain",
            "ados.core.brain.brain",
            "ados.core.brain.tool_boundary",
        }

        violations = {
            module
            for module in imported_modules
            if any(
                module == forbidden_module
                or module.startswith(forbidden_module + ".")
                for forbidden_module in forbidden
            )
        }

        self.assertEqual(
            violations,
            set(),
            f"ExecutionEngine has forbidden Brain imports: {sorted(violations)}",
        )

    def test_execution_engine_with_real_task_queue(self):
        from ados.execution.engine import ExecutionEngine
        from ados.queue import TaskQueue
        from ados.execution.task import Task

        queue = TaskQueue()

        queue.push(
            Task(
                id="task-001",
                title="Production execution test",
            )
        )

        engine = ExecutionEngine(queue)

        results = engine.execute()

        self.assertEqual(len(results), 1)
        self.assertEqual(
            results[0].status,
            "completed",
        )


if __name__ == "__main__":
    unittest.main()
