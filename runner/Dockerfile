FROM debian:stable-slim

# minimum packages: g++, python for the API and utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    g++ make python3 python3-pip ca-certificates procps time \
    && rm -rf /var/lib/apt/lists/*

# install FastAPI + Uvicorn
RUN pip3 install fastapi uvicorn pydantic

# create a new user without privileges
RUN useradd -m -s /bin/false runner
USER runner
WORKDIR /home/runner/app

# copy the API
COPY app.py /home/runner/app/app.py

#launch the API
EXPOSE 8000
CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8000"]
