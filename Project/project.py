from datetime import datetime


class Project():
    def __init__(self, auth_id, title, description, target, start_date, end_date) -> None:
        self.auth_id: str = auth_id
        self.title: str = title
        self.description: str = description
        self.traget: int = target
        self.start: datetime = start_date
        self.end: datetime = end_date

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start_date):
        self.__start: datetime = start_date

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end_date):
        self.__end: datetime = end_date

    def __str__(self) -> str:
        return f"""{"="*50}
        Auther: {self.auth_id}
        Title: {self.title}
        Description: {self.description}
        Traget: {self.traget}
        Started at: {self.start.day} / {self.start.month} / {self.start.year}
        Remaning Period: {(self.__end - self.__start).days} days
        {"="*50}
        """
