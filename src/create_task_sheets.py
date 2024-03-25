import inspect
import os
from typing import List, Literal

import nbformat

from task_sets import get_tasks_from_each_task_set


def create_task_sheets(num_tasks_per_set, num_task_sheets,
                       for_what: List[Literal['manual', 'auto', 'ChatGPT']] = ['manual']):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for i in range(num_task_sheets):
        tasks = get_tasks_from_each_task_set(num_tasks_per_set)
        for goal in for_what:
            basic_notebook_path = os.path.join(dir_path, f'basic_task_sheets/task_sheet_for_{goal}_gen.ipynb')
            save_to_path = os.path.join(dir_path, f'task_sheets/task_sheet_{i}_for_{goal}_gen.ipynb')
            save_tasks_to_notebook(basic_notebook_path, tasks, save_to_path)


def save_tasks_to_notebook(basic_notebook, tasks_per_set: list, save_to_path):
    with open(basic_notebook, 'r', encoding='utf-8') as nb_file:
        nb = nbformat.read(nb_file, as_version=4)

    for idx, tasks_in_set in enumerate(tasks_per_set):
        nb.cells.append(nbformat.v4.new_markdown_cell(f'## Task Set {idx + 1}'))
        test_config = []
        for task in tasks_in_set:
            from_metadata, to_metadata, task_func = task
            new_cell = nbformat.v4.new_code_cell(inspect.getsource(task_func))
            nb.cells.append(new_cell)
            test_config.append(f"({from_metadata}, {to_metadata}, {task_func.__name__})")

        if len(tasks_in_set) > 0:
            test_config = ', '.join(test_config)
            test_code = "# test the tasks in this set\ntest_conversion_functions([{}])".format(test_config)
            nb.cells.append(nbformat.v4.new_code_cell(test_code))

    with open(save_to_path, 'w', encoding='utf-8') as nb_file:
        nbformat.write(nb, nb_file)
