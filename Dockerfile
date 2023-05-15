FROM python:3.11.3-slim

COPY main.py /main.py

ENTRYPOINT ["python3", "/main.py"]
