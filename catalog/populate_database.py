"""Populate the item catalog database some initial content.

This script should only be run on an empty database.
"""
from sqlalchemy import func

from catalog.database_setup import User, Category, Item
from catalog.connect_to_database import connect_to_database

def populate_database():
    """Populate the item catalog database some initial content."""
    session = connect_to_database()

    # Make sure the database is empty before running this inital data dump.
    category_count = session.query(func.count(Category.id)).scalar()
    if category_count > 0:
        session.close()
        return

    # Create the six categories animals fall in to.
    category1 = Category(name="HTML&CSS", about=
             "HyperText Markup Language (HTML) is a markup language for creating webpages. Webpages are usually viewed in a web browser. They can include writing, links, pictures, and even sound and video. HTML is used to mark and describe each of these kinds of content so the web browser can show them correctly.", linkCat="https://www.w3.org/html/", linkCat2="https://www.w3.org/Style/CSS/",imageCat="fab fa-html5", imageCat2="fab fa-css3-alt")
    session.add(category1)
    session.commit()

    category2 = Category(name="JavaScript", about=
             "JavaScript (JS) is a lightweight interpreted or JIT-compiled programming language with first-class functions. While it is most well-known as the scripting language for Web pages, many non-browser environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat. JavaScript is a prototype-based, multi-paradigm, dynamic language, supporting object-oriented, imperative, and declarative (e.g. functional programming) styles", linkCat="https://developer.mozilla.org/en-US/docs/Web/JavaScript", imageCat="fab fa-js-square")
    session.add(category2)
    session.commit()

    category3 = Category(name="React.js", about=
             "React is a JavaScript library for building user interfaces. It is maintained by Facebook and a community of individual developers and corporations.", linkCat="https://reactjs.org/", imageCat="fab fa-react")
    session.add(category3)
    session.commit()

    category4 = Category(name="Node.js", about=
             "Node.js is an open-source, cross-platform JavaScript run-time environment that executes JavaScript code server-side.", linkCat="https://nodejs.org/", imageCat="fab fa-node")
    session.add(category4)
    session.commit()

    category5 = Category(name="Python", about=
             "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace.", linkCat="https://www.python.org/", imageCat="fab fa-python")
    session.add(category5)
    session.commit()

    category6 = Category(name="APIs", about=
             "API is a set of subroutine definitions, protocols, and tools for building application software.")
    session.add(category6)
    session.commit()

    category7 = Category(name="Databases", about=
             "A database is an organized collection of data. A relational database, more restrictively, is a collection of schemas, tables, queries, reports, views, and other elements.", imageCat="fas fa-database")
    session.add(category7)
    session.commit()

    category8 = Category(name="OAuth", about=
             "OAuth (Open Authorization) is an open standard for token-based authentication and authorization on the Internet. OAuth, which is pronounced oh-auth, allows an end user's account information to be used by third-party services, such as Facebook, without exposing the user's password.", linkCat="https://oauth.net")
    session.add(category8)
    session.commit()

    category9 = Category(name="Git", about=
             "Git is a version control system for tracking changes in computer files and coordinating work on those files among multiple people.", linkCat="https://git-scm.com/", imageCat="fab fa-git")
    session.add(category9)
    session.commit()



	


    # Create a  user for these initial items
    user1 = User(name="Irina Serova", email="isserova@gmail.com")
    session.add(user1)
    session.commit()

    # Create some items
    item1 = Item(
        user=user1,
        category=category1,
        name="Learn HTML",
        description=(
            "Learn the basics of HTML with this interactive Codecademy course. The introduction here gives an overview of the structure, purpose, and syntax of the language."
),
        duration="2 to 4 hours",
        level="BEGINNER",
        image_url="https://production.cdmycdn.com/webpack/3d7c19cebe85b8d870e6d2c181dec922.svg",
	    link="https://www.codecademy.com/learn/learn-html"

    )
    session.add(item1)
    session.commit()

    item2 = Item(
        user=user1,
        category=category1,
        name="Learn CSS",
        description=(
            "Elephants are large mammals of the family Elephantidae and the "
            "order Proboscidea. Two species are traditionally recognised, the "
            "African elephant and the Asian elephant, although some evidence "
            "suggests that African bush elephants and African forest elephants "
            "are separate species."
        ),
        duration="8 to 16 hours",
        level="INTERMEDIATE",
        image_url="https://production.cdmycdn.com/webpack/9522085449ef048604ca3f5fa8d1bc27.svg",
        link="https://www.codecademy.com/learn/learn-css"

    )
    session.add(item2)
    session.commit()

   
    item3 = Item(
        user=user1,
        category=category2,
        name="Learn JavaScript",
        description=(
            "Learn the fundamentals of JavaScript, the programming language of the web."
        ),
        duration="4 to 8 hours",
        level="INTERMEDIATE",
        image_url="https://production.cdmycdn.com/webpack/fbac2e163a79bceb56b5dbabe6c74945.png",
        link="https://www.codecademy.com/learn/learn-javascript"
    )
    session.add(item3)
    session.commit()

    item5 = Item(
        user=user1,
        category=category3,
        name="Learn ReactJS: Part I",
        description=(
            "Continue your learning by starting with Learn ReactJS: Part I Build powerful interactive applications with this popular JavaScript library."
        ),
        duration="8 to 16 hours",
        level="INTERMEDIATE",
        image_url="https://production.cdmycdn.com/webpack/d38587f67ab102541186df1c157597d1.svg",
        link="https://www.codecademy.com/learn/react-101"
    )
    item4 = Item(
        user=user1,
        category=category4,
        name="NODESCHOOL",
        description=(
            "Open source workshops that teach web software skills. Do them on your own or at a workshop nearby."
        ),
        duration="8 to 16 hours",
        level="INTERMEDIATE",
        image_url="https://nodeschool.io/images/schoolhouse.svg",
        link="https://nodeschool.io"
    )
    session.add(item4)
    session.commit()


    session.add(item5)
    session.commit()

    item6 = Item(
        user=user1,
        category=category5,
        name="Python",
        description=(
            "Learn Python fundamentals that set you up to work in web development and machine learning."
        ),
        duration="8 to 16 hours",
        level="INTERMEDIATE",
        image_url="https://production.cdmycdn.com/webpack/4bef5020e69a6464ebd9dabe087cb809.svg",
        link="https://www.codecademy.com/learn/learn-python"
    )
    session.add(item6)
    session.commit()

   
    item7 = Item(
        user=user1,
        category=category6,
        name="Learn API!",
        description=(
            "Learn how to use the YouTube API!"
        ),
        duration="8 to 16 hours",
        level="BEGINNER",
        image_url="https://s3.amazonaws.com/codecademy-production/original/50ecea3ba778dddcd50001d2_871712554.png",
        link="https://www.codecademy.com/en/tracks/youtube"
    )
    session.add(item7)
    session.commit()

    item8 = Item(
        user=user1,
        category=category7,
        name="Getting Started with PostgreSQL on Mac OSX",
        description=(
            "This tutorial will teach you how to set up, configure, and use PostgreSQL on MacOSX 10.7 (Lion) and above. You will need at least a basic level of comfort using the command line using either the MacOSX built-in terminal, iTerm2, Zsh, or something similar."
        ),
        duration="to 1 hour",
        level="BEGINNER",
        image_url="https://process.filestackapi.com/cache=expiry:max/resize=width:1050/compress/Vx31ILRQRSO5fBiMSvEg",
        link="https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb"
    )
    session.add(item8)
    session.commit()

    # Create some amphibians
    item9 = Item(
        user=user1,
        category=category8,
        name="OAuth2 with GitHub",
        description=(
            "Learn OAuth2 with the GitHub API"
        ),
        duration="2 to 4 hours",
        level="BEGINNER",
        image_url="https://process.filestackapi.com/cache=expiry:max/resize=width:1050/compress/Vx31ILRQRSO5fBiMSvEg",
        link="https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb"
    
    )
    session.add(item9)
    session.commit()

    item10 = Item(
        user=user1,
        category=category9,
        name="Learn Version Control with Git",
        description=(
            "A step-by-step course for the complete beginner"
           
        ),
        duration="to 1 hour",
        level="BEGINNER",
        image_url="https://tower-website-ftkdppxp1xaznovg.netdna-ssl.com/learn/assets/img/keyvisual/ebook_dark.1527173730.png",
        link="https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/best-practices"
    )
    session.add(item10)
    session.commit()

    item11 = Item(
        user=user1,
        category=category2,
        name="Javascript",
        description=(
            "Make your websites dynamic and interactive with JavaScript! You'll create features and stand-alone applications. This course will wrap everything you've learned at The Odin Project into one, final capstone project. 30 lessons"
           
        ),
        duration="16 to 32 hours",
        level="BEGINNER",
        image_url="https://www.theodinproject.com/assets/home-isometric-60f02f572fa9ae583a22bf4d391e48f30cae707cbdb602e130bc3f12d73bac85.svg",
        link="https://www.theodinproject.com/courses/javascript"
    )
    session.add(item11)
    session.commit()

    item12 = Item(
        user=user1,
        category=category3,
        name="Start Learning React",
        description=(
            "This series will explore the basic fundamentals of React to get you started."
           
        ),
        duration="2 to 4 hours",
        level="BEGINNER",
        image_url="https://d2eip9sf3oo6c2.cloudfront.net/series/square_covers/000/000/003/full/course_image.png",
        link="https://egghead.io/courses/start-learning-react"
    )
    session.add(item12)
    session.commit()

    item13 = Item(
        user=user1,
        category=category4,
        name="Node JS Training and Fundamentals",
        description=(
            "Node basics and fundamentals to make you ready to create any web app using express, jade and node modules."
           
        ),
        duration="4 to 8 hours",
        level="BEGINNER",
        image_url="https://udemy-images.udemy.com/course/480x270/595294_bc81.jpg",
        link="https://www.udemy.com/node-js-training-and-fundamentals/?siteID=Fh5UMknfYAU-TkergXOKdpODeZTt.miTZw&LSNPUBID=Fh5UMknfYAU"
    )
    session.add(item13)
    session.commit()

    item14 = Item(
        user=user1,
        category=category5,
        name="Python for Beginners with Examples",
        description=(
            "A practical Python course for beginners with examples and exercises."
           
        ),
        duration="4 to 8 hours",
        level="BEGINNER",
        image_url="https://udemy-images.udemy.com/course/480x270/577248_3b6f_12.jpg",
        link="https://www.udemy.com/ardit-sulce-python-for-beginners/?siteID=Fh5UMknfYAU-XQ5mHVXoiEA5LjPQW.xmAg&LSNPUBID=Fh5UMknfYAU"
    )
    session.add(item14)
    session.commit()

    item15 = Item(
        user=user1,
        category=category6,
        name="Laravel E-Commerce Restful API",
        description=(
            "Know what is Rest concept and how to create a RESTFUL API with Laravel Resource"
           
        ),
        duration="32 to 64 hours",
        level="INTERMEDIATE",
        image_url="https://udemy-images.udemy.com/course/480x270/1470550_2d1e.jpg",
        link="https://www.udemy.com/ardit-sulce-python-for-beginners/?siteID=Fh5UMknfYAU-XQ5mHVXoiEA5LjPQW.xmAg&LSNPUBID=Fh5UMknfYAU"
    )
    session.add(item15)
    session.commit()

    item16 = Item(
        user=user1,
        category=category7,
        name="Creating Programmatic SQL Database Objects",
        description=(
            "Learn how to add functionality to your database with programmatic database objects using the R programming language."
           
        ),
        duration="8 to 16 hours",
        level="INTERMEDIATE",
        image_url="https://prod-discovery.edx-cdn.org/media/course/image/d471fec7-5d9d-45f1-b622-af86a31064be-6fe9a510bf23.small.jpg",
        link="https://www.edx.org/course/creating-programmatic-sql-database-objects?source=aw&awc=6798_1528876589_9c64f89577cb3b4983eebd3c02c6f2e2"
    )
    session.add(item16)
    session.commit()

    item17 = Item(
        user=user1,
        category=category8,
        name="OAuth 2.0 Tutorial",
        description=(
            "This tutorial series explains how OAuth 2.0, the open authorization protocol, works."
           
        ),
        duration="4 to 8 hours",
        level="BEGINNER",
        image_url="http://tutorials.jenkov.com/images/oauth2/introduction.png",
        link="http://tutorials.jenkov.com/oauth2/index.html"
    )
    session.add(item17)
    session.commit()

    item18 = Item(
        user=user1,
        category=category9,
        name="How to Use Git and GitHub",
        description=(
            "This course, built with input from GitHub, will introduce the basics of using version control by focusing on a particular version control system called Git and a collaboration platform called GitHub."
           
        ),
        duration="8 to 16 hours",
        level="BEGINNER",
        image_url="https://res.cloudinary.com/db194k5td/image/upload/v1510723267/git_logo_tjnjxd.svg",
        link="https://in.udacity.com/course/how-to-use-git-and-github--ud775"
    )
    session.add(item18)
    session.commit()

        

    session.close()

    print "Populated database..."


if __name__ == '__main__':
    populate_database()
