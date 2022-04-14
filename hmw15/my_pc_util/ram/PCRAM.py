import psutil
from ..utility.PCUtility import PCPercentageBar
from ..decorators.PCDecorators import save_to_file
from ..interface.PCInterface import PCInterface


class PCRAM(PCInterface):
    def __init__(self):
        self.bar = PCPercentageBar()

    @save_to_file("ram.txt")
    def get(self) -> list:
        ram_obj = psutil.virtual_memory()
        ram_str = f"RAM: {ram_obj.total / 1024 / 1024 / 1024:.0f} GB"
        svmem_perc = f"{ram_obj.percent}% {self.bar.get(ram_obj.percent)}"
        return [f"{ram_str:<10}{svmem_perc:>65}"]

    def show(self):
        for obj in self.get():
            print(obj)


if __name__ == '__main__':
    r = PCRAM()
    r.show()
