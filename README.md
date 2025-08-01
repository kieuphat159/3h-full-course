# 3h-full-course

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

## Setup

1. **Clone the repository**

2. **Install dependencies**

   Make sure you have Python 3 and pip installed.

   ```sh
   pip install django pillow
   ```

   Or, if you have a correct `requirements.txt`:

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

## Notes

- Static files are in `myproject/static/`
- Media uploads are in `myproject/media/`
- Update `requirements.txt` to include all Python packages used in the project.
