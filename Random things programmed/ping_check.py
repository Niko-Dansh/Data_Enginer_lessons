import subprocess
import platform

def ping(host, count=4):
    """
    Пингует хост и возвращает среднее время отклика в мс или None, если недоступен.
    """
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, str(count), host]

    try:
        output = subprocess.check_output(command, universal_newlines=True)
        # Парсим время отклика из вывода
        times = []
        for line in output.splitlines():
            if platform.system().lower() == 'windows':
                if 'Среднее = ' in line:
                    # Пример: Среднее = 30мс
                    avg = line.split('Среднее = ')[1].replace('мс', '').strip()
                    return float(avg)
            else:
                if 'avg' in line:
                    # Linux пример: rtt min/avg/max/mdev = 30.123/40.456/50.789/5.678 ms
                    avg = line.split('=')[1].split('/')[1]
                    return float(avg)
    except Exception:
        return None

def main():
    hosts = [
        '8.8.8.8',           # Google DNS
        '1.1.1.1',           # Cloudflare DNS
        'google.com',
        'yandex.ru',
        'vk.com'

    ]

    for host in hosts:
        avg_ping = ping(host)
        if avg_ping is not None:
            print(f'{host}: Среднее время отклика {avg_ping} ms')
        else:
            print(f'{host}: Не удалось получить пинг')

if __name__ == "__main__":
    main()
