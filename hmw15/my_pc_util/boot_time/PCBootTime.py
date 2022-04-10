import datetime
import time
import psutil
from ..decorators.PCDecorators import save_to_file


class PCBootTime:
    def __init__(self):
        self.boot_time: float = time.time() - psutil.boot_time()

    @save_to_file("boot.txt")
    def get(self) -> list:
        """return boot_time in days"""
        self.boot_time = time.time() - psutil.boot_time()
        return [str(datetime.timedelta(seconds=self.boot_time))]

    def show(self):
        """prints boot_time"""
        for obj in self.get():
            print(obj)


if __name__ == '__main__':
    b = PCBootTime()
    b.show()
