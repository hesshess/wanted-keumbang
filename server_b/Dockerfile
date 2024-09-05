# 베이스 이미지로 Python 3.12.4 사용
FROM python:3.12.4-slim

# 작업 디렉토리 설정
WORKDIR /app

RUN apt-get update && apt-get install -y libmysqlclient-dev
# Poetry 설치
RUN pip install --upgrade pip && pip install poetry

# 프로젝트 의존성 파일 복사
COPY pyproject.toml poetry.lock /app/

# Poetry를 통해 의존성 설치 (Production 환경만 설치)
RUN poetry config virtualenvs.create false && poetry install --no-dev

# server_b 프로젝트 소스 코드 복사
COPY server_b /app/server_b

# 포트 노출
EXPOSE 8000

# Gunicorn으로 애플리케이션 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server_b.wsgi:application"]
