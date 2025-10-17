# Link Shortener

A URL shortening service built with Flask and PostgreSQL.

## Project Structure
```
├── app/
│   ├── app.py              # Main Flask application
│   └── requirements.txt    # Python dependencies
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile             # Dockerfile for the web application
└── README.md             # This file
```

## Prerequisites

- Docker and Docker Compose
- Python 3.14 (for local development)
- Poetry (optional, for local development)

## Getting Started

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/carol-frl/link-shortener.git
   cd link-shortener
   ```

2. Start the application using Docker Compose:
   ```bash
   docker-compose up --build -d
   ```

   This will:
   - Build the web application container
   - Start a PostgreSQL database container
   - Create necessary volumes for data persistence
   - Set up the network between containers

3. The application will be available at `http://localhost:5000`

### Local Development

1. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
   
   Or using pip:
   ```bash
   pip install -r app/requirements.txt
   ```

2. Set up PostgreSQL locally and configure the connection in your environment variables.

3. Run the Flask application:
   ```bash
   python app/app.py
   ```

## Environment Variables

The following environment variables can be configured:

- `DATABASE_URL`: PostgreSQL connection string
- Other environment variables as needed

## Docker Compose Services

- `web`: Flask application container
- `db`: PostgreSQL database container

## Database

The application uses PostgreSQL for data storage. The database schema and migrations will be handled automatically when the application starts.

## License
