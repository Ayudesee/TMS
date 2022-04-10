import psutil
from ..decorators.PCDecorators import save_to_file


class PCProcess:
    def __init__(self):
        self.information = "user"

    @save_to_file("process.txt")
    def get(self) -> list:
        """Get all processes running on machine with user='all'.
         Get processes without user 'None' with user='user'"""

        all_processes = []
        for proc in psutil.process_iter():
            dictproc = proc.as_dict(attrs=['name', 'username'])
            if self.information == "user" and dictproc['username'] is None:
                continue
            username = str(dictproc.get('username')).split('\\')[-1]
            process_name = dictproc.get('name')
            all_processes.append(f"{proc.pid:<10} {username:>14} {process_name:>35}")
        return all_processes

    def show(self):
        for process in self.get():
            print(process)


if __name__ == '__main__':
    p = PCProcess()
    p.show()
