#
# docker build -t wordcount-app .
# docker run --rm -v "$PWD/data/input:/data/input/" -v "$PWD/data/output:/data/output/" wordcount-app
#
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -e .
# python3 -m homework data/input data/output
CMD ["python", "-m", "homework", "/data/input/", "/data/output/"]

