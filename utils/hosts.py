import ctypes
import sys


def add_host_entry(ip, hostname):
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    need_add_n = False
    with open(hosts_path, 'r') as hosts_file:
        hosts_text = hosts_file.read()
        if not hosts_text.endswith('\n'):
            need_add_n = True
    with open(hosts_path, 'a') as hosts_file:
        if need_add_n:
            hosts_file.write(f'\n')
        hosts_file.write(f'{ip}\t{hostname}\n')


def remove_host_entry(ip, hostname):
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    with open(hosts_path, 'r') as hosts_file:
        lines = hosts_file.readlines()

    with open(hosts_path, 'w') as hosts_file:
        for line in lines:
            if f'{ip}\t{hostname}' not in line:
                hosts_file.write(line)


# 检查管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



if __name__ == '__main__':
    if is_admin():
        add_host_entry('127.0.0.1', 'reqres.in')
        #remove_host_entry('127.0.0.1', 'reqres.in')
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

