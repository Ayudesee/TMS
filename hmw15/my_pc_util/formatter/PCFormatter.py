from colorama import Fore, Back, Style, init

from ..ram.PCRAM import PCRAM
from ..process.PCProcess import PCProcess
from ..disk.PCDisk import PCDisk
from ..boot_time.PCBootTime import PCBootTime


class PCFormatter:
    def __init__(self):
        init(autoreset=True)

    def show(self):
        disk = PCDisk()
        boot = PCBootTime()
        ram = PCRAM()
        process = PCProcess()

        disk.show()
        boot.show()
        ram.show()
        print(Fore.BLUE + "-" * 61 + Style.RESET_ALL)
        print(Back.LIGHTBLACK_EX + f"{'PID':<10} {'User':>14} {'Process':>35}")
        process.show()


if __name__ == '__main__':
    pcf = PCFormatter()
    pcf.show()
