FROM python:3.12.4

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install --no-dev

# 애플리케이션 코드 복사
COPY . .

# Gunicorn 설치
RUN pip install gunicorn

# Gunicorn으로 Django 서버 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "auth_server.wsgi:application"]