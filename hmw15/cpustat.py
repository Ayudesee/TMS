import time
import datetime
import psutil
import os
from colorama import init
from colorama import Fore, Back, Style
from decorators import save_to_file


class CPUStat:
    def __init__(self):
        init(autoreset=True)

    def _cls(self):
        """console clearing function"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_all_processes(self, user="usr") -> dict:
        """Get all processes running on machine with user='all'.
         Get processes without user 'None' with user='usr'"""

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

    @save_to_file
    def print_disks(self, kwargs):
        return_list = []
        for disk in kwargs['all_disks']:
            diskinfo = self.get_disk_usage(disk.mountpoint)
            percent_bar = f"{diskinfo.percent}% {self.get_percent_bar(diskinfo.percent)}"
            on_print = f"{disk.mountpoint:<10} Total: {diskinfo.total / 1024 / 1024 / 1024:.0f} GB {percent_bar:>50}"
            return_list.append(on_print)
            print(on_print)
        return return_list

    @save_to_file
    def print_boot_time(self, kwargs):
        return_list = []
        on_print = f"Boot time: " + kwargs['boot_time']
        return_list.append(on_print)
        print(on_print)
        return return_list

    @save_to_file
    def print_ram(self, kwargs):
        return_list = []
        ram = f"RAM: {kwargs['svmem'].total / 1024 / 1024 / 1024:.0f} GB"
        svmem_perc = f"{kwargs['svmem'].percent}% {self.get_percent_bar(kwargs['svmem'].percent)}"
        on_print = f"{ram:<10}{svmem_perc:>65}"
        return_list.append(on_print)
        print(on_print)
        return return_list

    @save_to_file
    def print_processes(self, kwargs):
        return_list = []
        for proc, val in kwargs['processes'].items():
            username = val['username'].split('\\')[-1]
            process_name = val['name']
            on_print = f"{proc:<10} {username:>14} {process_name:>35}"
            return_list.append(on_print)
            print(on_print)
        return return_list

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
