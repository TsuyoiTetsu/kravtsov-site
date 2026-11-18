FROM python:3.15.0
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 8016
CMD ["python", "app.py"]