Title: NASA's Liquid Galaxy: An Overview
Date: 2011-09-26 12:02
Author: sengelha
Category: OpenGov
Tags: clusterGL, DOUG, gmat, google, Google Earth, HyperWall, Immersive Cave, Liquid Galaxy, Open Source, openGL, Ubuntu, World Wind
Slug: nasas-liquid-galaxy-an-overview

[youtube http://www.youtube.com/watch?v=qbin9WUHrDg]

A few months back, Open.Gov Team Lead, Nick Skytland approached me with
an idea to implement [Google's Liquid Galaxy][] project at NASA.  I was
immediately intrigued by the idea, and set forth researching what would
be involved.  Nick and I collaborated with others at Johnson Space
Center (JSC) to come up with a way to implement our own Liquid Galaxy.
 We also collaborated with people from other NASA centers to come up
with ideas to extend the project's functionality, and to apply the same
hardware to other activities.  In the end, we came up with an exciting
eight-display Liquid Galaxy "immersive cave" and a number of ideas to
consider for the future.

Early on, we sought to participate with the JSC Innovation Team, and
were successful in being selected as one of 20 innovation projects they
wanted to see implemented.  This gave us access to other innovators in
the center, to collaborate with, and better utilize available resources.
 Thankfully, we were able to get an early start on hardware acquisition,
which proved to be the most critical scheduling component for almost all
of the 20 innovation projects.  Over the course of six months or so, we
were able to participate in a variety of innovation activities around
JSC, including a Maker Camp, and several innovation project progress
presentations - which gave us great insight into the brilliant minds and
ideas others brought to the 2011 JSC innovation effort.

During our project's implementation, we collaborated with a variety of
people on different aspects of the task.  During the two day [NASA
Forward - Maker Camp][] in August, people from [Space Life Sciences][]
and [Engineering Directorates][] joined in with designing an 80/20-based
rack system to mount the hardware vertically.  This particular solution
gave us a configuration that will work for either a [HyperWall][] or
[Immersive Cave][] configuration of the Liquid Galaxy.  We also worked
with people from [Mission Operations Directorate][] and the new
[Commercial Crew & Cargo Program Office][] (C3PO) to overcome hurdles we
encountered with system configuration and optimization.

To get an idea of what we could do beyond Liquid Galaxy, we talked with
a variety of teams involved in graphical simulation projects at
different NASA centers around the country.  Our first conversation was
with the group responsible for [NASA's World Wind][] project at [Ames
Research Center][] in [Moffett Field, CA][], who we had met earlier this
year at the NASA [Open Source Summit][].  We also talked with the [VR
Lab Team][] at [Johnson Space Center][] in [Houston, TX][], who created
DOUG - a 3D viewing tool used in training for space walks as well as
shuttle and station robotic arm operations.  Finally, we have spent the
most time discussing opportunities with the team responsible for GMAT,
the [General Mission Analysis Tool][], from [Goddard Space Flight
Center][] in [Greenbelt, MD][].

Discussions with these groups looked at two different possibilities for
machine clustered HyperWall and Immersive Cave implementations.  The
first is similar to Google Earth's implementation, where you run the
application on every machine, and have one configured as a controller
that sends data to the rest, and the others receive the controller's
state data (position and attitude) and then draw their locations based
on offset values applied to the camera / screen position.  This requires
the software on every machine, and in the case of Google Earth, each
machine is requesting all of its own data from Google over the network -
in our case, eight times the bandwidth usage.

The second option is an innovative solution recently mentioned on
Google's Liquid Galaxy page, by one of their three GSoC (Google Summer
of Code) Interns: [ClusterGL][].  ClusterGL is basically taking OpenGL,
an open source graphic library alternative to DirectX, and providing its
graphics API calls over the network so that other machines can draw the
graphics themselves, without needing application on their machine.  You
can run one copy of the program on one machine, and setup all the rest
to just draw additional screens of data to make the field of view
larger.  So far this technique shows the most promise, because you don't
need to adapt an application to talk between multiple copies of itself
on the network.

So far our project has been met with great interest and enthusiasm on
site at Johnson Space Center.  People just can't stop playing with the
Liquid Galaxy, flying around the Earth, Moon, and Mars, looking at all
of the graphic visualizations of the world in an Immersive Cave
environment.  If you are ever at JSC, come over to Building 29 and try
it out.  We look forward to working with NASA and external parties
interested in collaborating on clustered graphical simulation solutions
in the future.

By [Stuart Engelhardt][]

  [Google's Liquid Galaxy]: http://code.google.com/p/liquid-galaxy/
    "Google - Liquid Galaxy"
  [NASA Forward - Maker Camp]: http://open.nasa.gov/blog/2011/08/13/nasa-forward-maker-camp-2/
    "NASA Forward - Maker Camp"
  [Space Life Sciences]: http://spacelifesciences.nasa.gov
    "Space Life Sciences Directorate"
  [Engineering Directorates]: http://www.nasa.gov/centers/johnson/engineering/
    "Engineering Directorate"
  [HyperWall]: http://www.nas.nasa.gov/Groups/VisTech/hyperwall/
  [Immersive Cave]: http://en.wikipedia.org/wiki/Cave_Automatic_Virtual_Environment
    "Immersive Cave Technology"
  [Mission Operations Directorate]: http://www.nasa.gov/centers/johnson/about/people/orgs/
    "JSC People"
  [Commercial Crew & Cargo Program Office]: http://www.nasa.gov/offices/c3po/home/
    "Commercial Crew and Cargo Program Office"
  [NASA's World Wind]: http://worldwind.arc.nasa.gov/java/
    "NASA WorldWind"
  [Ames Research Center]: http://www.nasa.gov/centers/ames/home/
    "Ames Research Center - ARC"
  [Moffett Field, CA]: http://maps.google.com/maps?q=NASA+Ames+Research+Center,+Moffett+Field,+CA+94035&hl=en&sll=37.409846,-122.063427&sspn=0.156805,0.139217&vpsrc=0&t=h&z=15
    "Google Map of NASA ARC"
  [Open Source Summit]: http://www.nasa.gov/open/source/
    "Open Source Summit (OSS)"
  [VR Lab Team]: http://vrlab.jsc.nasa.gov "Virtual Reality Lab"
  [Johnson Space Center]: http://www.nasa.gov/centers/johnson/home/
    "Johnson Space Center"
  [Houston, TX]: http://maps.google.com/maps?q=johnson+space+center&hl=en&ll=29.561662,-95.093708&spn=0.042032,0.034804&sll=37.415228,-122.06265&sspn=0.039198,0.034804&vpsrc=0&t=h&z=15
    "Google Map of JSC"
  [General Mission Analysis Tool]: http://gmat.gsfc.nasa.gov/ "GMAT"
  [Goddard Space Flight Center]: http://www.nasa.gov/centers/goddard/home/
    "GSFC"
  [Greenbelt, MD]: http://maps.google.com/maps?q=Goddard+Space+Flight+Center,+Goddard,+Maryland&hl=en&ll=38.997308,-76.850824&spn=0.038356,0.034804&sll=38.997308,-76.85149&sspn=0.018778,0.017402&vpsrc=6&t=h&z=15
    "Google Map of GSFC"
  [ClusterGL]: http://code.google.com/p/liquid-galaxy/wiki/GSoC2011_ClusterGL
    "ClusterGL on GSoC 2011"
  [Stuart Engelhardt]: https://plus.google.com/109745357980497670136?rel=author
    "Stuart Engelhardt on Google+"
