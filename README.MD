# Website Example

A fully responsive site template designed by [HTML5 UP](https://html5up.net).

This project includes a Python backend with Flask to handle feedback submissions.

## Running the application

You can run the application using Docker (recommended) or locally for simple static hosting.

This guide explains how to run the application using Docker.

#### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)

#### 1. Build the Backend Image

```bash
docker build -t python-backend .
```

#### 2. Create a Docker Network

```bash
docker network create app-network
```

#### 3. Run the Backend Container

```bash
docker run -d --name backend --network app-network python-backend
```

#### 4. Run the Nginx Container

```bash
docker run -d --name nginx -p 8181:80 --network app-network \
  -v $(pwd)/nginx.conf:/etc/nginx/conf.d/default.conf \
  -v $(pwd):/usr/share/nginx/html \
  nginx:latest
```

#### 5. Access the Application

Open your web browser and navigate to `http://localhost:8181`.

## Deployment

Before deployment, you should replace the `DEPLOYREF` placeholder in `index.html`. This is used to track the version of the deployed code.

In `index.html`, find the following line:

```html
<meta name="deployref" content="DEPLOYREF">
```

Replace `DEPLOYREF` with the actual deployment reference, for example, a git commit hash.

## Testing

The project includes a simple test script. To run the tests, execute the following command:

```bash
./test.sh
```
