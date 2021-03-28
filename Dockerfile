FROM ubuntu:latest

#Avoid prompting for timezone nginx setup
ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

## Step 1:
# Create a working directory
WORKDIR /app/
## Step 2:
# Copy source code to working directory
COPY . /app/
## Step 3:
#Update OS libraries
RUN apt update
RUN apt -y upgrade
RUN apt -y install make wget python3 python3-pip
RUN apt -y install -y nginx
## Step 4:
# Install App
RUN make install
## Step 5
#Copy nginx configurarion for reverse proxy
COPY ./nginx/nginx.conf /etc/nginx/sites-enabled/default
## Step 6:
# Expose port 
EXPOSE 80
## Step 5:
# Run  bokeh server at container launch
CMD ["./start.sh"]