В павершел

& 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon

FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends python3-pip && rm -rf /var/lib/apt/lists/*

CMD ["python3", "--version"]
тестовий коміт