# base image
FROM python:3.11-slim

# working directory
WORKDIR /app


# copy the requirements file into the image
COPY requirements.txt .

# run the command to install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application
COPY . .

# expose both ports: 8000 (API) and 8501 (Streamlit)
EXPOSE 8000 8501

# make startup script executable
RUN chmod +x start.sh

# run both services
CMD ["bash", "start.sh"]