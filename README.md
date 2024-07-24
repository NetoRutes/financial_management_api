# Financial Management System

## Overview

The Financial Management System is a personal finance management application built with Django REST Framework. It provides features for managing transactions, categories, payment methods, and more. This project aims to help users track and manage their finances efficiently.

## Features

- **Transactions**: Record and manage financial transactions with details such as amount, description, date, and payment method.
- **Categories**: Organize transactions into categories for better tracking and reporting.
- **Payment Methods**: Manage different payment methods used for transactions.
- **Users**: Support for multiple users with different roles and permissions.
- **Reports**: Generate financial reports to analyze spending patterns and financial health.
- **Investments**: Future plans to include investment tracking and reporting.

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/NetoRutes/financial_management_api.git
    cd financial_management_api
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

7. **Access the Admin Panel**

    Navigate to `http://localhost:8000/admin` and log in with the superuser credentials to manage the application.

## Configuration

- **Database**: The project uses SQLite by default. To use a different database (e.g., PostgreSQL), update the `DATABASES` settings in `settings.py`.
- **Environment Variables**: Create a `.env` file for environment-specific settings such as `SECRET_KEY`, `DEBUG`, and database credentials.

## Project Structure

- **core**: Contains user management and authentication.
- **common**: Includes common models like `Category`, `Tipo`, and `FormaPgmto`.
- **transactions**: Manages transaction records and related features.
- **reports**: Future module for financial reporting.
- **investments**: Future module for investment tracking.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding style and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [NetoRutes](https://github.com/NetoRutes).

---

Enjoy managing your finances with the Financial Management System!
