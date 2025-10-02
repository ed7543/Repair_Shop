# Repairs Management System

Auto Repairs Management System is a Django-based web application that allows users to manage car repairs, shops, manufacturers, and cars. Users can view repairs, add new repairs, and track information about cars and repair shops. Superusers have administrative control over all entities. The project includes a responsive frontend built with Bootstrap.

## Features
For All Users
View all repairs on the homepage.
Each repair displays:
Shop
Date
Car information
Image of the repair


For Authenticated Users
Add new repairs.
Repairs are linked to the user who created them.


For Superusers (Admin Panel)
Full CRUD (Create, Read, Update, Delete) access to Manufacturers, Cars, Repairs, and Shops.
Restrict certain actions for Shops (cannot be changed or deleted via admin panel).
Automatic assignment of user field on Repairs when created via admin panel.

## Models


Manufacturer
Information (name or description)
Can only be added by superusers.


Shop
Name, Year, Type (Boolean), Related Manufacturers
Cannot be changed or deleted in the admin panel.


Car
Type, Manufacturer, Max speed, Color


Repair
Code, Date, Description, Image, Associated Car and Shop, User (creator)


## Usage
Homepage: View all repairs with images, shops, cars, and dates.
Repairs Page: Add a new repair via a form.
Admin Panel: Superusers can manage Manufacturers, Cars, Repairs, and Shops. Shops are read-only for superusers.


## Frontend
Bootstrap 5 is used for responsive design.
Navbar links to Home, Repairs, and About Us pages.
Repairs displayed in card format with images and details.
Forms styled with Bootstrap classes.


Images uploaded for repairs are stored in the media/repairs/ folder.



## Technologies Used
Python 3.x
Django 4.x
Bootstrap 5
SQLite (default database)


## Notes
Repairs are linked to the user who created them.
Shops cannot be modified or deleted in the admin panel.
Images should be uploaded in supported formats (JPG, PNG).
