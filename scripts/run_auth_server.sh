echo "Running Auth Server..."
cd auth-server

# Poetry 환경에서 Django 서버 실행
poetry run python manage.py runserver & python grpc_server.py
