FROM debian:stable-slim

# no extra tools, only for execute and bash
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# user without privileges
RUN useradd -m -s /bin/false sandbox
USER sandbox
WORKDIR /home/sandbox

#Everything is assembled at runtime; we keep the base FS clean.
