# My-Unsplash
A Django based personal gallery application displaying a catalogue of photos according to their categories and location in which the photographs were taken

------------------------------------------------------------------------
## BY: [Eugene Nzioki](https://github.com/EugeneZnm)

## User Requirements

1. View different images that interest me.
2. Click on a single photo to expand it and also view the details of the image.
3. Search for different categories of images.
4. Copy a link to the image to share with my friends.
5. View images based on the location.

## Features

+ [x] Create and display photos based on categories
+ [x] Django admin dashboard for adding & managing images, categories and location
+ [x] Bootstrap image modal and copy link button.
+ [x] Filter images based on location.
+ [x] search functionality based on image category.

## Models
### Image Model
* Fields: Image, Image Name, Image Description, Image Location Foreign Key and Image category Foreign Key.

* `save_image()` - Save an image to the database.
* `delete_image()` - Delete image from the database.
* `update_image()` - Update image in the database.
* `get_image_by_id(id)` - Allows us to get an image using its ID.
* `search_image(category)` - Allows us to search for an image using its category.
* `filter_by_location(location)` - Allows us to filter images by the location.

### Location and Category models
* Location and category that link to the Image model.
* `save` and `delete` methods in both models

## Admin Dashboard
Use django admin to post photos to the database and manage the photos

## Setup

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3

### Cloning the repository
```bash
git clone https://github.com/EugeneZnm/My-Unsplash.git && cd Myunsplash
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip install -r requirements.txt
```

### Prepare environmet variables
Create a .env file and add the following configutions to it
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running Tests
```bash
python manage.py test
```

### Running the server 
```bash
python manage.py runserver
```
## Contributing

- Git clone [https://github.com/EugeneZnm/My-Unsplash.git](https://github.com/EugeneZnm/My-Unsplash.git) 
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

### Deploying to heroku
Refer to this guide: [deploying to heroku](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)
Set the configuration to production mode

## Live Demo

The web app can be accessed from the following link: 
[BELLA VISTA](https://bellavista.herokuapp.com/)


## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://docs.djangoproject.com/en/1.11/)
* [Heroku](https://heroku.com)


## License
MIT License

Copyright(c) 2018

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
