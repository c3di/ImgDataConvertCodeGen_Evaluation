import random

from .task_set_1_step_conversion import one_step_conversion_task_set
from .task_set_2_steps_conversion import two_steps_conversion_task_set
from .task_set_3_steps_conversion import three_steps_conversion_task_set
from .task_set_4_steps_conversion import four_steps_conversion_task_set
from .task_set_more_steps_conversion import more_steps_conversion_task_set

task_sets = [one_step_conversion_task_set, two_steps_conversion_task_set, three_steps_conversion_task_set,
             four_steps_conversion_task_set, more_steps_conversion_task_set]


def get_tasks_from_each_task_set(num_tasks_per_set):
    tasks = []
    for task_set in task_sets:
        tasks.append(random.sample(task_set, num_tasks_per_set))
    return tasks
