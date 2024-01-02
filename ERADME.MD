# Twitter Clone

**Author: [Younes Veisi]**

This is a Twitter clone project built using Django, aiming to replicate some of the core functionalities of the popular social media platform.

---

## Features

- **User Authentication**: Register and login functionalities for users.
- **Create Tweets**: Post short messages similar to tweets.
- **Follow Users**: Follow other users to see their tweets on your timeline.
- **Like and Retweet**: Interact with tweets by liking and retweeting.
- **Search Functionality**: Search for users and tweets.

---

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/younesveisi1374/Twitter.git`
2. Navigate to the project directory: `cd Twitter`
3. Create a virtual environment (optional but recommended): `python -m venv .venv`
4. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS and Linux: `source .venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Make migrations: `python manage.py makemigrations`
7. Apply the database migrations: `python manage.py migrate`
8. Create a superuser: `python manage.py createsuperuser`
9. Start the development server: `python manage.py runserver`

---


## Usage

Once the development server is running, access the application at `http://localhost:8000` in your web browser. You can then register a new account, log in, and start using the Twitter clone by creating tweets, following other users, liking, retweeting, and exploring the functionalities.

To create API documentation for your Django project, you'll want to outline the endpoints and their functionalities. Based on the provided `urls.py` files, here's an example API documentation:

---

## API Endpoints

### Home View
- **URL**: `/`
- **Description**: Renders the home page of the Twitter clone.
- **Method**: GET

### New Post View
- **URL**: `/post/new`
- **Description**: Allows users to create a new post.
- **Method**: GET

### Post Detail View
- **URL**: `/post/<int:pk>`
- **Description**: Displays details of a specific post.
- **Method**: GET

### Post Update View
- **URL**: `/post/update/<int:pk>`
- **Description**: Allows users to update a specific post.
- **Method**: GET, POST

### Post Delete View
- **URL**: `/post/delete/<int:pk>`
- **Description**: Allows users to delete a specific post.
- **Method**: GET, POST

### Sign Up View
- **URL**: `/accounts/signup/`
- **Description**: Allows users to register for a new account.
- **Method**: GET, POST

---

## Views Summary

### Twitter App Views

#### HomeView
- Renders the home page displaying a paginated list of posts.
- Uses `ListView` to display posts.
- URL: `/`
- Methods: GET

#### NewPostView
- Allows logged-in users to create new posts.
- Uses `CreateView`.
- URL: `/post/new`
- Methods: GET, POST

#### PostDetailView
- Displays details of a specific post.
- Utilizes `DetailView`.
- URL: `/post/<int:pk>`
- Methods: GET

#### PostUpdateView
- Enables users to update existing posts.
- Utilizes `UpdateView`.
- URL: `/post/update/<int:pk>`
- Methods: GET, POST

#### PostDeleteView
- Allows users to delete posts.
- Uses `DeleteView`.
- URL: `/post/delete/<int:pk>`
- Methods: GET, POST

#### CommentGet and CommentPost
- Handles comments related to specific posts.
- `CommentGet` fetches the comment form.
- `CommentPost` processes posted comments.
- URL: `/post/<int:pk>` (for commenting)
- Methods: GET, POST


### Accounts App Views

#### SignUpView
- Allows users to sign up/register.
- Utilizes `CreateView`.
- URL: `/accounts/signup/`
- Methods: GET, POST

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The project was created as a learning exercise by [younesveisi1374](https://github.com/younesveisi1374).
- Inspired by the functionalities of Twitter.

---