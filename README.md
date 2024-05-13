# JobQuest
![License](https://img.shields.io/badge/license-MIT-red.svg)

## Description

Calling all jobseekers and hiring managers! Look no further, as JobQuest is your all-in-one platform where managers can post jobs and applicants can apply to them. This app was built using Python, Django, HTML, and Tailwind.

## Demo

![Job Board](https://github.com/jtich40/django-job-board/assets/116316302/12707ee6-b8b8-47f5-83a8-1bad4f295c92)

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contributing](#contributing)
* [Questions](#questions)

## Installation

The application can be ran locally by following these steps:

1. Clone the repository to your machine using the following command:

```
git@github.com:jtich40/django-job-board.git
```

2. Move into the directory with the project files:

```
cd jobboard
```

3. Create a virtual environment:

```
# install virtualenv first
python -m pip install virtualenv

# create the virtual environment
virtualenv envname
```

4. Activate the virtual environment:

```
# run this command if on MacOS or Unix
source envname/bin/activate


# run this command if on Windows
envname\Scripts\activate
```

5. Install the requirements:

```
pip install -r requirements.txt
```

6. Run the migrations:

```
python manage.py migrate
```

7. Start the development server:

```
# start the server
python manage.py runserver

```


## Usage

The development server can be accessed at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Home page:

![Screenshot 2024-05-13 at 1 30 55 PM](https://github.com/jtich40/django-job-board/assets/116316302/02d453d6-4542-402d-85a5-a385912cd376)

Job Listing (Applicant) page:

![Screenshot 2024-05-13 at 1 36 01 PM](https://github.com/jtich40/django-job-board/assets/116316302/9d045819-02d2-4f5e-881b-cba7615d107d)

Application page:

![Screenshot 2024-05-13 at 1 37 14 PM](https://github.com/jtich40/django-job-board/assets/116316302/2c1d3369-7e4d-493f-bd30-4dde9e711a6f)

Success page:

![Screenshot 2024-05-13 at 1 39 37 PM](https://github.com/jtich40/django-job-board/assets/116316302/a3a8f757-8480-43ae-8680-9f4d9a2669b6)

Login page:

![Screenshot 2024-05-13 at 1 40 31 PM](https://github.com/jtich40/django-job-board/assets/116316302/47c5d50e-2330-4f41-b373-8c1b31782758)

Register page:

![Screenshot 2024-05-13 at 1 41 14 PM](https://github.com/jtich40/django-job-board/assets/116316302/462c303b-ce7a-40ee-9af3-6f9c62eb3b4c)

Create Listing page:

![Screenshot 2024-05-13 at 1 42 33 PM](https://github.com/jtich40/django-job-board/assets/116316302/69a91f57-59fa-41ab-9014-4f280869559b)

Job Listing (Creator) page:

![Screenshot 2024-05-13 at 1 44 31 PM](https://github.com/jtich40/django-job-board/assets/116316302/c449b129-61a9-4bdb-a192-c30040f99850)

Update Listing page:

![Screenshot 2024-05-13 at 1 46 36 PM](https://github.com/jtich40/django-job-board/assets/116316302/b54ac2ee-bc5f-4cf5-a4d5-327efa20a1e4)

Delete page:

![Screenshot 2024-05-13 at 1 47 31 PM](https://github.com/jtich40/django-job-board/assets/116316302/7ff66497-33b1-4e2d-8ec4-a04c475c503c)

Applicants page:

![Screenshot 2024-05-13 at 1 48 22 PM](https://github.com/jtich40/django-job-board/assets/116316302/904a3b3c-ecde-44c2-a2ea-d6cb597fb915)

## License
  This application is licensed by the MIT license.
 
## Contributing
 
All contributions and suggestions are welcome! For direct contributions, please fork the repository and file a pull request.

## Questions

For any questions, please contact me at jared.tichacek@gmail.com. Feel free to check out more of my projects at [jtich40](https://github.com/jtich40)!

