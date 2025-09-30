# TaskApi

**TaskApi** — this is app for tasks management. The API give provides the ability to create, get, patch and delete tasks.

## Key Features

- **Creating task**: POST `/post/` to create a new task with its title and description.
- **Getting data**:
  - GET `/tasks/<id>/` — to get a task by its ID.
  - GET `/task/` — to get list with all tasks.
- **Patching task**: PATCH `/tasks/{task_id}/update/` to patch a task.
- **Deleting task**: DELETE `/tasks/{task_id}/delete/` to delete a task by its id
- **Swagger UI**: Interactive API documentation is available at `/docs/`.

## Technologies

- **Backend**: FastApi
- **Data Base**: PostgreSQL


## Installing

1. **Clone repository**:
   ```bash
   git clone https://https://github.com/ADediche//TaskApi.git
   cd MountainPasses
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\scripts\activate  # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the environment**:
   Create file `.env` in project folder:
   ```
   DB_CONNECT=url-strring for database connect
   ```

5. **Start app**:
   ```bash
   python main.py
   ```

## Using

- **API**: Available at `http://127.0.0.1:8000/`.
- **Swagger UI**: open `http://127.0.0.1:8000/docs/` for a looking and testing endpoints.

## Contacts

- **Author**: Alekei Dedichenko
- **Email**: dedichenkoa@gmail.com
- **GitHub**: https://github.com/ADediche
