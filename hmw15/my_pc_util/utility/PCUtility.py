from colorama import Fore, Style


class PCPercentageBar:
    def __init__(self, rounding_to: int = 5, bar_len: int = 20):
        self.rounding_to = rounding_to
        self.bar_len = bar_len

    def get(self, percent: float) -> str:
        """return pretty percentage bar (**********----------)"""

        astnum = int(self.rounding_to * round(percent / self.rounding_to) / (100 / self.bar_len))
        return f"({Fore.RED + '*' * astnum}{Fore.GREEN + '-' * (self.bar_len - astnum) + Style.RESET_ALL})"

    def show(self, percent: float) -> None:
        print(self.get(percent))


if __name__ == '__main__':
    pcb = PCPercentageBar()
    pcb.show(15)
