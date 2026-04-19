# RAG Product Search

Сервис семантического поиска по каталогу товаров. Пользователь пишет запрос на естественном языке, система находит релевантные товары через векторный поиск и локальная LLM формирует короткое обоснование выбора.

## Стек

- **Backend:** FastAPI
- **Frontend:** Streamlit
- **БД:** PostgreSQL + pgvector
- **Эмбеддинги:** sentence-transformers (multilingual-e5-small)
- **LLM:** Ollama (локально)
- **Оркестрация:** docker-compose

## Быстрый старт

```bash
cp .env.example .env
docker compose up --build
```

- API: http://localhost:8000
- Healthcheck: http://localhost:8000/health
- Docs: http://localhost:8000/docs

## Структура

```
.
├── backend/          FastAPI приложение
├── frontend/         Streamlit UI
├── data/             датасет каталога (не коммитится)
├── docker-compose.yml
└── plan.md           план проекта
```

## Статус

Находится в разработке. См. `plan.md`.
