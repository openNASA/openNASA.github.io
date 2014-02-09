Title: Creating spaceappschallenge.org
Date: 2013-04-15 00:04
Author: sherron
Category: OpenGov
Tags: spaceapps, spaceappschallenge, spaceappschallenge.org, web
Slug: creating-spaceappschallenge-org

It's 4:39am and I'm staring at a blank screen.

"Well, that's just great," I say to myself before making a quick edit
and switching over to my command line prompt.

    $ git add . && git commit -m "Please let it work this time"
    $ fab deploy development

I refresh my browser and see an image of the blue marble with 75
colorful icons and a slowly moving International Space Station sliding
across the screen. Success. Issue ticket closed.

That's been the story of my life, and the lives of the rest of the team
behind [spaceappschallenge.org][], over the past few weeks as we
prepared the site to go live, first as a soft launch on March 3rd, and
later as a full rollout last week. We've spent a lot of time on the site
and are really proud of the result.

Last year, I wrote up a brief overview of the platform we created, and I
wanted to do same for our 2013 site. We've rewritten the code from the
ground up to incorporate a lot of the things we wanted to do in 2012 but
weren't able to. The site incorporates some of the latest techniques and
methodologies in web development, and it's our hope that it can serve as
a model for how government websites can be built in the future.

Methodology
-----------

I'm a big fan of responsive and adaptive design. Responsive design is
the concept of making content flexible to the device on which it is
viewed - whether that be on a mobile phone, tablet, laptop, desktop, or
any other medium. With 50% of US web traffic slated to be mobile in the
next few years, and our huge focus on countries where mobile device
deployments far outpace traditional internet access, this was critical.
Our 2012 website was responsive as well (utilizing the Skeleton
framework), but we took it one step further this year by making it
*mobile first*. With mobile first design, we approached the site with a
very different mindset. While traditionally, you would design your
website for the desktop and then scale down to mobile, with mobile first
you design for mobile and then scale up to desktop. For us, this had a
few notable benefits:

1.  Compatibility  
    Rather than try and fight browsers and pull content out that
    doesn't scale or doesn't work, we're able to progressively enhance
    and build on top of a base. This is really important for things like
    Internet Explorer 8 compatibility - rather than things just not
    working we're able to serve a slightly less nice looking experience
    but ultimately still deliver the content.
2.  Ease of Building  
    It's a lot easier to add things on top rather than pull things out.
    Rather than having to write super specific CSS (and probably use a
    lot of undesirable !important tags), we're able to just overwrite
    the CSS we want to.
3.  Information Architecture  
    Building mobile first really forced us to reconsider the importance
    of a lot of our content. You'll notice the front page, for instance,
    has a lot less content than this year. We also concentrated on
    trying to eliminate unneeded links, instead focusing on touch
    friendly imagery and buttons to provide an easier to navigate
    interface.

Backend
-------

As with last year, the site is built on Django, a Python framework.
We've found Django to be both extensible and easy to use, an important
factor considering no one on our team is a full-time developer. We have
four major components of our backend architecture:

-   Locations
-   Challenges
-   Projects
-   Users

Rather than introducing a lot of dependencies on our models as we did
last year, Space Apps 2013 focuses much more on an object-oriented
model. For future usage, it is much easier to move components of the
above four items to other projects or to strike one from another
deployment of the platform.

Frontend
--------

Our fronted is based on Foundation Zurb, a great framework that provides
a lot of baseline CSS and Javascript to jumpstart web projects. We used
a few tools pretty extensively in our development:

### SASS

SASS is a CSS preprocessor that offers a lot of enhancements over plain
CSS, such as nested rules, variables, and mixing to quicken development.

### Leaflet, OpenStreetMaps, & Mapquest Open Maps

Leaflet powers all of the mapping solutions on the site. We use a
combination of OpenStreetMaps and NASA Satellite imagery tiles served by
Mapquest's CDN.

### Isotope

We use Isotope to power some of the sorting and filtering for
Challenges.

### Wysihtml5

Wysihtml5 powers all of our backend WYSIWYG inline editing.

### Typekit

We use Typekit to serve our web fonts

### Disqus

Disqus powers our commenting system on challenges and projects. We've
used their SSO option so that users can use the same identity between
platforms.

### Hackpad

We use Hackpad's new API to offer collaboration tools for challenges and
projects

### Cloudflare

We use Cloudflare to help us more efficiently serve content around the
world.

### Google Apps

We use Google Apps to power some internal mailing lists.

To me, the Space Apps website is much more than just a platform for us
to offer our event on - it's a testbed for some of the latest web
technologies to be played around with. My hope is that others both
inside and outside government can fork our code, learn from our
experiences, and improve on our work.

We also view the Space Apps website as a work in progress - we hope that
citizens like yourself can help us make it even better than it already
is. If you see a bug, something that can be improved, or anything else
you think we should know about, drop us a line in the comments below.
We'd love to hear from you.

  [spaceappschallenge.org]: http://spaceappschallenge.org
