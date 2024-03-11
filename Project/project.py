from datetime import datetime

class Project():
    def __init__(self, title, description, target, start_date, end_date) -> None:
        self.title: str= title
        self.description: str = description
        self.traget: int = target
        self.start: datetime = start_date
        self.end: datetime = end_date
    
    @property
    def start(self):
        return self.__start.ctime()

    @start.setter
    def start(self, start_date):
        self.__start: datetime = start_date

    @property
    def end(self):
        return self.__end.ctime()

    @end.setter
    def end(self, end_date):
        self.__end: datetime = end_date

    def __str__(self) -> str:
        return f"""{"="*50}
        Title: {self.title}
        Description: {self.description}
        Traget: {self.traget}
        Remaning Period: {(self.__end - self.__start).days} days
        {"="*50}
        """