---
author: sherron
comments: false
date: 2012-04-06 05:36:43+00:00
layout: post
slug: behind-the-site-spaceappschallenge-org
Title: 'Behind the Site: spaceappschallenge.org'
wordpress_id: 6180
categories:
- OpenGov
tags:
- css3
- django
- html5
- space apps challenge
- spaceapps
- technology
- web development
- wordpress
---

If you follow openNASA, you’ve no doubt heard of the [International Space Apps Challenge](http://spaceappschallenge.org) – our global codeathon taking place on all seven continents and in space next month. Last month, we launched a new [website](http://spaceappschallenge.org) for the Challenge that allows visitors to sign up for events, view and submit challenges, and learn more about the event. We put a lot of effort in to making it cutting edge by using the latest web technologies and standards to provide an excellent user experience. This post will showcase just some of the methods we used to make the site, and give you some ideas for creating one yourself.

[![](http://open.nasa.gov/wp-content/uploads/2012/03/Screen-shot-2012-03-23-at-2.09.24-AM-300x241.png)](http://open.nasa.gov/wp-content/uploads/2012/03/Screen-shot-2012-03-23-at-2.09.24-AM.png)

**The Methodology**

One of the biggest challenges in creating the site was that, due to our global audience, we had to ensure the site is compatible and accessible across a wide range of devices, screen sizes, and internet speeds. The site is fully responsive, meaning that by using some HTML and CSS trickery, we’re able to serve up different designs depending on the user’s screen size. Try it now – visit [spaceappschallenge.org](http://spaceappschallenge.org) on a smartphone and a desktop at the same time. You’ll see two different designs, even though each uses the same HTML files.

Responsive design is becoming increasingly important on the web as more and more users access websites using smartphones, tablets, and other small devices. By optimizing the site to a range of user experiences, we don’t lock people in to viewing a design best suited for a desktop monitor.

The site also makes much use of the HTML5 and CSS3 standards. CSS3 allows us to duplicate a lot of the design features that previously required images, meaning that pages load faster and our design is more flexible. The framework of the site is built off of a combination of the [Skelton](http://getskelton.com) flexible grid system, with some design elements taken from [Twitter Bootstrap](http://twitter.github.com/bootstrap/). We also make use of [Font Awesome](http://fortawesome.github.com/Font-Awesome/), which allows us to use a webfont for icons rather than images. By using these forward-leaning practices, we can considerably cut down on file sizes and offer a faster and more accessible experience to visitors.

Accessibility for us also meant making the site available in as many different ways as possible. For instance, much of our content is encoded in [Microformats](http://microformats.org/), which extends our HTML in a semantic way to be understandable by machines. Additionally, we're working with our location partners to offer translations of content where appropriate. The Tokyo location, for instance, offers a [Japanese translation](http://tokyo.spaceappschallenge.org).

**The Backend**

Apart from our design philosophy, we also strived to create a backend system that enables flexibility, stability, and performance. The site is hosted on a cloud platform running Linux and powered by [nginx](http://nginx.org/) and [Postgres](http://www.postgresql.org/). While our sites have traditionally run on [WordPress](http://wordpress.org), we decided to go with a Django-based platform. This is due to some of the particular needs of the site, such as event registration and project collaboration. We utilize extensive server-side caching to improve performance and automatically compress and minify our HTML, CSS, and Javascript. On the design side, our templates were styled using [LESS](http://lesscss.org) and we used the helpLESS library to help us do some common tasks more effectively.

**Design Philosophy**

Ultimately, the technologies and methodologies I have written about are the things that the end-user is least likely to care about. On the web, design is paramount. We wanted the Apps Challenge site to be visually striking and immediately impart a sense of global collaboration to the visitor. We spent a lot of effort on creating the main design element on the front page - the map of the world with tags for every location where the Space Apps Challenge is taking place. Now, doing this with a map of the Earth is pretty easy (which is lucky, because we've been adding locations left and right recently!). The difficult part is showing the highest and fastest-moving location: the International Space Station. We first experimented with just showing a static icon of the station over the pacific ocean. Pretty boring. We decided it had to be animated and move across the screen. Here's a little secret, however: the station does not actually show up where it really is on the planet. We experimented with making the image live-update as the station crossed over the globe, but ultimately decided not to for a few reasons:

1) The code required to do so would be much heavier than we were willing to put on the site.
2) The projection of the map on the homepage is slightly different than the projections of most orbital tracks posted by NASA, meaning that we would have had to translate coordinates to our projection.
3) The station would have moved realllllly slowly on the screen. Most users probably wouldn't have even noticed it.

Thus, we made a small sacrifice - instead, the station follows an orbital-like wave across the map using jQuery animation and the [path plugin](https://github.com/weepy/jquery.path).

Beyond the homepage, we focused on making the site lightweight but incorporating design elements that reinforce that feeling of global collaboration - Google Maps integration, for instance.

**Conclusion**

I hope this post has given you at least a glimpse into our web philosophy and the direction in which we see taking our other properties ([open.nasa.gov](open.nasa.gov), [data.nasa.gov](data.nasa.gov), and [code.nasa.gov](code.nasa.gov)) in the future. We see the recent trend of accessible & responsive design as critical to the next generation of web experiences. Our goal is to make our content as open, accessible, and flexible as possible. We are open to feedback and ideas about how we can further this even more - please leave a comment and let us know what you think! Finally, none of what we've accomplished on the site would have been possible without the help of everyone on the Space Apps Challenge team, including Kristen Painting, Ali Llewellyn, Nick Skytland, Elizabeth Sabet, Chris Gerty, and William Eshagh. William was core in creating the backend of the site to go along with the frontend I developed - without him, we'd have no django, no server, and no site. 

If you're interested in hearing more about our approach to web development and user experience, see my [recent talk](http://wordpress.tv/2012/03/06/sean-herron-how-non-profits-and-government-organizations-of-all-sizes-can-use-wordpress-to-successfully-create-and-operate-a-website/) from WordCamp Phoenix on the topic.
