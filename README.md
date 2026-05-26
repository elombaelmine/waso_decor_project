#Waso Decor Project
    Welcome to the Waso Decor Management System. This application provides a platform for managing decor gallery items, customer inquiries, and testimonials. It is built with a decoupled architecture featuring a Django REST Framework backend and an Angular frontend.

🚀 Live Demo
    Backend API: [https://waso-decor-project-backend.onrender.com]

    Frontend: [https://waso-decor-project-frontend.vercel.app]

🛠 Tech Stack
    Backend: Django, Django REST Framework, PostgreSQL, Gunicorn, Whitenoise.

    Frontend: Angular, RxJS.

Services: Render (Backend Deployment),Vercel (Frontend Deployment) Brevo (Emailing), JWT (Authentication).

📋 Features
    Role-Based Admin Dashboard: Secure management of gallery content and user feedback.

    Persistent PostgreSQL Storage: Reliable cloud database for all business data.

    Automated CI/CD: Seamless production deployment using a custom build.sh script.

    Token-Based Security: Protected endpoints using JSON Web Tokens (JWT).

⚙️ Installation & Setup
    Prerequisites
    Python 3.x

    Node.js & Angular CLI

    PostgreSQL

Backend Setup
    Clone the repository: git clone [(https://github.com/elombaelmine/waso_decor_project.git)]

    Navigate to the backend: cd backend

    Create a virtual environment: python -m venv venv

    Activate it: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)

    Install dependencies: pip install -r requirements.txt

    Set your environment variables (see below).

    Run the server: python manage.py runserver

Frontend Setup
    Navigate to the frontend: cd frontend

    Install dependencies: npm install

    Run the application: ng serve


🏗 Deployment
    This project is automatically deployed on Render. The build process is handled by a custom build.sh script in the root directory, which automatically installs dependencies, runs database migrations, collects static files, and initializes the admin user.While the user-view deployed on vercel succesfully.

Created for [DjangoProject][ELOMBA ELMINE]