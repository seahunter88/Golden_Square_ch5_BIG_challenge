class todo_list():

    def __init__(self):
        self._task_list = []

    def add_task(self, entry):
        self._task_list.append(entry)

    def all_incomplete(self):
        return [task for task in self._task_list if not task.complete]

    def all_complete(self):
        return [task for task in self._task_list if task.complete]