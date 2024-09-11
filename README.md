
# ERD diagram
![auth](https://github.com/user-attachments/assets/2b37e422-9724-411a-8df3-848c1d47d1d2)
![resource](https://github.com/user-attachments/assets/11e684b4-8023-4c41-b7fc-fcb9e932e4cf)

# 디렉토리 구조
<details><summary>펼처보기</summary>



```
.
├── .DS_Store
├── .docker-compose.yml
├── .env
├── .vscode
│   └── settings.json
├── LICENSE
├── README.md
├── certificates
│   ├── .DS_Store
│   ├── ap-northeast-2-bundle.pem
│   └── hess-ec2-keypair3.pem
├── nginx
│   └── Dockerfile
├── nginx.conf
├── scripts
│   └── run_all_servers.sh
├── src
│   ├── .DS_Store
│   ├── auth_server
│   │   ├── .DS_Store
│   │   ├── .venv
│   │   ├── .vscode
│   │   │   └── settings.json
│   │   ├── Dockerfile
│   │   ├── __pycache__
│   │   ├── accounts
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── migrations
│   │   │   │   └── __init__.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── auth_pb2.py
│   │   ├── auth_pb2_grpc.py
│   │   ├── auth_server
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   ├── asgi.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── grpc_server.py
│   │   ├── manage.py
│   │   ├── poetry.lock
│   │   ├── proto
│   │   │   └── auth.proto
│   │   ├── pyproject.toml
│   │   ├── start_auth_servers.sh
│   │   └── test_grpc_server.py
│   └── resource_server
│       ├── .venv
│       ├── .vscode
│       │   └── settings.json
│       ├── Dockerfile
│       ├── __pycache__
│       ├── auth_pb2.py
│       ├── auth_pb2_grpc.py
│       ├── grpc_client.py
│       ├── grpc_server.py
│       ├── manage.py
│       ├── orders
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── migrations
│       │   │   ├── 0001_initial.py
│       │   │   ├── __init__.py
│       │   │   └── __pycache__
│       │   ├── models.py
│       │   ├── serializers.py
│       │   ├── tests.py
│       │   ├── urls.py
│       │   └── views.py
│       ├── poetry.lock
│       ├── products
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── migrations
│       │   │   ├── 0001_initial.py
│       │   │   ├── __init__.py
│       │   │   └── __pycache__
│       │   ├── models.py
│       │   ├── serializers.py
│       │   ├── tests.py
│       │   ├── urls.py
│       │   └── views.py
│       ├── pyproject.toml
│       ├── resource_server
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   ├── asgi.py
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       └── start_resource_servers.sh
└──.gitignore
```



</details>