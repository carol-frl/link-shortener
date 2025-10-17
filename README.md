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

### Docker Commands Reference

#### Basic Commands
```bash
# Start containers in the background
docker-compose up -d

# Start containers and force rebuild
docker-compose up --build -d

# Stop containers
docker-compose down

# Stop containers and remove volumes (will delete database data)
docker-compose down -v

# View running containers
docker-compose ps

# View logs
docker-compose logs

# View logs for a specific service
docker-compose logs web  # For the web service
docker-compose logs db   # For the database service

# Follow logs in real-time
docker-compose logs -f
```

#### Container Management
```bash
# Restart all services
docker-compose restart

# Restart a specific service
docker-compose restart web
docker-compose restart db

# Execute commands in the web container
docker-compose exec web bash
docker-compose exec web python

# View container resource usage
docker stats
```

#### Database Operations
```bash
# Access PostgreSQL CLI
docker-compose exec db psql -U postgres

# Backup database
docker-compose exec db pg_dump -U postgres > backup.sql

# Restore database
docker-compose exec -T db psql -U postgres < backup.sql
```

### Docker Compose Configuration

The project uses Docker Compose to manage two services:

1. `web` service:
   - Built from the local Dockerfile
   - Runs the Flask application
   - Exposes port 5000
   - Depends on the database service

2. `db` service:
   - Uses PostgreSQL image
   - Persists data using Docker volumes
   - Exposes port 5432 (database)
   - Configured with environment variables

### Troubleshooting Docker Issues

1. If containers won't start:
   ```bash
   # Check logs for errors
   docker-compose logs
   
   # Verify no port conflicts
   docker-compose ps
   
   # Try rebuilding
   docker-compose up --build -d
   ```

2. If database connection fails:
   ```bash
   # Check if database container is running
   docker-compose ps
   
   # Check database logs
   docker-compose logs db
   
   # Verify environment variables
   docker-compose config
   ```

3. For permission issues:
   ```bash
   # Check volume permissions
   ls -la $(docker volume inspect link-shortener_pgdata -f '{{ .Mountpoint }}')
   
   # Reset volume permissions if needed
   docker-compose down -v
   docker-compose up -d
   ```

### Local Development

#### Using Poetry (Recommended)

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Configure Poetry to create virtual environments in the project directory:
   ```bash
   poetry config virtualenvs.in-project true
   ```

3. Install project dependencies:
   ```bash
   poetry install
   ```

4. Activate the virtual environment:
   ```bash
   poetry shell
   ```

5. Add new dependencies when needed:
   ```bash
   poetry add package-name    # Add a new package
   poetry add --dev package-name    # Add a development dependency
   ```

6. Export dependencies to requirements.txt (for Docker or non-Poetry users):
   ```bash
   poetry run pip freeze > app/requirements.txt
   ```

#### Using pip

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix or MacOS
   # Or
   .\venv\Scripts\activate  # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

#### Running the Application

1. Set up PostgreSQL locally and configure the connection in your environment variables.

2. Run the Flask application:
   ```bash
   # If using Poetry:
   poetry run python app/app.py
   # Or
   # If using pip:
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
