## Project Overview
This project is a full-stack web application, designed to allow users to post, read, edit, comment, and interact with news stories in a Reddit-style format. The site aims to foster a community where users can discuss news topics.Users can upvote/downvote posts, and categorize content by topics. To run the server in the terminal,  writing python3 manage.py runserver and open the  browser. To access the admin panel, put slash(/)after the url of the page and write admin. In the top left corner of the home page,is the title Newsletters which when click upon it will return you to the home page, if you are not on home page. Click on  Register on the navbar if you are not a register user and then login to access the the page.To write a comment, upvote/downvote or update/delete post, first click on the post title, then post details will appear where you vote and comment can also edit or delete post. Then click on home or Newsletters to go back to home page. On the admin page, click on post. On the right corner click add to add a post, fill the blank form ,then add image and savs. On admin panel, click on comment to see the comments, then you can approve the comments in the Admin page.

![image](https://github.com/user-attachments/assets/0f2a3087-101a-4f10-8c7f-2959766227d8)


## Table of Contents
1. Purpose and Goals
2. Features
3. Technologies Used
4. Installation and Setup
5. Deployment
6. Data Model
7. Testing
8. Agile Development Process
9. UX Design
10. Security Considerations
11. Future Enhancements
## Purpose and Goals
### User Goals:
- Post, read,update/delete and comment on news stories.
- Interact with posts through upvotes and downvotes.
- Navigate topics to find relevant news.
### Site Owner Goals:
- Create an engaging and user-friendly community platform.
- Encourage user interaction and meaningful discussions.
- Moderate content effectively.
## Features
1. User Features:

- Account registration and login/logout.
 - ![image]()
+ Create, edit, and delete posts.
+ Upvote/downvote posts.
+ Leave comments on posts.
+ View post details, including time and date of posting.
2. Admin Features:
  + Create, edit, and delete posts.
## Signup 
  + ![image](https://github.com/user-attachments/assets/39cd18db-e846-4a75-8f7a-55ae78e4bfd1)


+ Moderate posts and comments.
+ Approve or disapprove user-generated content.
## Technologies Used
1. Frontend:
- HTML5, CSS3, JavaScript (ES6).
- Responsive design with Bootstrap.
2. Backend:
- Python, Django Framework.
- Django Templates for dynamic content.
3. Database:
- PostgreSQL (production) and SQLite (development).
4. Version Control:
- Git and GitHub.
5. Deployment:
. Heroku (or similar cloud-based platform).
## Installation and Setup
1. Clone the repository:
-  git clone <repository_url>
2. Navigate to the project directory:
 . cd restaurant
3. Create and activate a virtual environment:
. python3 -m venv env
. source env/bin/activate  # On Windows: env\Scripts\activate
4.Install dependencies:
- pip install -r requirements.txt
5. Set up environment variables (e.g., in .env file):
- SECRET_KEY=your_secret_key
- DEBUG=True
- DATABASE_URL=your_database_url
6.Run database migrations:
- python manage.py migrate
7. Start the development server:
- python manage.py runserver
## Deployment
### Steps to Deploy to Heroku:
1. Create a Heroku app.
2. Set up environment variables on Heroku.
3. Push the code to the Heroku remote repository.
4. Run migrations on Heroku:
- heroku run python manage.py migrate
5. Test the deployment to ensure functionality.
## Data Model
1. User Model:
- Extends Django's default User model for authentication.
2. Post Model:
- Title, content, author, timestamp, category, upvotes, downvotes.
3. Comment Model:
- Content, author, timestamp, related post.

## Testing
- Run unit tests:
  - Add impot env to wsgi & asgi then switch to first database url in setting.py for testing
  - After testing switch everything back again for production. 

 -python manage.py test: 
 ## Validation Css
- ![image](https://github.com/user-attachments/assets/a69e3a03-c4dc-47b4-a486-e9557333f689)

## Validation HTML
- ![image](https://github.com/user-attachments/assets/1b5322a0-ccde-4077-b59c-8609bb619705)

## Forms:
- Validate form inputs for creating/editing posts and comments.
##Navigation:
-Ensure all links and buttons are functional.
## Responsive Design:
- Test layout on various screen sizes.

## Agile Development Process
Epics:
User account management.
Post and comment management
## UX Design
- Design Principle.
- Wireframes:

- ![image](https://github.com/user-attachments/assets/9717e60f-4eb6-4dac-8383-c524cb89e89f)



## Security Considerations
- Passwords hashed using Django's authentication system.
- Environment variables for sensitive data.
- User permissions for role-based access control.
- Use DEBUG=False in production.

Use Whitenoise for static file management.

Enable SSL/TLS for secure connections.

Use Cloudinary.
## Future Enhancements
- Real-time Updates:

## Acknowledgments
- The Django documentation.
- Code Institute for guidance and resources.
