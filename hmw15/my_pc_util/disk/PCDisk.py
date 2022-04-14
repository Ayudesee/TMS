import psutil
from ..utility.PCUtility import PCPercentageBar
from ..decorators.PCDecorators import save_to_file
from ..interface.PCInterface import PCInterface


class PCDisk(PCInterface):
    def __init__(self):
        self.bar = PCPercentageBar()

    @save_to_file("disk.txt")
    def get(self):
        all_disks_info = []
        for disk in psutil.disk_partitions():
            disk_info = psutil.disk_usage(disk.mountpoint)
            percent_bar = f"{disk_info.percent}% {self.bar.get(disk_info.percent)}"
            on_print = f"{disk.mountpoint:<10} Total: {disk_info.total / 1024 / 1024 / 1024:.0f} GB {percent_bar:>50}"
            all_disks_info.append(on_print)
        return all_disks_info

    def show(self):
        for disk in self.get():
            print(disk)


if __name__ == '__main__':
    d = PCDisk()
    d.show()
