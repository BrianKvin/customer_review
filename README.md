# Customer Review/Feedback Application
![Customer Review Logo](https://previews.123rf.com/images/valentint/valentint1610/valentint161004490/65580547-customer-reviews-icon-internet-button-on-white-background.jpg)

> This Flask application allows customers to review retailers, send the data to PostgreSQL and email retailers.
## Installing depenencies
- pip -V or pip --version
- Install pip ***python3 get-pip.py***
- Upgrade pip ***pip install --upgrade pip setuptools***
- Set up a virtual environment ***python3 -m venv venv***
- Activate the virtual environment ***source venv/bin/activate***
- Install Flask ***pip install Flask***
- Install Flask SQLAlchemy ***pip install -U Flask-SQLAlchemy***
- Install PostgreSQL ***sudo apt install postgresql***
- Start postgresql ***sudo service postgresql start***
- Install psycopg2 ***pip install psycopg2***
- Interact with database with postgresql ***export FLASK_APP=review***
- Access interactive mode with PostgreSQL ***flask shell***

## Resources
1. [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
2. [Developing RESTful APIs with Python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
3. [The Application Context](https://flask.palletsprojects.com/en/2.3.x/appcontext/)
4. [How to use Python virtual environment](https://stackoverflow.com/questions/35017160/how-to-use-virtualenv-with-python)
5. [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## How the Project Works
> Feedback not only gives insight into satisfaction levels, but also provides a powerful metric for addressing customer issues, preventing churn, and building a base for loyal clientele. Organizations that actively seek customer feedback gain a competitive edge in improving products and services from the perspective of their customers. The diverse, empowered, and digitally connected nature of customers today makes it imperative to view business from the prism of what is important to customers and augment products and services to the insatiable wants. I was inspired to work on a customer-feedback system to provide a guiding resource for organizations to align their strategies and initiatives with evolving needs and preferences of customers.

> I recalled a jading shopping experience that attuned me to the reprieve that customers witness on this front. This was my motivation to build a customer-review system for my portfolio that would have an indelible imprint on businesses and customers alike. While this adventure might seem a skill development project, the underlying principle is to highlight the limitless possibilities for organizations to actively engage with customer preferences and reviews and create a continuous feedback loop.

> I employed responsive web design techniques in developing the front-end section of my project. I implemented a modern UI design using HTML, CSS, and JavaScript to create an intuitive, mobile-responsive, and visually appealing interface. These web design technologies enabled me to implement user testing and incorporate feedback that enhance usability, optimize the user flow, and achieve a seamless and interactive platform.

> Flask was pivotal in my project, providing a lightweight and flexible framework for creating routes and views to handle customer feedback functionalities. I leveraged Flask to build a RESTful API that handles https requests (server-side logic), enabling holistic communication between the application’s frontend and backend components. Flask was also essential in defining API endpoints and converting Python objects into JSON responses for API requests.

> I used Flask’s database integration capabilities to efficiently store the ratings and feedback by customers and allow organizations to retrieve this information. SQLAlchemy enabled interaction with the database through CRUD operations on reviews and customers. I utilized PostgreSQL to design the database schema and establish appropriate relationships between tables using foreign keys. Integrating PostgreSQL database enabled me to write database queries and ORM models to retrieve, store, and update data.

> In handling email notifications, I set up Mailtrap to facilitate test email sending functionalities. I achieved this capability in my development environment by configuring Flask’s email functionalities using the Mailtrap SMTP setting. Mailtrap service embodied the entire feedback process by notifying customers and when reviews are submitted.

> I did not anticipate radical challenges in accomplishing the project owing to the adroit support from peers and succinctly planning.  Nevertheless, the implementation was not without challenges. I often caught errors connecting to my database, notably (RuntimeError: Working outside of application context.). I resolved this by exporting Flask App (export FLASK_APP=<filename>) and interacting with the database using flask shell. I must say logging and error handling techniques helped me debug most issues during testing by capturing and handling exceptions to ensure the system functioned as intended.

> Overall, I learned that understanding the required modules and adapters may seem a frill rather than a necessity when starting projects but the practice could actually be a game changer. Likewise, creating a virtual environment for Python projects provides a powerful amulet for wadding off dependency conflicts and system-wide package interference.
[My GitHub link to this project](https://github.com/BrianKvin/customer_review). 

> There is room for improvement in creating a route that will allow retailers to register in the system for review and view feedback on a feedback page

> I’m Kelvin, investing my time in continuous learning at ALX Africa.
> Thanks for reading!
