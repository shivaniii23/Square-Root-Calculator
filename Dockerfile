FROM python:3.9
COPY . ./app/
WORKDIR /app
RUN apt-get update &&  apt-get install -y python3-pytest
ENTRYPOINT ["python3","sqrt.py"]
CMD ["9"]
