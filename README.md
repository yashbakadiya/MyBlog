# Django Blog and User Authentication Project

This project is a web application built with Django, featuring a blog and user authentication system. It allows users to register, log in, reset passwords, and manage profiles, along with creating and viewing blog posts.

---

## Features

- **User Authentication**: 
  - Register, login, and logout.
  - Password reset functionality with email confirmation.
  - Profile management.

- **Blog**: 
  - Separate app for blog-related routes and functionality.
  - Easily extendable for creating, editing, and viewing blog posts.

---

## Project Structure

### Main URL Configuration (`urls.py`)

The project routes are configured as follows:
- **Admin Panel**: Accessible at `/admin/`.
- **User Authentication**:
  - **Registration**: `/register/`
  - **Login**: `/login/`
  - **Logout**: `/logout/`
  - **Profile**: `/profile/`
  - **Password Reset**:
    - Start: `/password-reset/`
    - Confirmation: `/password-reset-confirm/<uidb64>/<token>/`
    - Success message: `/password-reset/done/`
- **Blog**: URL patterns are included from the `blog` app.

---

## Getting Started with Your Django Project

### 1\. **Set up a Virtual Environment** (Recommended)

First, let's create and activate a virtual environment to isolate your project dependencies:

```
# Create a virtual environment python -m venv myEnv  # Activate it (Windows) myEnv\Scripts\activate  # Or if you're using Git Bash or WSL source myEnv/Scripts/activate
```

### 2\. **Install Dependencies**

Once your virtual environment is activated, install the required packages:


```
pip install -r requirements.txt
```

### 3\. **Set up Environment Variables**

I notice your project uses environment variables for sensitive data. Create a `.env` file in your project root with:

```
SECRET_KEY=your-secret-key-here
EMAIL=your-email@gmail.com
PASSWORD=your-app-password
```

### 4\. **Run Database Migrations**

Set up your database by running migrations:

```
python manage.py makemigrations
python manage.py migrate
```

### 5\. **Create a Superuser** (Optional)

Create an admin user to access the Django admin panel:


```
python manage.py createsuperuser
```

### 6\. **Start the Development Server**

Run your Django development server:

```
python manage.py runserver
```

Your application should now be running at `http://127.0.0.1:8000/` or `http://localhost:8000/`

- - -

## Project Overview

Based on the code I examined, this appears to be a **blog application** with:

*   **Blog functionality**: Create, read, update, and delete blog posts
    
*   **User authentication**: Registration, login, logout, password reset
    
*   **User profiles**: Profile management with image uploads
    
*   **Static files**: CSS styling and media file handling
    
*   **Email functionality**: For password resets
    
*   **Heroku deployment ready**: With Procfile and whitenoise for static files
    

- - -

## Key Features Available

1.  **Home page** - Main blog listing
    
2.  **User registration/login** - Account management
    
3.  **Blog post management** - CRUD operations for posts
    
4.  **User profiles** - Profile pictures and user information
    
5.  **Contact page** - Contact functionality
    
6.  **Explore page** - Browse posts
    

- - -

## Next Steps

1.  Run the commands above to get started
    
2.  Visit `http://localhost:8000/admin/` to access the Django admin panel
    
3.  Create some blog posts through the admin or the web interface
    
4.  Test the user registration and login functionality
    

Would you like me to help you with any specific part of the setup, or do you have questions about any particular feature of your Django project?
