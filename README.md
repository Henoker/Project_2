# Project Title: Henoker Auction House
Design an eBay-like e-commerce auction site that will allow users to post auction listings, 
place bids on listings, comment on those listings, and add listings to a “watchlist.”

## Screenshots

Here are some screenshots of the boilerplate project.

![Screenshot01][1]  
[1]: ./auctions/static/images/project2.png

## About the Project

This assignment requires writing a ebay like auction ecommerce web app using django. 
I have learned and implemented the following by developing the app.

* How to Crate Models for an app based on the specification of the project.
- In addition to the User model: I created three models; one for auction listings, 
  one for bids, and one for comments made on auction listings.
* How to Create Listing: Users can be able to visit a page to create a new auction listing. 
  They  can be able to specify a title for the listing, a text-based description, and 
  what the starting bid amount. Users can also optionally be able to provide a URL for an image for 
  the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).

* How to create Active Listings Page: The default route of your web application would let users view all of 
  the currently active auction listings. For each active listing, this page will display (at minimum) the title,
  description, current price, and photo (if one exists for the listing).

* How to create Listing Page: Clicking on a listing will take users to a page specific to that listing. 
  On that page, users can be able to view all details about the listing, including the current price for the listing.
  - If the user is signed in, the user can be able to add the item to their “Watchlist.” 
    If the item is already on the watchlist, the user can be able to remove it.
  - If the user is signed in, the user can be able to bid on the item. 
    Only a bid that is as large as the starting bid and greater than any other bids is accepted. 
    If the bid doesn’t meet those criteria, the user is notified with an error.
  - If the user is signed in and is the one who created the auction listing, the user has the ability to 
    “close” the auction from this page, which makes the highest bidder the winner of the auction and 
    makes the listing no longer active.
  - If a user is signed in on a closed listing page, and the user has won that auction, the page will notify him.
  - Users who are signed in can add comments to the listing page. 
    The listing page displays all comments that have been made on the listing.

* How to create a Watchlist: Users who are signed in can visit a Watchlist page, 
  which will display all of the listings that a user has added to their watchlist. 
  Clicking on any of those listings will take the user to that listing’s page.

* How to create Categories for Auction: Users can visit a page that displays a list of all listing categories. 
  Clicking on the name of any category will take the user to a page that displays all of the active listings
  in that category.
* How to do CRUD opertaion from Django Admin Interface: Via the Django admin interface, a site administrator 
  can view, add, edit, and delete any listings, comments, and bids made on the site. 
  

## Built using:
- HTML
- CSS
- Python 
- Django
- Bootstrap 4.4.1

## Getting started:
- Clone this repository or fork it.
    - To clone this repository type:
        git clone `https://github.com/Henoker/Project_2.git` on your command line
    - To fork this repository, click fork button of this repository then type:
        git clone `https://github.com/<your username>/Project_2.git`
- open it with your favorite editor
- RUN pip install -r requirements.txt
- CD to commerce folder and run python manage.py makemigrations
- You project will be accessible in your web browse.


## License
Distributed under the [MIT](https://github.com/Henoker/Project_2/blob/master/LICENSE) License. See [`LICENSE`](https://github.com/Henoker/Project-0/blob/master/LICENSE) for more information.

## Contact
- Henock Beyene Testfatsion - [hennybany@gmail.com](mailto:hennybany@gmail.com)
- Project link: https://github.com/Henoker/Project_2

## Love my effort?

<a href='https://www.linkedin.com/in/henock-beyene-tesfatsion-921ba54b/' target='_blank'><img height='35' style='border:0px;height:34px;' src='auctions/static/images/download.jpg' border='0' alt='Hire me at LinkediN' />