# Use the official Debian image as the base image
FROM debian:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y fortune cowsay netcat-openbsd && \
    apt-get clean

# Add /usr/games to PATH
ENV PATH="/usr/games:${PATH}"

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY wisecow.sh /app/wisecow.sh

# Make the script executable
RUN chmod +x /app/wisecow.sh

# Expose the port the server will run on
EXPOSE 4499

# Run the script
CMD ["/app/wisecow.sh"]
