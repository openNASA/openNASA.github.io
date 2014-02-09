Title: A Million ISS Images
Date: 2013-04-02 09:35
Author: nbergey
Category: OpenGov
Tags: ISS, Open Data, Participation, space apps
Slug: a-million-iss-images

*We've always been a fan of [ISS Notify][]... but when the open.NASA
team saw the [latest project][] from [Nate Bergey][], we wanted to get
him to share it directly with you. This project exemplifies why we share
our [open data][] with the public as well as the kind of inspiration
we're anticipating at the upcoming [Space Apps Challenge][]. Hopefully
this will be the first in a long series of posts by Nate and other
innovators who are using space data to create great things. *

I’ve always been fascinated with space. I’ve done plenty of [looking up
at the skies][] throughout my life, wondering what I would see if I were
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
Houston, Texas, maintains a [giant database of all the photographs
astronauts have ever taken in space][].  Luckily, they also have a
[database search page][] that allows you to ask for information about
photos from particular missions, and features all kinds of metadata.

It’s possible to [screen scrape][] the search result pages, using
popular programing languages like python and tools like [Beautiful
Soup][], creating your personal mini database of the data you care
about. In my case, it was the approximate latitude and longitude of the
photos taken from the ISS, or at the very least, the position of the
station when the photo was taken.

So, I wrote some python scripts to do this for me a few pages at a time,
and I ended up with the location of 1,129,177 photos!** **

Visualization {dir="ltr"}
=============

The next step was to put the data on a map. To do this, I decided to
draw each photo as a single pixel on a blank image. This is actually
really easy in python using cairo.

The result is a giant map of Earth, based only on images from the ISS!

[![All ISS][]][All ISS]

Most of the photos are taken of land masses. Coastlines, islands and
cities seem to be popular targets. So much, that it’s possible to
identify outline of continents. This makes sense, photos of clouds over
an otherwise blank ocean get old after a while. I’m sure every astronaut
has taken at least one photograph of the town they grew up in.

Now, let’s divide up the dots by mission. Is there any pattern? Here I
draw each mission in a different color:

[![All ISS Missions][]][All ISS Missions]

The map is dominated by purple, light blue, and green with some yellow.
Also notice that the purple dots make almost uninterrupted orbit lines
while most of the other dots seem to fill in randomly. This is because
during Expedition 30/31 [Don Pettit took dozens of amazing time lapse
sequences][] consisting of hundreds of images taken continuously as the
ISS orbited. In fact he’s single-handedly responsible for almost half
the images taken on orbit!

One more thing we can do is add a map underneath to see exactly how the
photos line up:

[![All ISS Missions by Map][]][All ISS Missions by Map]

You can see that the ISS stays between about 50° and -50° latitude as it
orbits the Earth The [inclination][] of the orbit of the station is in
fact 51.6°.

Since it’s hard to see the overlapped colors in the above image here is
a collection maps with the photos from each mission mapped separately:

[![Multiple Maps][]][Multiple Maps]

This is just some of the data that NASA has to offer. If you’re
interested in getting involved in things like this I suggest taking a
look at [data.nasa.gov][open data] and [International Space Apps
Challenge][Space Apps Challenge].

You can also [download the data I scraped from my github page][latest
project].

 

  [ISS Notify]: http://mechanicalintegrator.com/2011/iss-notify/
  [latest project]: http://natronics.github.com/ISS-photo-locations/
  [Nate Bergey]: https://twitter.com/natronics
  [open data]: http://data.nasa.gov/
  [Space Apps Challenge]: http://spaceappschallenge.org/
  [looking up at the skies]: http://www.flickr.com/photos/natronics/5310760993/
  [giant database of all the photographs astronauts have ever taken in
  space]: http://eol.jsc.nasa.gov/
  [database search page]: http://eol.jsc.nasa.gov/sseop/mrf.htm
  [screen scrape]: http://en.wikipedia.org/wiki/Web_scraping
  [Beautiful Soup]: http://www.crummy.com/software/BeautifulSoup/
  [All ISS]: http://open.nasa.gov/wp-content/uploads/2013/04/all_iss.preview.png
  [All ISS Missions]: http://open.nasa.gov/wp-content/uploads/2013/04/all_iss_missions.preview.png
  [Don Pettit took dozens of amazing time lapse sequences]: http://vimeo.com/61083440
  [All ISS Missions by Map]: http://open.nasa.gov/wp-content/uploads/2013/04/all_iss_missions_map.preview.png
  [inclination]: http://en.wikipedia.org/wiki/Orbital_inclination
  [Multiple Maps]: http://open.nasa.gov/wp-content/uploads/2013/04/small_mult.preview.png
