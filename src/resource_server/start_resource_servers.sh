#!/bin/bash

# 프로젝트 루트 디렉토리 설정
PROJECT_ROOT=$(dirname $(dirname $(realpath $0)))

# Resource 서버 설정
RESOURCE_SERVER_DIR="$PROJECT_ROOT/resource_server"  # 잘못된 경로 수정
RESOURCE_GRPC_SERVER_SCRIPT="$RESOURCE_SERVER_DIR/grpc_server.py"
RESOURCE_DJANGO_MANAGE_SCRIPT="$RESOURCE_SERVER_DIR/manage.py"

# PYTHONPATH 설정 (src 디렉토리)
export PYTHONPATH="$PROJECT_ROOT/src"

# 현재 디렉토리를 Resource 서버 디렉토리로 변경
cd "$RESOURCE_SERVER_DIR" || exit  # 경로가 올바른지 확인

# 가상 환경 활성화
source .venv/bin/activate

# Resource 서버의 gRPC 서버와 Django 서버를 백그라운드에서 실행
echo "Starting gRPC Server for Resource Server..."
PYTHONPATH="$PYTHONPATH" python grpc_server.py &
GRPC_PID=$!

echo "Starting Django Server for Resource Server..."
PYTHONPATH="$PYTHONPATH" python manage.py runserver 9999 &
DJANGO_PID=$!

# Ctrl+C를 누를 때 모든 서버 종료
trap "echo 'Stopping servers...'; kill $DJANGO_PID $GRPC_PID; wait" SIGINT

# 백그라운드에서 실행된 모든 프로세스를 기다립니다.
wait