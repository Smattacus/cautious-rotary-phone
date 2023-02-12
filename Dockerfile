FROM python:3.7-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY simple_client.py simple_client.py
RUN pip install requests
CMD ["python", "simple_client.py"]