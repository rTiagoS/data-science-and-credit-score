# Use python 3.6 image as base for the new image.
FROM python:3.8

# Adds metadata to the image
LABEL maintainer = "Tiago Sá tiago.ramos121@gmail.com"
LABEL version = "0.1"
LABEL description = "Streamlit app for datascience projects"

# Use this path as the default location for all subsequent commands
WORKDIR /app

# Copy requerements.txt requirements.txt
COPY requirements.txt requirements.txt
COPY modules/ modules/
COPY markdowns/ markdowns/
COPY figures/ figures/
COPY constants.py constants.py
COPY main.py main.py

RUN pip3 install -r requirements.txt

# Expose port to listen for incoming requests
EXPOSE 8501


ENTRYPOINT [ "streamlit", "run" ]

CMD ["main.py"]