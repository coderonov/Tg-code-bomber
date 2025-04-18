
# Telegram Code Bomber

## Описание (Русское)

`main.py` — это скрипт, который шлёт кучу запросов на код авторизации в Telegram на указанный номер телефона. Он использует разные API Telegram, меняет пользовательские агенты, чтобы всё выглядело естественно, и даёт выбрать, сколько раз это всё повторить.

### Что умеет

- Спрашивает номер телефона и сколько раз отправлять запросы.
- Шлёт запросы к разным Telegram API.
- Меняёт юзер-агенты, показывает всё в консоли с цветными сообщениями.
- Делает паузы между циклами, чтобы не нагружать сервера.

### Что нужно

Для работы скрипта нужны такие библиотеки:

- `requests` — чтобы слать запросы в интернет.
- `fake-useragent` — для подмены юзер-агентов.
- `termcolor` — для цветного текста в консоли.

Установи их одной командой:

```bash
pip install requests fake-useragent termcolor
```

### Как запустить

1. Запусти скрипт:

   ```bash
   python main.py
   ```

2. Введи номер телефона (с плюс, например, `+79123456789`).

3. Скажи, сколько раз повторять отправку.

4. Скрипт начнёт бомбить запросами и покажет, сколько их ушло.

### Важно

- Это только для тестов и учёбы! Не используйте для спама или чего-то плохого, это незаконно.
- Некоторые API могут не работать, если Telegram их поменяет.
- Между циклами пауза 5 секунд, чтобы не перегружать сервера.

---

## Description (English)

`main.py` is a script that sends a bunch of Telegram authorization code requests to a given phone number. It uses various Telegram APIs, switches user agents to look legit, and lets you choose how many times to repeat the process.

### What it does

- Asks for a phone number and how many times to send requests.
- Sends requests to different Telegram APIs.
- Switches user agents and shows everything in the console with colorful messages.
- Pauses between cycles to avoid overloading servers.

### What you need

The script requires these libraries:

- `requests` — for sending internet requests.
- `fake-useragent` — for faking user agents.
- `termcolor` — for colorful console text.

Install them with one command:

```bash
pip install requests fake-useragent termcolor
```

### How to run

1. Run the script:

   ```bash
   python main.py
   ```

2. Enter a phone number (with a plus, like `+79123456789`).

3. Specify how many times to send requests.

4. The script will start bombing requests and show how many were sent.

### Heads up

- This is for testing and learning only! Don’t use it for spam or anything bad, it’s illegal.
- Some APIs might stop working if Telegram changes them.
- There’s a 5-second pause between cycles to keep things chill for the servers.
