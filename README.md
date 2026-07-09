# Level-4-practic

# Book API

## Установка

Создать виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Настройка базы данных

Создать файл `.env`:

```env
DB_HOST=localhost
DB_PORT=5433
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
```

## Запуск приложения

```bash
uvicorn app.main:app --reload
```

После запуска открыть:

```
http://127.0.0.1:8000/docs
```

Swagger:

```
http://127.0.0.1:8000/docs
```