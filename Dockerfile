FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir hatchling asyncpg

COPY . .

RUN hatchling build && \
    pip install --no-cache-dir --no-deps dist/*.whl && \
    pip install --no-cache-dir aiosqlite freenit[sql] asyncpg uvicorn

ENV FREENIT_ENV=prod

COPY prod_config.py /app/sysit/local_config.py

EXPOSE 5000

CMD ["sh", "-c", "python migrate.py && uvicorn sysit.app:app --host 0.0.0.0 --port 5000"]
