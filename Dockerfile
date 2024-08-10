FROM python:3.9-bookworm

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

EXPOSE 8000

# make entrypoint.sh executable by adding executable permission to file
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]