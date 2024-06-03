<p align="center">
  <img src="static/images/mug-white.png" alt="Software Stacks Logo">
</p>
<h1 align="center">Cups Of Joy</h1>

<h2>Welcome</h2>

Link to live website: [CLICK HERE!](https://cupsofjoy-c2c917eb3f59.herokuapp.com/)

![Am I Responsive Image](documentation/amireponsive/cupsofjoy.png)

# Introduction

## Cups of Joy

Welcome to [**Cups of Joy**](documentation/amireponsive/cupsofjoy.png), a vibrant online platform dedicated to celebrating the art of coffee and fostering a sense of community. Our mission is to create a warm and inviting space where coffee enthusiasts can explore the rich world of artisanal brews, share their passion, and connect with like-minded individuals.

At Cups of Joy, we believe that every cup tells a story – one of craftsmanship, culture, and the pursuit of pure indulgence. Through our engaging content, we aim to inspire and educate, unveiling the secrets behind exceptional coffee experiences. Join us on this flavorful journey as we savor the finest beans, unravel brewing techniques, and uncover the tales behind each sip.

### Get Involved

Join **Cups of Joy** today and immerse yourself in a world where coffee is more than just a beverage – it's a passion, a culture, and a way of life. Our vibrant community welcomes coffee enthusiasts of all levels, from seasoned aficionados to curious explorers. Whether you're here to expand your knowledge, share your love for the perfect brew, or simply indulge in the rich aromas and flavors, our platform is your gateway to a vast and captivating landscape of coffee experiences. Let's embark on this flavorful journey together, savoring each sip, exchanging stories, and uncovering the secrets that make every cup a true masterpiece.

# Table of Contents
- [Introduction](#introduction)
  - [Cups Of Joy](#cups-of-joy)
    - [Our Website Features](#our-website-features)
    - [Get Involved](#get-involved)
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Fonts](#fonts)
    - [Google Fonts](#google-fonts)
      - [Roboto](#roboto)
      - [Lato](#lato)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
  - [Agile Methodologies - Project Management:](#agile-methodologies---project-management)
    - [Story Points Allocation](#story-points-allocation)
    - [Sprint Planning Example](#sprint-planning-example)
    - [MoSCoW Prioritization:](#moscow-prioritization)
    - [User Stories, Milestones and Epics](#user-stories-milestones-and-epics)
      - [Users Stories](#users-stories)
      - [Milestones](#milestones)
      - [Epics](#epics)
        - [Epic 1: User Engagement and Interaction](#epic-1-user-engagement-and-interaction)
        - [Epic 2: User Account Management](#epic-2-user-account-management)
        - [Epic 3: Core Platform Development](#epic-3-core-platform-development)
        - [Epic 4: Content Management and Administration](#epic-4-content-management-and-administration)
        - [Epic 5: Community Building and Feedback](#epic-5-community-building-and-feedback)
        - [Epic 6: Documentation and Quality Assurance](#epic-6-documentation-and-quality-assurance)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
      - [Home Page Wireframes](#home-page-wireframes)
      - [Categories Page Wireframes](#categories-page-wireframes)
      - [Post Detail Page Wireframes](#post-detail-page-wireframes)
      - [About \& Contact Page Wireframes](#about--contact-page-wireframes)
      - [Add Post Page Wireframes](#add-post-page-wireframes)
      - [Register Page Wireframes](#register-page-wireframes)
      - [Login Page Wireframes](#login-page-wireframes)
      - [Logout Page Wireframes](#logout-page-wireframes)
      - [My Bookmarks Page Wireframes](#my-bookmarks-page-wireframes)
      - [My Likes Page Wireframes](#my-likes-page-wireframes)
      - [My Comments Page Wireframes](#my-comments-page-wireframes)
      - [My Posts Page Wireframes](#my-posts-page-wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
      - [Database Schema](#database-schema)
      - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
      - [Tables Overview](#tables-overview)
      - [Relationships](#relationships)
      - [Design Considerations](#design-considerations)
    - [Security](#security)
      - [Data Encryption](#data-encryption)
      - [CSRF Tokens](#csrf-tokens)
      - [AllAuth](#allauth)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Features Functionality](#features-functionality)
    - [CRUD Functionality](#crud-functionality)
    - [All Existing Features with Screenshots](#all-existing-features-with-screenshots)
      - [Home Page](#home-page)
      - [User Registration, Login, and Logout](#user-registration-login-and-logout)
      - [User Profile](#user-profile)
      - [Add Post](#add-post)
      - [Search Functionality](#search-functionality)
      - [Post Details](#post-details)
      - [Comments and Interactions](#comments-and-interactions)
      - [Responsive Navigation Bar](#responsive-navigation-bar)
      - [Categories](#categories)
      - [My Bookmarks](#my-bookmarks)
      - [My Likes](#my-likes)
      - [My Comments](#my-comments)
      - [My Posts](#my-posts)
      - [Pagination](#pagination)
      - [Footer](#footer)
      - [Admin Panel](#admin-panel)
      - [Error Handling](#error-handling)
  - [Future Features](#future-features)
- [Technology Used](#technology-used)
  - [Frontend](#frontend)
  - [Backend](#backend)
  - [Deployment and Version Control](#deployment-and-version-control)
  - [Development Tools](#development-tools)
  - [Libraries and Frameworks](#libraries-and-frameworks)
  - [Validation Tools](#validation-tools)
  - [Others](#others)
- [Testing](#testing)
- [Deployment](#deployment)
  - [GitHub](#github)
  - [Gitpod](#gitpod)
  - [Heroku](#heroku)
  - [ElephantSQL](#elephantsql)
  - [Cloudinary](#cloudinary)
- [Cloning and Forking](#cloning-and-forking)
  - [Cloning the Repository](#cloning-the-repository)
  - [Forking the Repository](#forking-the-repository)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)

# Overview

Cups of Joy is a vibrant online platform celebrating the art of coffee and fostering a sense of community. It serves as a communal hub for:

- Joining a passionate community of coffee enthusiasts and professionals.
- Creating personalized profiles to share coffee experiences and insights.
- Contributing and interacting with engaging content on coffee culture.
- Discovering the latest trends, techniques, and best practices in the world of coffee.
- Facilitating discussions and exchanges within a supportive coffee-loving community.

Accessible across various devices and browsers, Cups of Joy aims to demystify the complexities of coffee, making the art of brewing and appreciation accessible to a diverse audience. Whether you're a seasoned barista, a coffee connoisseur, or a curious newcomer, the platform offers tailored resources to support your journey into the world of coffee.

Cups of Joy envisions fostering a collaborative ecosystem where members can learn, share, and grow together in their love for coffee. By engaging with the platform, users can stay ahead of coffee trends, enhance their brewing skills, and connect with like-minded individuals. As the platform evolves, future enhancements will include advanced interactive features, further enriching the user experience and community engagement around the shared passion for coffee.

# UX - User Experience

The UX design of Cups Of Joy revolves around creating an immersive and engaging experience for coffee enthusiasts. With a focus on community, personalization, and seamless navigation, we aim to provide a delightful journey through the world of coffee. Here's a breakdown of our user experience:

- **Intuitive Navigation:** Our user-friendly interface ensures effortless exploration of articles, reviews, and community contributions, making it easy for users to find their desired content.
- **Responsive Design:** Whether accessing Cups Of Joy from a desktop, tablet, or mobile device, our responsive layout adapts seamlessly, ensuring a consistent and enjoyable experience across all platforms.
- **Engaging Content:** Our articles, reviews, and community posts are crafted to captivate and inform, offering a wealth of knowledge and insights into the art of coffee appreciation.
- **Personalization:** Users can create personalized accounts, allowing them to save their favorite articles, follow fellow coffee enthusiasts, and curate their own collection of coffee experiences.

- **Interactive Community:** We foster a vibrant community where users can share their passion, exchange ideas, and engage in discussions through comments, likes, and personal reviews of coffee shops and flavors.

- **Seamless Contribution:** Our platform empowers users to contribute their own content, whether it's writing reviews, sharing personal coffee stories, or offering tips and recommendations to fellow enthusiasts.

Overall, the UX design of Cups Of Joy aims to create an immersive and inclusive environment where coffee lovers can explore, learn, and connect, all while savoring the rich flavors and experiences that the world of coffee has to offer.

# Design

## Colour Scheme

The color scheme for Cups Of Joy is carefully crafted to evoke a warm, inviting, and coffee-inspired atmosphere. Here's a detailed breakdown:

[Coolors](https://color.romanuke.com/tsvetovaya-palitra-1160/) - Colour Scheme for Cups Of Joy website

![Palette](documentation/colour/colorscheme.png)

- **#4a5060 (Dark Grayish Blue):** This deep, rich shade is used as the primary background color for the navigation menu, creating a cozy and grounding foundation for the website.

- **#70AFE2 (Bright Sky Blue):** Reminiscent of a clear morning sky, this vibrant hue is employed for accents, buttons, and interactive elements, adding a refreshing and energizing touch to the design.

- **#926e5a (Warm Brown):** Inspired by the rich tones of freshly brewed coffee, this earthy shade is utilized for accents and highlights, evoking a sense of comfort and familiarity.

- **#929fb0 (Soft Gray):** This muted gray tone serves as a complementary color, providing a subtle backdrop for content and allowing the other colors to shine.

- **#FFFFFF (White):** Used for backgrounds, text, and other elements, white creates a clean and crisp canvas, ensuring excellent readability and contrast.

- **#000000 (Black):** This bold and classic color is used for text, borders, and other accents, providing a strong contrast and adding depth to the overall design.

The color palette is carefully curated to create a harmonious and visually appealing experience, capturing the essence of coffee culture while maintaining a modern and inviting aesthetic. The deep blues and grays establish a cozy ambiance, while the warm browns and vibrant accents evoke the rich flavors and aromas of coffee.

This color scheme not only enhances the visual appeal of Cups Of Joy but also supports usability and accessibility, guiding users through the platform and creating a welcoming environment for coffee enthusiasts to explore, connect, and indulge in their passion.

## Fonts

The font choices for **Cups Of Joy** are carefully curated to create a warm, inviting, and coffee-inspired atmosphere. By leveraging the power of typography, we aim to enhance the user experience and immerse our visitors in the rich world of coffee culture.

### Google Fonts

**Cups Of Joy** utilizes fonts from  [Google Fonts](https://fonts.google.com/), a library of open-source font families, ensuring easy integration and accessibility across various devices and platforms.

#### Roboto
- **Usage:** Body text, descriptions, and content.

- **Characteristics:** Clean, modern, and highly legible, with a friendly and approachable design.

- **Reason for Selection:** Roboto's simple yet elegant style perfectly complements the cozy and welcoming vibe of Cups Of Joy. Its readability ensures that our content is easily consumable, allowing coffee enthusiasts to immerse themselves in the stories and experiences we share.

[Roboto on Google Fonts](https://fonts.google.com/specimen/Roboto)

#### Lato
- **Usage**: Headings, titles, and emphasis
- **Characteristics**: A harmonious blend of soft curves and strong lines, striking a balance between warmth and sophistication.
- **Reason for Selection**: Lato's unique character captures the essence of coffee culture – a fusion of comfort and craftsmanship. Its distinctive yet approachable style draws attention to important elements, guiding users through the platform while evoking a sense of artistry and passion.

[Lato on Google Fonts](https://fonts.google.com/specimen/Lato)

By combining the friendly readability of Roboto with the warm sophistication of Lato, Cups Of Joy creates a typographic experience that resonates with coffee lovers. Each letter, word, and line invites users to explore, savor, and connect with the rich tapestry of flavors, aromas, and stories that make the coffee world so captivating.

# Project Planning

## Strategy Plane

**Project Overview:**  
Cups Of Joy is an immersive online platform dedicated to celebrating the rich culture of coffee. It serves as a vibrant community hub where coffee enthusiasts can explore captivating articles, engage in discussions, contribute reviews, and share their personal coffee journeys. With personalized accounts, users can curate their favorite content, follow fellow connoisseurs, and actively participate by writing reviews, sharing stories, and offering recommendations. Whether you're a seasoned barista or a curious newcomer, Cups Of Joy invites you to indulge in the magic of coffee, connect with like-minded individuals, and embark on a flavorful adventure through the vast landscape of artisanal brews.

**Site Goals:**
- Create an engaging platform where coffee lovers can explore and learn about the world of coffee through informative articles and reviews.

- Build a vibrant community that encourages members to share their passion, experiences, and knowledge about coffee.

- Offer a user-friendly interface that is accessible and easy to navigate, ensuring a seamless experience for both desktop and mobile users.

- Enable personalized features that allow members to create accounts, save their favorite content, follow other coffee enthusiasts, and contribute their own reviews and stories.

- Continuously enhance the platform based on user feedback and evolving trends in the coffee industry, ensuring a dynamic and up-to-date experience.

## Agile Methodologies - Project Management:  
Cups Of Joy embraces Agile methodologies, enabling iterative development and continuous enhancement. Through GitHub Projects, tasks are efficiently managed, and progress is tracked using a Kanban-style board, ensuring a seamless workflow and timely delivery of new features.ard.

### Story Points Allocation

**Story Points Distribution**
Story points were meticulously assigned to each user story, quantifying the effort and complexity involved in developing features for Cups Of Joy. This approach facilitated effective workload estimation and task prioritization, ensuring a smooth development process.

**Allocation Guidelines:**
- **Must-have Stories**: Core functionalities like creating user accounts, writing reviews, and sharing content were given the highest priority, ensuring the platform's primary purpose was met.
- **Should-have Stories**: Features that improve the overall user experience, such as personalization options and community engagement tools, were considered important but not critical. These were prioritized after the essential features were implemented.
- **Could-have Stories**: Additional features like integration with external coffee communities or advanced analytics were considered desirable but not essential for the initial launch of Cups Of Joy.

### Sprint Planning Example
Here is an example of how story points are managed and allocated across different categories in sprints:

- **Total Story Points for the Sprint**: 100
- **Must-have Points**: 40 (40% of the total)
- **Should-have Points**: 50 (50% of the total)
- **Could-have Points**: 10 (10% of the total)

**Example Milestones:**
- **Milestone 1: Core Functionality**
  - Total Story Points: 60
  - Breakdown:
    - Must-have: 36 points
    - Should-have: 24 points
- **Milestone 2: Enhanced User Experience**
  - Total Story Points: 80
  - Breakdown:
    - Must-have: 32 points
    - Should-have: 48 points

### MoSCoW Prioritization:

Cups Of Joy follows the MoSCoW prioritization method to ensure a structured and efficient development approach:

- **Must Haves**: Fundamental features enabling users to read articles, create accounts, save favorites, and contribute reviews and comments about coffee shops and flavors.
- **Should Haves**: Enhancing the platform with personalization options, advanced search capabilities, and community engagement tools like following fellow enthusiasts.
- **Could Haves**: Additional functionalities such as integration with external coffee communities, gamification elements to encourage participation, and advanced analytics.
- **Won't Haves**: Features deemed non-essential for the initial launch, like a dedicated e-commerce platform or third-party advertising integrations.

### User Stories, Milestones and Epics

#### Users Stories

**User stories** are a brief statement of intent that captures what a user does or needs to do as part of their job function. They are written in non-technical language and focus on the value or outcome that the user

| Epic                                               | Title                                    | User Story                                                                                                                                                                        |  MoSCoW Priority |  Milestone                   |
|----------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------------------|
| EPIC 1 : Website Content   Creation and Publishing | Manage and Publish Articles              | As an admin, I want to manage   and publish articles, so that I can control the website's content.                                                                                | **Must Have**    | Core Features Development    |
| EPIC 1 : Website Content   Creation and Publishing | Moderate User-Submitted Reviews          | As an admin, I want to moderate user-submitted reviews, so   that I can maintain the quality and appropriateness of the content.                                                  | **Must Have**    | Core Features Development    |
| EPIC 1 : Website Content   Creation and Publishing | Like, Save Favorite Articles and Reviews | As a registered user, I want to   comment, like and save articles as favorites, so that I can easily access   them later.                                                         | **Must Have**    | Core Features Development    |
| EPIC 1 : Website Content   Creation and Publishing | Write Article Comments                   | As a registered user, I want to add and manage comments on   articles, so that I can actively participate in discussions and share my   thoughts.                                 | **Must Have**    | User Experience Enhancements |
| EPIC 1 : Website Content   Creation and Publishing | Moderate Article Comments                | As an admin, I want to manage and moderate comments on   articles, so that I can maintain the quality and appropriateness of the   content.                                       | **Must Have**    | Core Features Development    |
| EPIC 1 : Website Content   Creation and Publishing | Write Coffee Shop Reviews                | As a registered user, I want to write, edit, and delete my own   coffee shop reviews, so that I can contribute to the community and share my   experiences.                       | **Should Have**  | User Experience Enhancements |
| EPIC 1 : Website Content   Creation and Publishing | Moderate Coffee Shop Reviews             | As an admin, I want to manage and moderate coffee shop   reviews, so that I can maintain the quality and appropriateness of the   content.                                        | **Must Have**    | User Experience Enhancements |
| EPIC 2: Website Usability and   Navigation         | Intuitive Website Navigation             | As a visitor, I want to easily navigate through the website's   content and find relevant information, so that I can explore coffee-related   topics efficiently.                 | **Must Have**    | Core Features Development    |
| EPIC 2: Website Usability and   Navigation         | Account Features Navigation              | As a registered user, I want to   personalize my website experience and access my account-related features   easily, so that I can efficiently manage my content and preferences. | **Must Have**    | Content Administration       |
| EPIC 2: Website Usability and   Navigation         | Administrative Dashboard Access          | As an admin, I want to access and navigate the website's   administrative features efficiently, so that I can manage content and user   accounts effectively.                     | **Must Have**    | Content Administration       |
| EPIC 2: Website Usability and   Navigation         | Search Function                          | As   a visitor, I want to easily search through the website's content by keywords,   tags, or categories.                                                                         | **Must Have**    | User Experience Enhancements |
| EPIC 2: Website Usability and   Navigation         | Filter Coffee Shop Reviews               | As a visitor, I want to easily filter and discover reviews and   comments about different coffee shops, so that I can make informed decisions   about where to visit.             | **Must Have**    | User Experience Enhancements |
| EPIC 3: Content Discovery and   Exploration        | Browse and Read Articles                 | As   a visitor, I want to browse and read articles on the website, so that I can   learn about coffee culture and explore different topics.                                       | **Must Have**    | User Experience Enhancements |
| EPIC 3: Content Discovery and   Exploration        | View Coffee Shop Reviews                 | As   a visitor, I want to view coffee shop reviews, so that I can make informed   decisions about where to visit.                                                                 | **Must Have**    | User Experience Enhancements |
| EPIC 3: Content Discovery and   Exploration        | Favorite and Manage Articles             | As a registered user, I want to favorite articles and manage   my favorite list, so that I can easily access and revisit content that   interests me.                             | **Should Have**  | User Experience Enhancements |
| EPIC 3: Content Discovery and   Exploration        | Read Article Comments                    | As a visitor, I want to read comments on articles, so that I   can gain additional insights and perspectives from the community.                                                  | **Must Have**    | User Experience Enhancements |
| EPIC 3: Content Discovery and   Exploration        | View Article Likes                       | As a visitor, I want to see the number of likes on articles,   so that I can gauge the popularity and engagement of the content.                                                  | **Should Have**  | User Experience Enhancements |
| EPIC 3: Content Discovery and   Exploration        | Like and Unlike Articles                 | As a registered user, I want to like or unlike articles, so   that I can express my interest and engagement with the content.                                                     | **Should Have**  | User Experience Enhancements |
| EPIC 3: Content Discovery and   Exploration        | Read Coffee Shop Reviews                 | As a visitor, I want to read reviews about coffee shops, so   that I can make informed decisions about where to visit.                                                            | **Must Have**    | User Experience Enhancements |
| EPIC 4: User Account                               | Create and Manage User Profile           | As a registered user, I want to create and manage my account   profile, so that I can personalize my experience and save preferences.                                             | **Must Have**    | Core Features Development    |
| EPIC 4: User Account                               | User Registration                        | As   a visitor, I want to have the option to sign up for an account, so that I can   access additional features and personalized content.                                         | **Must Have**    | Community   Engagement       |
| EPIC 4: User Account                               | User Management                          | As an admin, I want to manage registered users from the admin   back office, so that I can oversee and maintain user accounts effectively.                                        | **Must Have**    | Core Features Development    |

[Cups Of Joy GitHub Link](https://github.com/AmirShkolnik/Cups-of-Joy)

[Cups Of Joy Kanban Board Link](https://github.com/users/AmirShkolnik/projects/8)

[Cups Of Joy User Stories Link](https://github.com/AmirShkolnik/Cups-of-Joy/issues)

[Cups Of Joy Milestones Link](https://github.com/AmirShkolnik/Cups-of-Joy/milestones)

#### Milestones

**A milestone**, here from above table represents a significant checkpoint or goal in a project's timeline. Milestones are used to signify the completion of a key phase of work, the achievement of a major objective, or the meeting of a significant deadline. They are critical for tracking progress, setting deadlines, and aligning the team and stakeholders around key project events or achievements. Unlike tasks or user stories, milestones don't involve work themselves but are markers indicating that a specific set of work has been completed.

#### Epics

**An epic** in software development and project management is a large body of work that can be broken down into smaller tasks or stories, often referred to as user stories. Epics are used to organize related tasks that contribute toward a significant, unified objective within a project. They help teams to focus on bigger-picture goals and ensure that all the smaller tasks (user stories) are aligned towards achieving that overarching aim. Epics typically span across multiple sprints or iterations and can take several weeks or months to complete.

##### Epic 1: User Engagement and Interaction
- **Goal:** Enhance user engagement and community interaction through posts, comments, and social features.
- **Associated User Stories:**
  - Comment on a post
  - Bookmark Blog Posts
  - Like Blog Posts
  - View paginated list of posts
  - Search Blog Posts
  - View comments
  - Navigate easily
  - Modify or delete comment on a post
  - Inquiry via Contact Section

##### Epic 2: User Account Management
- **Goal:** Provide a seamless and secure user experience from account registration through to content management.
- **Associated User Stories:**
  - Account Registration
  - 'Register' and 'Login' buttons disappear after 'Login'.
  - Manage posts
  - Create drafts
  - Edit Existing Blog Post
  - Approve comments
  - Delete Existing Blog Post
  - Add Post USER STORY: Allow Registered user to Create New Posts

##### Epic 3: Core Platform Development
- **Goal:** Establish the foundational elements of the Software Stacks platform, including database creation, deployment, and basic functionalities.
- **Associated User Stories:**
  - Creating the Database in ElephantSQL
  - Deploying the Django Project on Heroku
  - Software Stacks Blog
  - Create Project App
  - Open a Post
  - Browse without Logging in

##### Epic 4: Content Management and Administration
- **Goal:** Empower authors with comprehensive tools for content creation, modification, and management.
- **Associated User Stories:**
  - EDIT POST USER STORY: Enable Post Modifications by Author/Post Owner.
  - DELETE POST USER STORY: Facilitate Removal of Outdated or Incorrect Posts
  - ADD POST USER STORY: Allow Registered user to Create New Posts
  - TESTING: Implement Comprehensive Testing
  - VALIDATION: Enhance Data Validation

##### Epic 5: Community Building and Feedback
- **Goal:** Foster community interaction and feedback through enhanced contact form functionalities and about page updates.
- **Associated User Stories:**
  - CONTACT FORM USER STORY: Marking Contact Requests as "Read"
  - CONTACT FORM USER STORY: Contact Form Submission Feature(Site Owner)
  - CONTACT FORM USER STORY: Contact Form Submission Feature (Registered User)
  - ABOUT APP USER STORY: Add and update the about text
  - ABOUT APP USER STORY: Read about the site

##### Epic 6: Documentation and Quality Assurance
- **Goal:** Ensure the platform's reliability and ease of use through comprehensive documentation, testing, and data validation.
- **Associated User Stories:**
  - DOCUMENTATION: Create Comprehensive Documentation
  - VALIDATION: Enhance Data Validation
  - TESTING: Implement Comprehensive Testing

Each epic captures a significant area of functionality or development goal, providing a roadmap for progressing from initial platform setup to a fully-featured, user-engaged community platform.

## Scope Plane

**Purpose:**
Software Stacks aims to educate and engage users interested in various software technologies, focusing on Front-End Development, E-Commerce, and Predictive Analysis. It serves as a platform for both novice and experienced developers to explore articles, tutorials, and community insights.

**Goals:**
- Provide comprehensive guides and articles on key software development topics.
- Offer a community-driven platform where users can interact, and learn from each other.
- Enable users to stay updated with the latest trends and best practices in software technology.

**Target Audience:**
- Novice to experienced software developers.
- Individuals interested in the practical applications of software technology in business.
- Educators and students looking for resources on software development and technology trends.

**User Needs:**
- Access to reliable and up-to-date information.
- Ability to interact with other community members.
- Tools to navigate content based on specific interests or needs.

**Features:**
- Detailed articles and blog posts categorized by technology themes.
- Regular updates and new content notifications.
- User profiles for personalized experiences and content tracking.

## Structural Plane

**Information Architecture:**
- **Home Page:** Overview of the site, featured articles, and direct access to major categories.
- **Category Pages:** Dedicated pages for each major topic (Front-End Development, E-Commerce, Predictive Analysis) featuring articles.
- **Post Detail Pages:** Comprehensive content on chosen topics, including images, and more information.
- **About & Contact Pages:** Organized by category to facilitate discussions and interactions among users.
- **Registration and SignIn Page:** Users can signup and signin to more interactions.
- **User Profile:** Personalized area where users can manage their preferences, saved articles, and contributions to discussions.

**Navigation:**
- **Primary Navigation:** Direct links to each major category from every page.
- **Secondary Navigation:** Links to user profiles, contact information, and about page.
- **Footer Navigation:** Links to privacy policy, terms of use,  and social media.

**Interaction Design:**
- Responsive design to ensure usability across devices.
- Interactive elements such as buttons, links, and forms are designed for ease of use.
- Visual cues (icons, color changes) for interactive elements to enhance user experience.

## Skeleton & Surface Planes

### Wireframes

I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

#### Home Page Wireframes
<details>
<summary>Click to View Home Page wireframes</summary>

**Mobile**
![wireframes](documentation/wireframes/home.JPG)

**Tablet**
![wireframes](documentation/wireframes/tab.JPG)

**Desktop**
![wireframes](documentation/wireframes/phone.JPG)

</details>

#### Categories Page Wireframes
<details>

<summary>Click to View Categories Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/categories.JPG)

</details>

#### Post Detail Page Wireframes
<details>

<summary>Click to View Post Detail Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/post_detail.JPG)

</details>

#### About & Contact Page Wireframes
<details>

<summary>Click to View About & Contact Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/about.JPG)

</details>

#### Add Post Page Wireframes
<details>

<summary>Click to View Add Post Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/add_stack.JPG)

</details>

#### Register Page Wireframes
<details>

<summary>Click to View Register Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/register.JPG)

</details>

#### Login Page Wireframes
<details>

<summary>Click to View Login Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/login.JPG)

</details>

#### Logout Page Wireframes
<details>

<summary>Click to View Logout Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/logout.JPG)

</details>

#### My Bookmarks Page Wireframes
<details>

<summary>Click to View My Bookmarks Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/bookmarked.JPG)

</details>

#### My Likes Page Wireframes
<details>

<summary>Click to View My Likes Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/liked.JPG)

</details>

#### My Comments Page Wireframes
<details>

<summary>Click to View My Comments Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/comments.JPG)

</details>

#### My Posts Page Wireframes
<details>

<summary>Click to View My Posts Page wireframes</summary>

**Desktop**
![wireframes](documentation/wireframes/posts.JPG)

</details>

### Database Schema - Entity Relationship Diagram

I've used [dbdiagram](https://dbdiagram.io/home) to design my site's ERD.

#### Database Schema

The Software Stacks application is structured on a robust database schema designed to facilitate the efficient organization and retrieval of data. Below is an overview of the database schema and the relationships between the different entities.

#### Entity Relationship Diagram (ERD)

The Entity Relationship Diagram (ERD) represents the database schema of Software Stacks, detailing the system's tables, the data fields within them, and the relationships between the tables.

![ERD of Software Stacks](documentation/screenshots/erd.JPG)

#### Tables Overview

- **User**: Stores information about the users of the platform, including username, email, and password. The `is_staff` field indicates whether a user has administrative privileges.

- **Profile**: Contains extended user information such as name, join date, and bookmarks. This table extends the `User` table by associating profiles with user accounts.

- **Blog**: Central to the application, the `Blog` table holds data about blog posts including title, content, and metadata like creation date and whether the post is approved for public viewing.

- **Comment**: Enables the community aspect of the blog by storing user comments on blog posts. Each comment is linked to a specific post and user.

- **Category**: Categories allow for the organization of blog posts into topics, making it easier for users to find content related to specific subjects.

- **About**: This table likely contains static information about the application, such as the company's background, mission statement, and contact details.

- **Contact**: Presumably used for storing user inquiries submitted through the platform's contact form.

#### Relationships

- A **one-to-many** relationship exists between `User` and `Blog`, where one user can author many blog posts.
- A similar **one-to-many** relationship is set between `Blog` and `Comment`, allowing multiple comments to be associated with a single blog post.
- The `Profile` table has a **one-to-one** relationship with the `User` table, extending it with additional personal information.
- The `Category` table is linked to the `Blog` table in a **many-to-one** relationship, categorizing each blog post.
  
#### Design Considerations

The schema was designed with scalability in mind, ensuring that as the platform grows, new features and data types can be easily incorporated. For example, the separation of the `User` and `Profile` tables allows for flexible user management and the possibility to include additional user attributes in the future without altering the core user authentication system.

### Security

Security is a critical aspect, especially for a platform like Software Stacks that handles user-generated content and personal data.

#### Data Encryption
- All sensitive data, including user passwords and personal information, are encrypted using robust encryption methods to protect against unauthorized access and breaches.

#### CSRF Tokens
- CSRF (Cross-Site Request Forgery) tokens are included in every form to help authenticate the request with the server when the form is submitted. Absence of these tokens can leave a site vulnerable to attackers who may steal a users data.

#### AllAuth  

- Django AllAuth is an installable framework that takes care of the user registration and authentication process. Authentication was needed to determine when a user was registered or unregistered and it controlled what content was accessible on **SoftwareStacks**

# Features

## Existing Features

### Features Functionality

Software Stacks is a dynamic web application that allows users to engage with content across various technology domains. Below is a table highlighting its features, detailing the level of access for unregistered and registered users, and the CRUD (Create, Read, Update, Delete) functionalities available:

| Feature                   | Unregistered User Access | Registered User Access         | CRUD Functionality               |
|---------------------------|--------------------------|--------------------------------|----------------------------------|
| **Landing Page**          | Viewable                 | Viewable                       | Read                             |
| **Registration**          | Available                | N/A                            | Create                           |
| **Login**                 | Available                | N/A                            | Create/Read                      |
| **Browse Posts**          | Viewable                 | Viewable                       | Read                             |
| **View Categories**       | Viewable                 | Viewable                       | Read                             |
| **Post Details**          | Limited Interaction      | Full Interaction (like, comment, bookmark) | Read/Create/Update/Delete    |
| **Profile Management**    | Not Available            | Available                      | Create/Read/Update/Delete        |
| **Create New Post**       | Not Available            | Available                      | Create                           |
| **Edit/Delete Post**      | Not Available            | Available (Own Posts)          | Update/Delete                    |
| **Like Posts**            | Not Available            | Available                      | Create/Delete                    |
| **Bookmark Posts**        | Not Available            | Available                      | Create/Delete                    |
| **Comment on Posts**      | Not Available            | Available                      | Create/Update/Delete             |
| **Search Functionality**  | Available                | Enhanced (user-specific results) | Read                             |
| **User Interaction**      | Not Available            | Follow/Unfollow Users, Interact with Community | Create/Read/Delete             |
| **About & Contact**       | Viewable                 | Viewable                       | Read                             |
| **Search**            | Available                    | Available        | Not Available                    |                 |

---

### CRUD Functionality

The table below describes the CRUD operations that can be performed on Software Stacks' main features by a registered, logged-in user.

| Feature               | Create                    | Read                        | Update               | Delete                 |
|-----------------------|---------------------------|-----------------------------|----------------------|------------------------|
| **User Accounts**     | Sign up for a new account | View own and others' profiles | Edit own profile     | Deactivate/Delete account |
| **Posts**             | Publish new posts         | Browse and read all posts  | Edit own posts       | Remove own posts       |
| **Comments**          | Comment on posts          | View comments              | Edit own comments    | Delete own comments    |
| **Likes**             | Like posts and comments   | See likes on posts/comments | -                    | Unlike posts/comments  |
| **Bookmarks**         | Bookmark posts            | View bookmarked posts      | -                    | Remove bookmarks       |
| **Search**            | -                         | Search posts/users         | -                    | -                      |

Certainly, here's a detailed existing features section for Software Stacks using the provided template:

### All Existing Features with Screenshots

#### Home Page

  - The initial point of contact with Software Stacks, where users can understand the platform's offerings. Featured articles, latest stacks, and prominent categories are displayed here.

  ![Home Page Screenshot](documentation/screenshots/home.JPG)

#### User Registration, Login, and Logout

  - New users can sign up by providing their username, email, and password. Existing users can log in using their credentials to access personalized features.

  **Registration/SignUp**
      ![Sign Up Screenshot](documentation/screenshots/signup.JPG)

  **Login/SignIn**  
    ![Login Screenshot](documentation/screenshots/signin.JPG)

  **Logout/Signout**
    ![Logout Screenshot](documentation/screenshots/signout.JPG)

#### User Profile

  - Upon logging in, users can view and edit their profiles, see their published stacks, and manage bookmarks and likes.

  ![Profile Screenshot](documentation/screenshots/login2.JPG)
  ![Profile Screenshot](documentation/screenshots/profile.JPG)

#### Add Post

  - Registered users can contribute by creating their own stacks. They can include a title, content, images, and select categories for their Post.

  ![Add Post Screenshot](documentation/screenshots/add_stack.JPG)

#### Search Functionality

  - Both registered and unregistered users can search for specific stacks or browse categories using the search bar on the navigation menu.

  ![Search Screenshot](documentation/screenshots/search.JPG)

#### Post Details

  - Users can read detailed views of each post, engage with content through likes, bookmarks, and comments.

  ![Post Details Screenshot](documentation/screenshots/postdetail.JPG)

#### Comments and Interactions

  - Users can leave comments on stacks, engage in discussions, and provide feedback to authors. They can also like and bookmark stacks for future reference.

  ![Comments Screenshot](documentation/screenshots/leavecomment.JPG)
  ![Comments Screenshot](documentation/screenshots/posting_comment-as.JPG)
  ![Comments Screenshot](documentation/screenshots/approvedcomment.JPG)
  ![Comments Screenshot](documentation/screenshots/unapprovedcomments.JPG)

#### Responsive Navigation Bar

  - The navigation bar provides easy access to all sections of the site, adjusts for different screen sizes, and includes user authentication options.

  ![Navigation Bar Screenshot](documentation/screenshots/navbar2.JPG)
  ![Navigation Bar Screenshot](documentation/screenshots/navbar.JPG)

#### Categories

  - Users can browse stacks by categories, such as Front-End Development, E-Commerce, and Predictive Analytics, to find content tailored to their interests.

  ![Categories Screenshot](documentation/screenshots/categories.JPG)
  ![Categories Screenshot](documentation/screenshots/cat_fed.JPG)
  ![Categories Screenshot](documentation/screenshots/cat_ecom.JPG)
  ![Categories Screenshot](documentation/screenshots/cat_pa.JPG)

#### My Bookmarks

  - Logged-in users have a personal bookmarks section where they can save stacks for later reading or reference. This personalized list helps users quickly access their favorite content.

  ![My Bookmarks Screenshot](documentation/screenshots/bookmarkedposts.JPG)
  ![My Bookmarks Screenshot](documentation/screenshots/empty-bookmark.JPG)

#### My Likes

    - The 'My Likes' feature allows users to revisit stacks they have liked. This feature encourages users to engage with content and authors they appreciate.

  ![My Likes Screenshot](documentation/screenshots/likedposts.JPG)
  ![My Likes Screenshot](documentation/screenshots/empty-liked.JPG)

#### My Comments

  - Users can review and manage their comments across different stacks. This section provides users with an overview of their contributions and engagements within the community.
  
  ![My Comments Screenshot](documentation/screenshots/commentedposts.JPG)
  ![Comments Screenshot](documentation/screenshots/nocommentempty.JPG)

#### My Posts

  - Content creators can manage their stacks through 'My Posts'. They can view all their contributions, edit existing stacks, or delete any content they no longer wish to share.

  ![My Posts Screenshot](documentation/screenshots/yourposts.JPG)
  ![My Posts Screenshot](documentation/screenshots/noposts_empty.JPG)

#### Pagination

  - Users can navigate through multiple pages of content seamlessly with pagination controls. This feature ensures that the website remains uncluttered and enhances user experience by dividing content into manageable and orderly sections. Users can easily move between pages using 'Previous', 'Next', or direct page number links.

  ![My Pagination Screenshot](documentation/screenshots/pagination.JPG)
  

#### Footer

  - The footer is consistent across the platform and offers additional navigation options, social media links, and legal information.

  ![Footer Screenshot](documentation/screenshots/footer.JPG)

#### Admin Panel

  - Administrators have access to a backend panel where they can manage users, stacks, categories, and comments.

  ![Admin Panel Screenshot](documentation/screenshots/allauth.JPG)

#### Error Handling

  - Custom error pages are designed to inform users of various errors such as 404 Not Found or 403 Forbidden, along with a user-friendly message and a link to navigate back home.

  ![404 Error Page Screenshot](documentation/screenshots/404.JPG)
  ![403 Error Page Screenshot](documentation/screenshots/403.JPG)

## Future Features

**Advanced Search Capabilities**
- **Description**: Implement advanced search options to allow users to filter posts by date, popularity, and specific tags or categories.
- **Benefit**: Helps users find the content they are interested in more efficiently.

**User Profile Customization**
- **Description**: Allow users to customize their profiles with themes, profile pictures, and bio information.
- **Benefit**: Enhances user engagement and personalization on the platform.

**Real-time Notifications**
- **Description**: Introduce real-time notifications for likes, comments, and new posts from followed categories or authors.
- **Benefit**: Keeps users informed and engaged with the content they care about most.

**Mobile App**
- **Description**: Develop a mobile application for iOS and Android to access Software Stacks on the go.
- **Benefit**: Increases accessibility and user engagement by providing a convenient way to browse and interact with content from mobile devices.

**API for Developers**
- **Description**: Offer a public API that allows developers to access and integrate Software Stacks content into their own applications.
- **Benefit**: Expands the platform’s reach and utility, fostering an ecosystem around Software Stacks content.

**Multi-language Support**
- **Description**: Add support for multiple languages to cater to a global audience.
- **Benefit**: Makes the platform accessible to non-English speaking users, expanding the user base.

**Dark Mode**
- **Description**: Introduce a dark mode feature to enhance visual ergonomics by reducing eye strain in low-light conditions.
- **Benefit**: Improves user comfort and accessibility, particularly during night-time browsing.

**Forums and Discussion Boards**
- **Description**: Implement forums and discussion boards where users can engage in deeper discussions and build community.
- **Benefit**: Strengthens the community aspect of Software Stacks, making it a hub for like-minded enthusiasts to share and learn.

These features are designed to enhance the functionality and user experience of Software Stacks, driving greater user engagement and expanding the platform’s capabilities.

# Technology Used

## Frontend
- [**HTML5**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5): Structure of the web pages.
- [**CSS3**](https://developer.mozilla.org/en-US/docs/Web/CSS): Styling of the web content.
- [**JavaScript**](https://developer.mozilla.org/en-US/docs/Web/JavaScript): Enhancements of interactivity and web behaviors.
- [**Bootstrap**](https://getbootstrap.com/): Responsive design and layout framework.

## Backend
- [**Django**](https://www.djangoproject.com/): A high-level Python web framework.
- [**Python**](https://www.python.org/): Backend programming language.
- [**SQLite**](https://www.sqlite.org/index.html) (Development) / [**PostgreSQL**](https://www.postgresql.org/) (Production): Database systems.

## Deployment and Version Control
- [**Git**](https://git-scm.com/): Used for version control.
- [**GitHub**](https://github.com/): Hosts the repository and facilitates version control and collaboration.
- [**Heroku**](https://www.heroku.com/): Platform as a service (PaaS) for deploying applications.

## Development Tools
- [**GitPod**](https://www.gitpod.io/): Preferred IDE for writing and editing code.
- [**Django Extensions**](https://github.com/django-extensions/django-extensions): Provides custom management extensions for Django.

## Libraries and Frameworks

- **asgiref (3.8.1)**: Supports asynchronous capabilities in Django, enabling better performance for asynchronous apps.
- **cloudinary (1.36.0)**: Manages cloud-based image and video storage and optimizations, integrating seamlessly with web applications for media management.
- **crispy-bootstrap5 (0.7)**: Allows Django forms to be styled effortlessly with Bootstrap 5, enhancing form presentation without extensive front-end coding.
- **dj-database-url (0.5.0)**: Simplifies database configuration using a URL scheme, which is especially useful for deployments on platforms like Heroku.
- **dj3-cloudinary-storage (0.0.6)**: Integrates Django projects with Cloudinary for handling static and media files storage.
- **Django (4.2.11)**: The main web framework for the project, providing the necessary tools to build a secure, scalable, and maintainable web application.
- **django-allauth (0.57.2)**: Adds authentication, registration, and account management capabilities, supporting both traditional and social authentication methods.
- **django-bootstrap4 (24.1)**: Facilitates the use of Bootstrap 4 in Django templates for consistent and responsive design across the application.
- **django-crispy-forms (2.1)**: Helps in rendering Django forms in a DRY (Don't Repeat Yourself) manner, allowing form styling through template packs.
- **django-summernote (0.8.20.0)**: Provides a rich text editor for Django forms, enhancing text input fields with WYSIWYG editing capabilities.
- **gunicorn (20.1.0)**: Serves as a Python WSGI HTTP Server for UNIX, enabling Django apps to handle more concurrent traffic.
- **oauthlib (3.2.2)**: A generic implementation of OAuth for sharing authentication across services, used in conjunction with django-allauth.
- **psycopg2 (2.9.9)**: Acts as a PostgreSQL database adapter for Python, essential for database operations in Django projects using PostgreSQL.
- **PyJWT (2.8.0)**: A Python library for encoding, decoding, and verifying JSON Web Tokens (JWT), useful for stateless authentication mechanisms.
- **python3-openid (3.2.0)**: Supports Python 3 applications in implementing OpenID authentication, often used in conjunction with django-allauth.
- **requests-oauthlib (2.0.0)**: Combines the power of the `requests` library with `oauthlib` for OAuth 1 and OAuth 2 authentication of requests.
- **sqlparse (0.4.4)**: A non-validating SQL parser for Python, which provides formatting and syntax analysis for SQL scripts used within Django.
- **urllib3 (1.26.18)**: A powerful HTTP client for Python, used for making HTTP requests in various parts of the application.
- **whitenoise (5.3.0)**: Simplifies static file management in Django by allowing the app to serve its own static files, improving performance and reducing complexity in production setups.

## Validation Tools
- [**W3C Markup Validation Service**](https://validator.w3.org/): For validating HTML5 code.
- [**W3C CSS Validation Service**](https://jigsaw.w3.org/css-validator/): For validating CSS3 code.
- [**JSHint**](https://jshint.com/): A tool that helps to detect errors and potential problems in JavaScript code.
- [**CI Python Linter**](https://pep8ci.herokuapp.com/): Analyzes Python code to look for bugs and signs of poor quality.
- [**Google Lighthouse**](https://developers.google.com/web/tools/lighthouse): For auditing performance, accessibility, and search engine optimization of web pages.

## Others
- [**Cloudinary**](https://cloudinary.com/): An end-to-end image and video management solution.
- [**Favicon.io**](https://favicon.io/): To generate favicon icons for the website.
- [**Font Awesome**](https://fontawesome.com/): Provides icons for enhancing UI/UX.
- [**Tiny Png**](https://tinypng.com/): To compress the images.
- [**Free Convert**](https://www.freeconvert.com/): To convert PNG, JPG, JPEG...images to Webp format.

# Testing

For all testing and validation, please refer to the [TESTING.md](TESTING.md) file.

# Deployment

The deployment process for Software Stacks involves multiple platforms including GitHub, Gitpod, Heroku, ElephantSQL, and Cloudinary. Here's how each part fits into the deployment process:
Below are the respective URLs for the platforms and services used in deploying and managing the Software Stacks application:

## GitHub
- **Repository Setup:** Initially, a GitHub repository is created to host all project code and documentation. This repository is the central hub for version control and collaboration.
[GitHub](https://github.com)

## Gitpod
- **Development Environment:** Gitpod is used as a cloud-based IDE for writing, running, and debugging the code. It is directly integrated with GitHub, allowing seamless pulls and pushes to the repository. [Gitpod](https://www.gitpod.io/)

## Heroku
- **Application Hosting:** Heroku is used to deploy the live application. It is connected to the GitHub repository for continuous deployment. Every push to the main branch triggers a deployment process.
[Heroku](https://www.heroku.com)
  - **Setting up on Heroku:**
    1. Create a new app on Heroku.
    2. Connect the Heroku app to the GitHub repository.
    3. Set up Config Vars in Heroku including `DATABASE_URL`, `SECRET_KEY`, `CLOUDINARY_URL`, `DISABLE_COLLECTSTATIC`, 	1 (this is temporary, and can be removed for the final deployment) etc.
    4. Deploy the main branch using the Heroku dashboard or enable automatic deployments for every push to the main branch.
    5. 
**For deployment Heroku needs two additional files in order to deploy properly.**
- requirements.txt
- Procfile
  
You can install this project's requirements (where applicable) using:

- **pip3 install -r requirements.txt**

If you have your own packages that have been installed, then the requirements file needs updated using:

- **pip3 freeze --local > requirements.txt**

**The Procfile can be created with the following command:**

echo web: gunicorn app_name.wsgi > Procfile
replace app_name with the name of your primary Django app name; the folder where settings.py is located

## ElephantSQL
- **Database Hosting:** ElephantSQL provides a PostgreSQL database service, which is used by the Django application. The `DATABASE_URL` from ElephantSQL is set in the Heroku config vars to connect the application to the database. 

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: tribe).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

## Cloudinary
- **Media Storage:** Cloudinary is used for hosting media files like images. It removes the load of serving static files from Heroku, ensuring better performance and scalability. [Cloudinary](https://cloudinary.com/)
  - **Integration:**
    1. Set up a Cloudinary account.
    2. Configure the Cloudinary settings in the Django settings file with the API keys provided by Cloudinary.
    3. Use Django’s storage backend for Cloudinary to handle media uploads.

# Cloning and Forking

## Cloning the Repository
- **Local Setup:**
  1. Clone the repository: [GitHub repository](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4). 
 `git clone https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4`.
  2. Navigate into the project directory: `cd software-stacks-p4`
  3. Install dependencies: `pip install -r requirements.txt`
  4. Set up local environment variables in a `.env` file.
  5. Run migrations: `python manage.py migrate`
  6. Start the development server: `python manage.py runserver`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://swathikesha-softwaresta-yuwx4g4ondz.ws-eu110.gitpod.io/)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).


## Forking the Repository
- **For Contributions:**
  1. Fork the repository on [GitHub repository](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4).
  2. Clone your forked repository to your local machine.
  3. Follow the local setup steps as above.
  4. Make changes and push them back to your fork.
  5. Create a pull request from your fork back to the original repo.

# Credits

## Code

The following blogs/tutorials complemented my learning for this project:

- [Django Docs](https://www.djangoproject.com/)
- [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Blog Article](<https://www.sankalpjonna.com/learn-django/how-to-override-the-save-method-in-your-django-models>)
- [StackOverflow](<https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains>)
- [Very Academy](<https://www.youtube.com/watch?v=H4QPHLmsZMU>)
- [StackOverflow for Pagination ](<https://stackoverflow.com/questions/30864011/display-only-some-of-the-page-numbers-by-django-pagination>)

## Media

The following sites were used to gather the photographic media used:
- [Freepik](https://www.freepik.com/)

## Additional reading/tutorials/books/blogs

- [Dee Mc](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy) for Django
- [Geeks for Geeks](https://www.geeksforgeeks.org/python-programming-language/?ref=ghm) for additional Python learning.
- PP4 walkthrough projects.
- Used Google for website text and post content.

## Acknowledgements

- Many thanks to **my husband and son** for their continued support.
- Thank you to my Code Institute mentor **Jack Wachira** for his positive support, guidance and advice.
- Thanks to **Kristyna**, Cohort facilitator at Code Institute how she always there to give all the infromation needed and for keeping positive the energy up.
- Thanks to my **fellow students** for constantly inspiring on slack and being there for each other to help in trouble.

**Due to time constraints, I was unable to add more features and functionality. However, I am happy and satisfied with my project and its current learning outcomes.** *"Putting a lot of time and effort into this project feels GREAT!"*