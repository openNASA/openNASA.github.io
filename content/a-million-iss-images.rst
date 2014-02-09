A Million ISS Images
####################
:date: 2013-04-02 09:35
:author: nbergey
:category: OpenGov
:tags: ISS, Open Data, Participation, space apps
:slug: a-million-iss-images

*We've always been a fan of `ISS Notify`_... but when the open.NASA team
saw the `latest project`_ from `Nate Bergey`_, we wanted to get him to
share it directly with you. This project exemplifies why we share our
`open data`_ with the public as well as the kind of inspiration we're
anticipating at the upcoming `Space Apps Challenge`_. Hopefully this
will be the first in a long series of posts by Nate and other innovators
who are using space data to create great things. *

I’ve always been fascinated with space. I’ve done plenty of `looking up
at the skies`_ throughout my life, wondering what I would see if I were
up there looking back down below.

I use NASA data every day, even though I don’t work for NASA.  They have
many detailed and rich datasets available for reading/viewing by the
general public. The problem though is that they are often published in
archaic formats buried under hard to use interfaces. But with a little
ingenuity, anyone can get their hands on amazing data about the universe
we live in.

For instance, I love the photographs that are being downloaded from the
International Space Station’s cameras. Each one inspires me to dream of
floating high above our blue planet. Sometimes, I wonder, what do the
astronauts mostly take pictures of? In order to find out, I had to get
some data.

The Image Science & Analysis Laboratory, at Johnson Space Center in
Houston, Texas, maintains a `giant database of all the photographs
astronauts have ever taken in space`_.  Luckily, they also have a
`database search page`_ that allows you to ask for information about
photos from particular missions, and features all kinds of metadata.

It’s possible to `screen scrape`_ the search result pages, using popular
programing languages like python and tools like `Beautiful Soup`_,
creating your personal mini database of the data you care about. In my
case, it was the approximate latitude and longitude of the photos taken
from the ISS, or at the very least, the position of the station when the
photo was taken.

So, I wrote some python scripts to do this for me a few pages at a time,
and I ended up with the location of 1,129,177 photos!\ ** **

Visualization
=============

The next step was to put the data on a map. To do this, I decided to
draw each photo as a single pixel on a blank image. This is actually
really easy in python using cairo.

The result is a giant map of Earth, based only on images from the ISS!

|All ISS|

Most of the photos are taken of land masses. Coastlines, islands and
cities seem to be popular targets. So much, that it’s possible to
identify outline of continents. This makes sense, photos of clouds over
an otherwise blank ocean get old after a while. I’m sure every astronaut
has taken at least one photograph of the town they grew up in.

Now, let’s divide up the dots by mission. Is there any pattern? Here I
draw each mission in a different color:

|All ISS Missions|

The map is dominated by purple, light blue, and green with some yellow.
Also notice that the purple dots make almost uninterrupted orbit lines
while most of the other dots seem to fill in randomly. This is because
during Expedition 30/31 `Don Pettit took dozens of amazing time lapse
sequences`_ consisting of hundreds of images taken continuously as the
ISS orbited. In fact he’s single-handedly responsible for almost half
the images taken on orbit!

One more thing we can do is add a map underneath to see exactly how the
photos line up:

|All ISS Missions by Map|

You can see that the ISS stays between about 50° and -50° latitude as it
orbits the Earth The `inclination`_ of the orbit of the station is in
fact 51.6°.

Since it’s hard to see the overlapped colors in the above image here is
a collection maps with the photos from each mission mapped separately:

|Multiple Maps|

This is just some of the data that NASA has to offer. If you’re
interested in getting involved in things like this I suggest taking a
look at `data.nasa.gov`_ and `International Space Apps Challenge`_.

You can also `download the data I scraped from my github page`_.

 

.. _ISS Notify: http://mechanicalintegrator.com/2011/iss-notify/
.. _latest project: http://natronics.github.com/ISS-photo-locations/
.. _Nate Bergey: https://twitter.com/natronics
.. _open data: http://data.nasa.gov/
.. _Space Apps Challenge: http://spaceappschallenge.org/
.. _looking up at the skies: http://www.flickr.com/photos/natronics/5310760993/
.. _giant database of all the photographs astronauts have ever taken in space: http://eol.jsc.nasa.gov/
.. _database search page: http://eol.jsc.nasa.gov/sseop/mrf.htm
.. _screen scrape: http://en.wikipedia.org/wiki/Web_scraping
.. _Beautiful Soup: http://www.crummy.com/software/BeautifulSoup/
.. _Don Pettit took dozens of amazing time lapse sequences: http://vimeo.com/61083440
.. _inclination: http://en.wikipedia.org/wiki/Orbital_inclination
.. _data.nasa.gov: http://data.nasa.gov/
.. _International Space Apps Challenge: http://spaceappschallenge.org/
.. _download the data I scraped from my github page: http://natronics.github.com/ISS-photo-locations/

.. |All ISS| image:: http://open.nasa.gov/wp-content/uploads/2013/04/all_iss.preview.png
   :target: http://open.nasa.gov/wp-content/uploads/2013/04/all_iss.preview.png
.. |All ISS Missions| image:: http://open.nasa.gov/wp-content/uploads/2013/04/all_iss_missions.preview.png
   :target: http://open.nasa.gov/wp-content/uploads/2013/04/all_iss_missions.preview.png
.. |All ISS Missions by Map| image:: http://open.nasa.gov/wp-content/uploads/2013/04/all_iss_missions_map.preview.png
   :target: http://open.nasa.gov/wp-content/uploads/2013/04/all_iss_missions_map.preview.png
.. |Multiple Maps| image:: http://open.nasa.gov/wp-content/uploads/2013/04/small_mult.preview.png
   :target: http://open.nasa.gov/wp-content/uploads/2013/04/small_mult.preview.png
