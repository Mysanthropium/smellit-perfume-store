# Smellit Perfume Store
![amiresponsive](static/README/images/amiresponsive.jpg)
## A men's perfume e-commerce store online.
An E-commerce store for men who seek to buy perfumes, colognes and deodorants online. You can also find information about new fragrances, brands, differences between them all and more in the blog section. 

### - By Rasmus Persson

### [Live Site](https://smellit-perfume-store-8571815b705d.herokuapp.com/)

### [Repository](https://github.com/Mysanthropium/smellit-perfume-store)

## Table of contents
- [Business Modell](#business-model)
- [UX](#ux)
- [Features](#features)
- [User Stories](#user-stories)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)

### Business Model
The business is a B2C e-commerce platform focusing on a diverse selection of men's perfumes, fragrances and colognes from various suppliers.

#### Marketing Strategy
The marketing strategy for this online shop is:
* Use platforms like Facebook and Instagram for advertising and engaging with customers.
* Send newsletters and promotional emails to reach existing customers.
* Collaborate with influencers and bloggers for product reviews.
* Offer free shipments depending on the value of the customers shopping bag.
* Offer gift wrapping and personalization services for additional fees.
* Implement SEO strategies to compete with bigger companies.
* Use the blog section to write meaningful and useful posts with links to other companies.
* Track the sales rate of different brands to choose a fitting and meaningful cover image.
* Offer streamers with 5000+ viewers good products for them to advertise to start the flow of traffic to the site.

Key Activities:
* Acquire a diverse selection of men's perfumes, fragrances and colognes from various suppliers.
* As the owner, maintain a user-friendly website with up-to-date products, pricing and blog posts.
* Create marketing campaigns and keep up with the social media engagement.
* Continuously use SEO optimization.
* Offer customer support that's responsive via chat, phone and email.
* Implement management systems to make sure the inventory doesn't get out of stock.

Resouces:
* Keep the website fully functional.
* Make use of a marketing/advertising budget.
* Use good tools to keep track of inventory.
* Make use of a skilled workforce group in marketing, advertisement and e-commerce platforms.

Target Audience:
* The target audience is mostly males between 18-55 years old, due to their most likely more disposable income for luxury fragrances.
* Customers that focuses on personal grooming and self-care.
* Customers that follow trends and luxury brands.

#### Goals For This Website:
The goal is to give the user a nice experience throughout the whole website, on any device. To be able to purchase perfumes from different brands that's been handpicked by the owner, and read news about brands and the evolution of perfumes throughout the world on the blog.
* Users have the possibility to register for an account to save their information for easier purchases in the future.
* Read posts on the blog and find other useful sources about the difference between perfume and cologne for example.
* Sign up for newsletters to be able to catch all the latest news whenever they get out.
* Contact the owner to give feedback, blog requests or general questions.
* Keep the products and pricing up-to-date.
* To grow as a brand and a reputation of good customer support.

#### Facebook Business Page:
(My site got taken down before I realized it was in Swedish.)
![facebookpage](static/README/images/fbpage.jpg)
![fbpresentation](static/README/images/fbpagepresentation.jpg)

# UX

### Design
Since I like perfumes and didn't really know anything about it except that they smell good, I thought this would be a great idea for me to be able to research a bit more about the differences and how they are made. That's how I also came up with the idea of adding a blog to share som research with the users.

### Database
Before starting this project I created a database schema that helped me out alot, but was slightly changed throughout development.
![dbschema](static/README/images/databasestructure.jpg)

### Wireframes
I made my wireframes using [Figma Wireframes](https://www.figma.com/templates/wireframe-kits/)

### Desktop view

>Home page

![wfhomepage](static/README/images/wfhomepage.jpg)

>Product page

![wfprodpage](static/README/images/wfproductpage.jpg)

>Blog page

![wfblogpage](static/README/images/wfblog.jpg)

### Mobile view

>Home page

![wfhomepagemob](static/README/images/wfhomepagemob.jpg)

>Product page

![wfprodpagemob](static/README/images/wfprodpagemob.jpg)

>Blog page

![wfblogpagemob](static/README/images/wfblogpagemob.jpg)

## Features
- Navigation\
At the top left corner of the page there's a logo which will take the user to the homepage. In the top middle there's a navbar which will collapse into a burger icon on smaller devices, containing a dropdown menu of All Products(sorting), a Men's Cologne dropdown menu(categories), a Special Offers dropdown menu, a link to the Blog page and a link to Contact us page. Then at the top right corner there's a dropdown menu of My Account, depending if the user is logged in or not the menu list will change accordingly.

    - Not logged in users:
        - All Products
            - By Price
            - By Rating
            - By Category
            - All Products
        - Men's Cologne
            - Cologne
            - Deodorant
            - All Products
        - Special Offers
            - New Arrivals
            - Deals
            - All Specials
        - Blog
        - Contact Us
        - My Account
            - Register
            - Login
        - Shopping Bag
    - Logged in users:
        - All Products
            - By Price
            - By Rating
            - By Category
            - All Products
        - Men's Cologne
            - Cologne
            - Deodorant
            - All Products
        - Special Offers
            - New Arrivals
            - Deals
            - All Specials
        - Blog
        - Contact Us
        - My Account
            - My Profile
            - Logout
        - Shopping Bag
    - Superusers will see all of the above plus:
        - My Account
            - Product Management
            - Add Blog Post

<br>
<details>
<summary>Home Page</summary>
<br>
- The home page consists of a background image with a shop now button to get to the products page.

![shopnowbutton](static/README/images/shopnowbutton.jpg)
</details>
<br>
<details>
<summary>Products Page</summary>
<br>
- The products page consists of images, price, rating and category of the products listed on that page. In the top right corner there is also a sort by dropdown menu and in the bottom right there's a small arrow icon that takes you to the top of the page.

![shopnowbutton](static/README/images/productspage.jpg)
</details>
<br>
<details>
<summary>Product Detail Page</summary>
<br>
- On the product detail page users can read a description of the product, aswell as price, rating and category. There's the possibility to choose quantity of the product. There's a button to add this product to the bag and a button to go back to products page and keep shopping. 

![shopnowbutton](static/README/images/productdetail.jpg)
</details>
<br>
<details>
<summary>Footer</summary>
<br>
- The footer exist on all pages and consists of social links, privacy policy and a form to subscribe to newsletters.

![shopnowbutton](static/README/images/newsletters.jpg)
![socials](static/README/images/footericons.jpg)
</details>
<br>
<details>
<summary>Blog</summary>
<br>
- On the blog, users can browse the posts and click on them to get to the blog details.

![shopnowbutton](static/README/images/blogpage.jpg)
</details>
<br>
<details>
<summary>Contact Us</summary>
<br>
- Contact page features a form to fill out to send emails to the store owner.

![shopnowbutton](static/README/images/contactus.jpg)
</details>
<br>
<details>
<summary>Sign Up Page</summary>
<br>
- On this page users can sign up for an account to save billing information for future checkouts.

![shopnowbutton](static/README/images/signup.jpg)
</details>
<br>
<details>
<summary>Sign In Page</summary>
<br>
- On this page registered users can sign in to be able to use its benefits.

![shopnowbutton](static/README/images/signin.jpg)
</details>
<br>
<details>
<summary>Profile Page</summary>
<br>
- On the profile page signed in users can edit their billing information and see their order history.

![shopnowbutton](static/README/images/myprofile.jpg)
![orderhistory](static/README/images/orderhistory.jpg)
</details>
<br>
<details>
<summary>Shopping Bag</summary>
<br>
- The shopping bag consists of a summary of what the user added to the bag, quantity, price and subtotal. The ability to update or remove products. In the bottom right there's a secure checkout button to take the user to the checkout page, or a keep shopping button to get back to products.

![shopnowbutton](static/README/images/shoppingbag.jpg)
</details>
<br>
<details>
<summary>Checkout</summary>
<br>
- The checkout page consists of a form to complete the order, and a order summary with a grand total price. To complete the order use the Complete Order button, or choose to adjust bag.

![shopnowbutton](static/README/images/checkout.jpg)
</details>
<br>
<details>
<summary>Notifications</summary>
<br>
- The website show success, error and info messages in the top right corner.

![shopnowbutton](static/README/images/messages.jpg)
</details>
<br>
<details>
<summary>Superuser/Product Management Page</summary>
<br>
- As superuser it's possible to add products in the front end.

![shopnowbutton](static/README/images/productmanagement.jpg)
</details>
<br>
<details>
<summary>Superuser/Edit or Delete a product</summary>
<br>
- The home page consists of a background image with a shop now button to get to the products page.

![shopnowbutton](static/README/images/productcrud.jpg)
</details>
<br>
<details>
<summary>Superuser/Add Blog Post</summary>
<br>
- As superuser it's possible to add blog posts.

![shopnowbutton](static/README/images/addblogpost.jpg)
</details>
<br>
<details>
<summary>Superuser/Edit or Delete blog</summary>
<br>
- As superuser it's possible to edit or delete blog posts both from blog page and blog post detail page.

![shopnowbutton](static/README/images/blogcrud.jpg)
</details>

## Features Left To Implement
* User profiles could be expanded, maybe a profile page containing order history and returns.
* Maybe widen the blog, let users create posts aswell.
* Implement more products and categories, for example men's skin care.
* To be able to add more images to product details.
* A FAQ page.

# User Stories

* Link to my user stories is [here](https://github.com/users/Mysanthropium/projects/5)

# Testing
* Link to the testing page is [here](https://github.com/Mysanthropium/smellit-perfume-store/blob/main/TESTING.md)

# Technologies Used
### Languages
- HTML5
- CSS
- Python
- JavaScript

### Frameworks
- Django
- Bootstrap

### Libraries
- Font Awesome
- Google Fonts

### Other Tools Used
- GitHub, used to store code and user stories
- Gitpod, my IDE of choice for the application
- Git, used for version control
- Heroku, for deployment and hosting of the application
- elephantSQL, used for storing data for this project
- AWS S3 Bucket, my choice for hosting static files and media files
- Stripe, used for secure payment and to validate credit cards
- [Freeformatter](https://www.freeformatter.com/), used to make my code look nicer and cleaner
- [Temp-mail](https://temp-mail.org/sv/), used to test mail functions on the page
- [Figma](https://www.figma.com/templates/wireframe-kits/), my wireframe tool of choice
- [MailerLite](https://www.mailerlite.com/?source=google&medium=cpc&campaign=1.%20Brand%20-%20Exact%20[EU]%20tCPA&content=MailerLite%20Brand%20EXT&term=mailerlite&ml_campaignid=1934853293&ml_adsetid=71004315072&gad=1&gclid=Cj0KCQjwrMKmBhCJARIsAHuEAPSXHcISYTvAObpx0DaVtFNR_4Z5q0qbxY1yRWoeOvPfUGUegvEQiY4aAgZ6EALw_wcB), my newsletter tool for subscriptions

### Tools used for testing
- W3C HTML Validator
- W3C CSS Validator
- PEP8
- JSHint
- DevTools Lighthouse
- DevTools

To find more about testing, click [here](https://github.com/Mysanthropium/smellit-perfume-store/blob/main/TESTING.md).

[Back to top](#a-mens-perfume-e-commerce-store-online)

## Deployment
### Version Control
Using Gitpod
1. Create a Git Repository by navigating to your repositories on GitHub and click "New" in the top right corner.
2. If you haven't already, you can choose to install the Gitpod browser extension or use the Gitpod IDE.
3. Open a new workspace by navigating to your newly created repository and click the "Open in Gitpod" button which will open up a development environment for this repository.
4. In your workspace, set up your environment variables and make sure your application is working by running it locally.
5. Commit your changes to GitHub by using Git commands:
    * git add .
    * git commit -m "initial commit message"
    * and push changes to GitHub with git push

### App Deployment
Deploy app to Heroku.
1. Navigate to heroku.com and log in to your account, or create one if needed.
2. On your dashboard, click the "New" button in the top right corner and choose "Create new app".
3. Choose a name for your application, preferebly something close to the repository name on GitHub.
4. Choose the region closest to you.
5. Navigate to the deploy section and choose the GitHub option as deployment method. Add the correct repository to link the account.
6. You can choose automatic deploys by enabling it with the main/master branch.
7. Using elephantSql as the Database:
    * Login to ElephantSQL.com
    * On your dashboard select "Create New Instance" in the top right corner.
    * Choose a fitting name and select a region.
    * Choose the data center closest to you.
    * When created, navigate to your new database and copy the URL for the database.
8. Go back to your heroku app and navigate to the Settings tab.
9. Click on "Reveal Config Vars" and add a new one named DATABASE_URL and paste in the database URL from elephantSql.
10. Go to your workspace and install. "pip3 install dj_database_url" and "pip3 install psycopg2".
11. Update the requirements.txt file using "pip3 freeze requirements.txt"
12. Add the database url to your env.py file.
13. Head to settings.py and change the default DATABASES setting to: 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')).
14. Run migrations for your new database:
    * Create a new file called "Procfile" in the root directory, in that file add: web: gunicorn PROJECT_NAME.wsgi.
    * Navigate to settings.py again and add the heroku link and the localhost link to ALLOWED_HOSTS.
    * Update the SECRET_KEY to os.environ.get('SECRET_KEY', '')
    * Go to your env.py file and add a new secure SECRET_KEY then copy the key.
    * Add this SECRET_KEY to your config vars on heroku and copy in the key as the value.
    * Go back to your workspace and push these changes to GitHub.


# Credits
### [YouTube](https://www.youtube.com/)
* For having great learning content.

### [Django](https://www.djangoproject.com/)
* For built in admin panel and additional useful features.

### [Python](python.org)
* For beginner friendly tutorials.

### [GitHub](docs.github.com)
* For learning how to document a nice looking readme.

### [Bootstrap](https://getbootstrap.com/)
* For helping me style the project.

### [MailerLite](https://www.mailerlite.com/?source=google&medium=cpc&campaign=1.%20Brand%20-%20Exact%20[EU]%20tCPA&content=MailerLite%20Brand%20EXT&term=mailerlite&ml_campaignid=1934853293&ml_adsetid=71004315072&gad=1&gclid=Cj0KCQjwrMKmBhCJARIsAHuEAPSXHcISYTvAObpx0DaVtFNR_4Z5q0qbxY1yRWoeOvPfUGUegvEQiY4aAgZ6EALw_wcB)
* For newsletter subscription

### Code Institute
* This project is a part of the course content.

### [John Elder](https://www.youtube.com/@Codemycom)
* For well made tutorials on how to make a blog that's easy to understand.

### Code base
* I followed along with the walkthrough project Boutique Ado to have as a base for this project.

### [CSS-tricks](https://css-tricks.com/)
* To help with css issues, like sticking the footer to bottom of the page.

# Acknowledgements
* Students at code institute on slack for solving issues together.
* Tutors at code intitute for being of great help whenever needed.

[Back to top](#a-mens-perfume-e-commerce-store-online)