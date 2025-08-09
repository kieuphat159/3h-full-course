# mini-blog-project

A Django blog project following a YouTube tutorial.

## Project Structure

- `myproject/` - Main Django project folder
  - `manage.py` - Django management script
  - `myproject/` - Project settings and configuration
  - `posts/` - Blog post app
  - `users/` - User authentication app
  - `static/` - Static files (CSS, JS)
  - `media/` - Uploaded media files
  - `templates/` - Shared HTML templates

## Setup (Local)

1. **Clone the repository**

2. **Install dependencies**

   Make sure you have Python 3 and pip installed.

   ```sh
   pip install -r requirements.txt
   ```

3. **Apply migrations**

   ```sh
   python myproject/manage.py migrate
   ```

4. **Create a superuser (optional, for admin access)**

   ```sh
   python myproject/manage.py createsuperuser
   ```

5. **Run the development server**

   ```sh
   python myproject/manage.py runserver
   ```

6. **Access the app**

   Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Setup with Docker

1. **Install Docker Desktop** (if not already installed)

2. **Build and run the containers**

   ```sh
   docker-compose up --build
   ```

3. **Apply migrations inside the container**

   ```sh
   docker-compose exec web python myproject/manage.py migrate
   ```

4. **Create a superuser inside the container (optional)**

   ```sh
   docker-compose exec web python myproject/manage.py createsuperuser
   ```

5. **Access the app**

   Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Notes

- Static files are in `static/`
- Media uploads are in `media/`
- Update `requirements.txt` to include all Python dependencies for deployment.
- Make sure your `templates` folder is at the project root and your `settings.py` uses `BASE_DIR / 'templates'` for the `DIRS` setting in `TEMPLATES`.

---
