#!/bin/bash

# 가상 환경 활성화
source .venv/bin/activate

# Django 서버 실행 (백그라운드)
echo "Starting Django server on port 8888..."
python manage.py runserver 8888 &
DJANGO_PID=$!

# gRPC 서버 실행 (백그라운드)
echo "Starting gRPC server on port 50051..."
python grpc_server.py &
GRPC_PID=$!

# Ctrl+C를 누를 때 모든 서버 종료
trap "echo 'Stopping servers...'; kill $DJANGO_PID $GRPC_PID; wait" SIGINT

# 백그라운드에서 실행된 모든 프로세스를 기다립니다.
wait