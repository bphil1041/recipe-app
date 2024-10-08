# Recipe Application

The Recipe Application is a web-based platform built using Python and the Django framework, designed to help users manage and explore a collection of recipes. Users can log in to access protected content, view a list of recipes, and get detailed information about each recipe. The application also provides an admin panel for managing recipes, allowing users to perform CRUD (Create, Read, Update, Delete) operations seamlessly.

## How to Get the Project Running

**Note:** You will need to work in a virtual environment with Django installed.

### Step 1: Create a Virtual Environment

If you have not yet created a virtual environment on your machine, you can do so using `virtualenvwrapper`. Once installed, create a new virtual environment and activate it. Then, install Django in the environment.

### Step 2: Clone the Repository

Navigate to the desired directory and clone the project repository.

### Step 3: Install Dependencies

Install the necessary Python packages from `requirements.txt`.

### Step 4: Set Up the Database

Run the Django migrations to set up the SQLite database.

### Step 5: Create a Superuser

Create an admin user to access Django's admin interface. Follow the prompts to set a username, email, and password.

### Step 6: Run the Development Server

Start the local development server. In your browser, navigate to the specified URL. You will be prompted to log in using the provided credentials.

## Features

- **Admin Panel:** Capable of performing CRUD operations on the database.
- **User Capabilities:**
  - View all recipes in a list.
  - Click on any recipe to view its details.
  - Create new recipes by entering custom information.
  - Search recipes by sorting based on difficulty.

## Technologies Used

- **Python**: The programming language used for backend development.
- **Django**: The web framework that provides the structure for the application.
- **SQLite**: The default database used for data storage.
- **HTML/CSS**: For structuring and styling the web pages.

## Screenshots

- Login Page
- Recipe List Page
- Recipe Detail Page
- Logout Success Page


