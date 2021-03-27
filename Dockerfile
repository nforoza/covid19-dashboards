FROM python:3.8-buster

## Step 1:
# Create a working directory
WORKDIR /app/
## Step 2:
# Copy source code to working directory
COPY . /app/

## Step 3:
# Install packages from requirements.txt
RUN make install
# hadolint ignore=DL3013

## Step 4:
# Expose port 
EXPOSE 80

## Step 5:
# Run  bokeh server at container launch
CMD ["python","/app/app.py"]