[<img src="https://img.shields.io/badge/Telegram-%40Me-orange">](https://t.me/sho6ot)


![img1](.github/images/demo.png)

> 🇪🇳 README in english available [here](README-EN.md)


## [Настройки](https://github.com/shamhi/BlumCryptoBot/blob/main/.env-example)
| Настройка                | Описание                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| **API_ID / API_HASH**    | Данные платформы, с которой запускать сессию Telegram _(сток - Android)_ |
| **REFERRAL_LINK**        | Реферальная ссылка (напр. https://t.me/blum/app?startapp=ref_rWpJlD48na) |
| **AUTO_CLAIM_TASKS**     | Выполнять ли задания из раздела Tasks _(True / False)_                   |
| **AUTO_PLAY_GAME**       | Играть ли в Drop игру _(True / False)_                                   |
| **RANDOM_POINTS_COUNT**  | Рандомное количество поинтов в Drop игре _(напр. 50,150)_                |
| **SAVE_REFS_DATA**       | Сохранять ли реферальные данные в файле `ref_data.json` _(True / False)_ |
| **USE_RANDOM_USERAGENT** | Использовать ли рандомный User Agent _(True / False)_                    |


## 📕 [Профили](profiles.json)
Для каждой сессии можно создать профиль с уникальными данными:
```json
{
  "session1": {
    "proxy": "http://yGow3a:uBro3wL@58.195.21.83:9715",
    "headers": {}
  },
  "session2": {
    "proxy": "socks5://yGow3a:uBro3wL@58.195.21.83:9715",
    "headers": {}
  }
}
```
> [!NOTE]
> `session1` и `session2` - это примеры названий сессий.  
> Если `headers` пусты, то возьмутся [дефолтные](bot/utils/default.py) значения.


## Установка
Вы можете скачать [**Репозиторий**](https://github.com/shamhi/BlumCryptoBot) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
~ >>> git clone https://github.com/shamhi/BlumCryptoBot.git 
~ >>> cd BlumCryptoBot

# Если вы используете Telethon сессии, то клонируйте ветку "converter"
~ >>> git clone https://github.com/shamhi/BlumCryptoBot.git -b converter
~ >>> cd BlumCryptoBot

# Linux
~/BlumCryptoBot >>> python3 -m venv venv
~/BlumCryptoBot >>> source venv/bin/activate
~/BlumCryptoBot >>> pip3 install -r requirements.txt
~/BlumCryptoBot >>> cp .env-example .env
~/BlumCryptoBot >>> nano .env  # Здесь вы обязательно должны указать ваши API_ID и API_HASH , остальное берется по умолчанию
~/BlumCryptoBot >>> python3 main.py

# Windows
~/BlumCryptoBot >>> python -m venv venv
~/BlumCryptoBot >>> venv\Scripts\activate
~/BlumCryptoBot >>> pip install -r requirements.txt
~/BlumCryptoBot >>> copy .env-example .env
~/BlumCryptoBot >>> # Указываете ваши API_ID и API_HASH, остальное берется по умолчанию
~/BlumCryptoBot >>> python main.py
```


Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/BlumCryptoBot >>> python3 main.py --action (1/2)
# Или
~/BlumCryptoBot >>> python3 main.py -a (1/2)

# 1 - Создает сессию
# 2 - Запускает кликер
# 3 - Запуск через Telegram
```
