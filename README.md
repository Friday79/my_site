## Project Overview
This project is a full-stack web application, designed to allow users to post, read, edit, comment, and interact with news stories in a Reddit-style format. The site aims to foster a community where users can discuss news topics.Users can upvote/downvote posts, and categorize content by topics. To run the server in the terminal,  writing python3 manage.py runserver and open the  browser. To access the admin panel, put slash(/)after the url of the page and write admin. In the top left corner of the home page,is the title Newsletters which when click upon it will return you to the home page, if you are not on home page. Click on  Register on the navbar if you are not a register user and then login to access the the page.To write a comment, upvote/downvote or update/delete post, first click on the post title, then post details will appear where you vote and comment can also edit or delete post. Then click on home or Newsletters to go back to the home page. On the admin page, click on post. On the right corner click add to add a post, fill the blank form ,then add image and savs. On admin panel, click on comment to see the comments, then you can approve the comments in the Admin page.

![image](https://github.com/user-attachments/assets/4ffc207e-5446-4c08-b7d6-431deec8cfa1)


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
 - ![image](https://github.com/user-attachments/assets/a3622d5e-3e19-431a-88b9-0175bd121ab6)
 - If User already exist it shows.
 - ![image](https://github.com/user-attachments/assets/91d1f8b8-6f78-4e04-bbad-1c4751a1b734)
- On logout it shows .
- ![image](https://github.com/user-attachments/assets/7f010c61-b630-45a4-8043-3fcc8202ea3f)
- Login with incorrect credentials .
- ![image](https://github.com/user-attachments/assets/bd82d386-7370-4a87-99e8-abd27dd0663d)
+ Create, edit, and delete posts.
+ Upvote/downvote posts.
+ Leave comments on posts.
- Appove comment in admin.
- ![image](https://github.com/user-attachments/assets/afb92961-4773-4989-a3b2-268cfc288c09)
- ![image](https://github.com/user-attachments/assets/c9e77aa0-8a1c-4ddb-93cb-13c369ca6b47)
+ View post details, including time and date of posting.
![image](https://github.com/user-attachments/assets/a80e45ab-f5ec-4602-98e0-c13aeb5e46f6)
2. Admin Features:
- ![image](https://github.com/user-attachments/assets/169d02d2-63a5-489f-a38e-65f3ffa6b027)
- ![image](https://github.com/user-attachments/assets/5a6d8b7f-5560-446a-935a-4e55c0decf2d)
+ Create, edit, and delete posts.
- ![image](https://github.com/user-attachments/assets/0de37b55-4eae-4be1-b178-5f2c764393ef)
## Signup 
+ ![image](https://github.com/user-attachments/assets/39cd18db-e846-4a75-8f7a-55ae78e4bfd1)
## Subscring with already existing email.



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
## Test_models.py.
- ![image](https://github.com/user-attachments/assets/c4998492-b0c0-43d2-9b08-1dca1140e0fe)
## Added Test_form.py.
- ![image](https://github.com/user-attachments/assets/07f3d6cb-492f-4a18-a573-e83c5319a1bb)
  - Add impot env to wsgi & asgi then switch to first database url in setting.py for testing
  - After testing switch everything back again for production. 

 -python manage.py test: 
 ## Validation Css
- ![image](https://github.com/user-attachments/assets/a69e3a03-c4dc-47b4-a486-e9557333f689)

## Validation HTML with source page enter on W3C validation
- ![image](https://github.com/user-attachments/assets/1b5322a0-ccde-4077-b59c-8609bb619705)

## Forms:
- Validate form inputs for creating/editing posts and comments.
##Navigation:
-Ensure all links and buttons are functional.
## Responsive Design:
- Test layout on various screen sizes.
## Desktop view.
- ![image](https://github.com/user-attachments/assets/a1f98e7d-aff6-4366-a2ac-40d37ea200b0)
## Mobile s-320px view.
- ![image](https://github.com/user-attachments/assets/f683b83b-55ff-4581-bb0e-6e68d84f4a59)
## Create post form on 320px screeen.
- ![image](https://github.com/user-attachments/assets/96aa9ed5-7467-4ab8-9352-49d2d1fc984e)

## Agile Development Process.
- ![image](https://github.com/user-attachments/assets/5bc69785-0f94-497a-9e17-ebee01905aa6)
Epics:
User account management.
Post and comment management
## UX Design
- Design Principle.
- Wireframes:
## Desktop Nav Bar View.
- +----------------------------------------------------------------------------------+
| Newsletters|blog               Home   Travel   Health   Technology   Science     |
|                                                                 Create Post Logout|
+----------------------------------------------------------------------------------+

## Mobile Nav Bar View.
- +------------------------------------------------+
| Newsletters|blog                    ☰ (menu)   |
+------------------------------------------------+
                 ↓ Dropdown (on click) ↓
--------------------------------------------------
| Home                                            |
| Travel                                          |
| Health                                          |
| Technology                                      |
| Science                                         |
| Create Post                                     |
| Logout                                          |
--------------------------------------------------

## Creating post on large screen View.
- +--------------------------------------------------------------------------------+
| Navbar: Newsletters | blog   Home  Travel  Health  Tech  Science   Create Logout |
+--------------------------------------------------------------------------------+
|                                  Create New Post                               |
| Title:   [__________________________]                                          |
| Slug:    [__________________________]                                          |
| Category:[__________▼]                                                         |
| Image:   [Choose File]                                                         |
| Excerpt: [___________________________________________________________]         |
| Content: [___________________________________________________________]         |
|          [___________________________________________________________]         |
| Status:  [ Draft ▼ ]                                                           |
|                                                                                |
|                        [ Publish Button ]                                      |
+--------------------------------------------------------------------------------+
| Footer: Made by us | Social icons [FB][TW][IG][YT] | Subscribe [____][Button]  |
+--------------------------------------------------------------------------------+

## Creating post on Mobile view.
- +------------------------------------------------+
| Navbar: Logo | ☰                                |
+------------------------------------------------+
|                Create New Post                 |
| Title:   [_____________]                        |
| Slug:    [_____________]                        |
| Category:[____▼]                                |
| Image:   [Choose File]                          |
| Excerpt: [_____________]                        |
|          [_____________]                        |
| Content: [_____________]                        |
|          [_____________]                        |
| Status:  [ Draft ▼ ]                            |
|                                                |
|            [ Publish Button ]                  |
+------------------------------------------------+
| Footer: Made by us                             |
| [FB][TW][IG][YT]                               |
| Subscribe: [____ Enter email ____][Subscribe]  |
+------------------------------------------------+

## Home page for large screen.
- +--------------------------------------------------------------------------------+
| Navbar: Newsletters | blog   Home Travel Health Tech Science   Register Login  |
+--------------------------------------------------------------------------------+
|                             Browse by Category                                |
+--------------------------------------------------------------------------------+
| [Image]  Author: Friday   Title: Risk with gmos                               |
|          Short excerpt text...                                                |
|          Date, Time   ♥ count                                                 |
+--------------------------------------------------------------------------------+
| [Image]  Author: Friday   Title: Gmos and Evolution                           |
|          Short excerpt text...                                                |
|          Date, Time   ♥ count                                                 |
+--------------------------------------------------------------------------------+
| [Image]  Author: Friday   Title: Herbal medicine supplement                   |
|          Short excerpt text...                                                |
|          Date, Time   ♥ count                                                 |
+--------------------------------------------------------------------------------+
| [Image]  Author: Friday   Title: Old method of Agriculture                    |
|          Short excerpt text...                                                |
|          Date, Time   ♥ count                                                 |
+--------------------------------------------------------------------------------+
| [Image]  Author: Friday   Title: Sustainable Agriculture                      |
|          Short excerpt text...                                                |
|          Date, Time   ♥ count                                                 |
+--------------------------------------------------------------------------------+
| [Image]  Author: Friday   Title: Robotic and manufacturing                    |
|          Short excerpt text...                                                |
|          Date, Time   ♥ count                                                 |
+--------------------------------------------------------------------------------+
| Pagination: < PREV   NEXT >                                                   |
+--------------------------------------------------------------------------------+
| Footer: Made by us | Social icons [FB][TW][IG][YT] | Subscribe bar            |
+--------------------------------------------------------------------------------+

## Home page for mobile screen.
- +------------------------------------------------+
| Navbar: Logo | ☰                                |
+------------------------------------------------+
|            Browse by Category                  |
+------------------------------------------------+
| [no Image]                                        |
| Author: Friday                                 |
| Title: Risk with gmos                          |
| Short excerpt text...                          |
| Date, Time   ♥ count                           |
+------------------------------------------------+
| [no Image]                                        |
| Author: Friday                                 |
| Title: Gmos and Evolution                      |
| Short excerpt text...                          |
| Date, Time   ♥ count                           |
+------------------------------------------------+
| [no Image]                                        |
| Author: Friday                                 |
| Title: Herbal medicine supplement              |
| Short excerpt text...                          |
| Date, Time   ♥ count                           |
+------------------------------------------------+
| ... (Remaining posts stacked vertically)       |
+------------------------------------------------+
| Pagination: < PREV   NEXT >                    |
+------------------------------------------------+
| Footer: Made by us                             |
| [FB][TW][IG][YT]                               |
| Subscribe: [____ Enter email ____][Subscribe]  |
+------------------------------------------------+

- Navbar: Dark background with orange highlight on "letters" (logo). Active page (Home) underlined/white.

- Main Title: "Browse by Category" centered, large font (h2).

- Post Cards:

- Image at the top, full-width.

- Author tag (teal background, white text).

- Post title bold, excerpt truncated (2–3 lines).

- Metadata: date, time, likes aligned at the bottom.

## Grid Layout:

- Desktop → 3-column grid.

- Tablet → 2-column grid.

- Mobile → 1-column stacked.

- Pagination: Simple buttons (Previous, Next). Highlight current page.

## Footer:

- Dark background, centered social icons.

- Newsletter subscription with email field + blue "Subscribe" button.


- ![image](https://github.com/user-attachments/assets/9d1a42ad-c82b-4851-9a37-3ba86068ef09)



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
