class Todo():
    # User facing property:
        # task: string

    def __init__(self, task):
        self.task_name = task
        self.complete = False

    def mark_complete(self):
        self.complete = True