import time
import datetime
import psutil
import os
from colorama import init
from colorama import Fore, Back, Style


class CPUStat:
    def __init__(self):
        init(autoreset=True)

    def _cls(self):
        """console clearing function"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_all_processes(self, user="usr") -> dict:
        """Get all processes running on machine with user='all'.
         Get processes without 'None' user with user='usr'"""

        proc_dict = {}
        for proc in psutil.process_iter():
            dictproc = proc.as_dict(attrs=['name', 'username'])
            if user == "usr" and dictproc['username'] is None:
                continue
            proc_dict[proc.pid] = dictproc
        return proc_dict

    def virtual_memory(self):
        return psutil.virtual_memory()

    def get_swap_memory(self):
        print(psutil.swap_memory())

    def get_all_disks(self):
        return psutil.disk_partitions()

    def get_disk_usage(self, mountpoint):
        return psutil.disk_usage(mountpoint)

    def get_inet(self):
        for conn in psutil.net_connections(kind='inet'):
            print(conn)

    def get_boot_time(self) -> str:
        """return boot_time in days"""
        boot_time = time.time() - psutil.boot_time()
        return str(datetime.timedelta(seconds=boot_time))

    def get_process_info(self, pid: int):
        psutil.Process(pid=pid)

    def get_stats(self):
        # TODO: Various method calls
        self.formatter(
            boot_time=self.get_boot_time(),
            all_disks=self.get_all_disks(),
            processes=self.get_all_processes(),
            svmem=self.virtual_memory()
        )

    def get_percent_bar(self, percent: float) -> str:
        """return pretty percentage bar (**********----------)"""

        n = 5
        astnum = int(n * round(percent / n) / 5)
        return f"({Fore.RED + '*' * astnum}{Fore.GREEN + '-' * (20 - astnum) + Style.RESET_ALL})"

    def print_disks(self, kwargs):
        for disk in kwargs['all_disks']:
            diskinfo = self.get_disk_usage(disk.mountpoint)
            percent_bar = f"{diskinfo.percent}% {self.get_percent_bar(diskinfo.percent)}"
            print(f"{disk.mountpoint:<10} Total: {diskinfo.total / 1024 / 1024 / 1024:.0f} GB {percent_bar:>50}")

    def print_boot_time(self, kwargs):
        print(f"Boot time: " + kwargs['boot_time'])

    def print_ram(self, kwargs):
        ram = f"RAM: {kwargs['svmem'].total / 1024 / 1024 / 1024:.0f} GB"
        svmem_perc = f"{kwargs['svmem'].percent}% {self.get_percent_bar(kwargs['svmem'].percent)}"
        print(f"{ram:<10}{svmem_perc:>65}")

    def print_processes(self, kwargs):
        for proc, val in kwargs['processes'].items():
            username = val['username'].split('\\')[-1]
            process_name = val['name']
            print(f"{proc:<10}", f"{username:>14}", f"{process_name:>35}")

    def formatter(self, **kwargs):
        self.print_disks(kwargs)
        self.print_boot_time(kwargs)
        self.print_ram(kwargs)
        print(Fore.BLUE + "-" * 61 + Style.RESET_ALL)
        print(Back.LIGHTBLACK_EX + f"{'PID':<10} {'User':>14} {'Process':>35}")
        self.print_processes(kwargs)


if __name__ == '__main__':
    stat = CPUStat()
    stat.get_stats()
