import argparse
from typing import List, Literal

from create_task_sheets import create_task_sheets


def main(num_tasks_per_set: int, num_task_sheets: int, for_what: List[Literal['manual', 'auto', 'ChatGPT']]):
    print(f"Number of tasks per set: {num_tasks_per_set}")
    print(f"Number of task sheets: {num_task_sheets}")
    print(f"For what: {for_what}")
    create_task_sheets(num_tasks_per_set, num_task_sheets, for_what)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Task Sheets for Evaluation")

    parser.add_argument("num_tasks_per_set", type=int, help="The number of tasks in each set. 5 sets in total.")
    parser.add_argument("num_task_sheets", type=int, help="The number of task sheets to generate")
    parser.add_argument("--for_what", nargs="+", type=str, default=['manual'], choices=['manual', 'auto', 'ChatGPT'],
                        help="The evaluation goal using the task sheets (manual, auto, or ChatGPT)")

    args = parser.parse_args()

    main(args.num_tasks_per_set, args.num_task_sheets, args.for_what)
