What is NASA doing with Big Data today?
#######################################
:date: 2012-10-04 17:00
:author: nskytlan
:category: OpenGov
:tags: big data, Open Data, open government, Open Innovation, Open Source, TopCoder
:slug: what-is-nasa-doing-with-big-data-today

In the time it took you to read this sentence, NASA gathered
*approximately* 1.73 gigabytes of data from our nearly 100 currently
active missions! We do this every hour, every day, every year - and the
collection rate is growing exponentially. Handling, storing, and
managing this data is a massive challenge. Our data is one of our most
valuable assets, and its strategic importance in our research and
science is huge. We are committed to making our data as accessible as
possible, both for the benefit of our work and for the betterment of
humankind through the innovation and creativity of the over seven
billion other people on this planet who don’t work at NASA.

In version 2.0 of our `Open Government Plan`_, we scratched the surface
in terms of the work that the Agency is involved in around "`big
data`_\ ” but there is much more to explore.

Recently, I had the opportunity to participate in a panel hosted by `CBS
TechLines`_ called "*Big Data Debunked -- Finding the Data Signals.*\ "
I was joined by `Michael Cavaretta`_ of Ford, `Katrina Montinola`_ of
Archimedes, `Christine Twiford`_ of T-Mobile, `James Kobielus`_ of IBM
and ZDNet editor-in-chief `Larry Dignan`_. We discussed the challenges
and opportunities big data poses for organizations today. I was humbled
by their vision and so inspired by the examples that they shared, that I
wanted to share more about what NASA is doing.

**What is Big Data?**

The whole idea of big data is still relatively new and most discussions
or presentations around the subject start off with a definition of what
big data really is. Definitions are certainly helpful, especially when
the topic is still relatively new, and so we'll start there oursevles.
Big data is very simply a collection of data sets so large and complex
that your legacy IT systems can not handle them. When organizations get
to the point where their `volume, velocity, variety`_ and veracity of
data exceed storage or computing capacity, there are some big challenges
that need to be addressed. You know you have a big data challenge when
your traditional data management systems and analysis tools are
overwhelmed and it becomes difficult to process your data using the
analytic or visualization tools you currently have. Approaching the big
data challenge often necessitates advanced algorithms, infrastructure
and frameworks - and it can all seem very daunting for those just
starting out - but the reality for information-age-based organizations
is that our success is throttled by our our ability to rapidly and
comprehensively navigate the big data universe.

But of course, big data is relative.  In the end, big data by itself has
no value - it's meaningless. It's what you do with the data that matters
most. Today's big data discussion is often centered around how to target
advertisements or customize a user experience, which makes sense given
that the growth in the market place is so closely tied to fact that how
we interact with the physical world is more and more dependent on the
pervasive use of mobile devices that are connect to the work through
sensors. Having the ability to leverage our rich history of data and
combine it with new data we are receiving is a huge asset in making our
missions successful.

If you are still trying to wrap your head around the difference between
petabytes, exabytes, zetabytes, and yottabytes, check out this
overview \ `presentation`_ titled *"What is Big Data and why does it
matter"* by `Tom Soderstrom`_, the Chief Technology Officer for IT at
NASA JPL.

**NASA's Big Data Challenge**

NASA's big data challenge is not just a terrestrial one and it goes
beyond the stereotypical challenge. Many of our “big data” sets are
described by significant metadata, but on a scale that challenges
current and future data management practice. We regularly engage in
missions where data is continually streaming from spacecraft on Earth
and in space, faster than we can store, manage, and interpret it. NASA
has two very different types of spacecraft. We have deep space
spacecraft that sends back data in the order of MB/s. Then we have earth
orbiters that can send back data in GB/s per second. In our current
missions, data is transferred with radio frequency, which is relatively
slow. In the future, NASA will employ technology such as optical (laser)
communication to increase the download and mean a 1000x increase in the
volume of data. This is much more then we can handle today and this is
what we are starting to prepare for now. We are planning missions today
that will easily stream more then 24TB's a day.  That’s roughly 2.4
times the entire Library of Congress - EVERY DAY. For one mission.

It's still very expensive to transfer just one bit down from a
spacecraft so we want to make sure we collect what is most important.
Once the data makes its way to our data centers, storing, managing,
visualizing and analyzing it becomes an issue. To give you an idea of
what we are dealing with, the size of the Climate Change data
repositories alone are projected to grow to nearly 350 Petabytes by
2030.  5 PB's is equivalent to the total number of letters delivered by
the US Postal Service in one year!

One great example of the unique challenge that we face with managing
space data is just starting to be demonstrated by the `Australian Square
Kilometer Array Pathfinder (ASKAP)`_ project which is a large array made
up of 36 antennas, each 12 meters in diameter, spread out over 4,000
square meters but working together as a single instrument to unlock the
mysteries of our universe. The array, which will officially be turned on
and open for business tomorrow Friday, October 5, 2012, is able to
survey the whole sky very quickly and offers an ability to perform
research that could never have been done before.   Check out this great
`time lapse video`_ showing off the new telescopes capabilities!  The
array is a precursor for the larger `Square Kilometre Array`_ telescope
that will open in 2016 and will combine the signals received from
thousands of small antennas spread over a distance of more than 3000 km.
When operational, as much as `700TB/second of data`_ will flow from the
Square Kilometre Array! This is a big data challenge.

And of course, spacecraft are not the only source of our data, thanks to
an ever-growing supply of mobile devices, low-cost sensors, and online
platforms. As an article in `Harvard Business Review`_ this month put
it, "*each of us is now a walking data generator*." The scale of the big
data challenge for NASA, like many organizations, is daunting.

As you can probably imagine, the increasing data volumes are not our
only challenges. As our wealth of data increases, the challenge of
indexing, searching, transferring, and so on all increase exponentially
as well. Additionally, the increasing complexity of instruments and
algorithms, increasing rate of technology refresh, and the decreasing
budget environment, all play a significant factor in our approach.
Fortunately, the entire federal government has turned their attention
towards the growing challenge. In March 2012, the Obama administration
announced the `Big Data Research and Development Initiative`_ to
“\ *greatly improve the tools and techniques needed to access, organize,
and glean discoveries from huge volumes of digital data*." The goal is
to transform government's ability to use big data for scientific
discovery, environmental and biomedical research, education, and
national security.

**Current Approaches**

Developing new approaches to understanding, analyzing, and visualizing
the data we have en masse is of vital interest to NASA. Within
government, there is a push to get ahead of big data from both the top
down and bottom up. We outlined many of the big data activities and
approaches from the perspective of the Mission Directorates (`Science`_,
`Human Space Exploration and Operations`_, `Aeronautics`_, and
`Technology`_) in Version 2.0 of the `NASA Open Government Plan`_. Below
are six world-class examples of how we manage, store, archive, analyze,
visualize, and apply our big data efforts.

    **Managing and Processing**

    NASA’s approach to managing and processing data is demonstrated by
    the `Mission Data Processing and Control System (MPCS)`_ which was
    recently used by the Curiosity rover on Mars. MPCS interfaces with
    NASA's deep-space network, and in turn the Mars Reconnaissance
    Orbiter, to relay data to and from Curiosity and process the raw
    data in real time, a process which previously took hours if not days
    to accomplish. The system produces custom data visualizations that
    are used by the flight operations team.

    **Storage**

    The `NASA Center for Climate Simulation (NCCS)`_, which is primarily
    used by NASA’s Global Modeling and Assimilation Office and the
    Goddard Institute for Space Studies, demonstrates the Agency's
    approach to storing big data. The NCCS focuses on climate and
    weather data and currently houses 32 petabytes of data, with a total
    capacity of 37 petabytes (`source`_). The center also has advanced
    visualization tools, such as it's 17-by-6-foot visualization wall
    which allows for one high-resolution surface on which scientists can
    display still images, video and animated content from data housed in
    the system.

    **Archiving and Distribution**

    Two examples of how NASA approaches processing and archiving are
    demonstrated by the `Atmospheric Science Data Center (ASDC)`_, which
    is focused on Earth science, and the `Planetary Data System (PDS)`_,
    which is focused on planetary science. The Atmospheric Science Data
    Center at NASA Langley Research Center is responsible for
    processing, archiving, and distribution of NASA Earth science data.
    It specializes in atmospheric data important to understanding the
    causes and processes of global climate change and the consequences
    of human activities on the climate and includes petabytes of climate
    data collected over decades. The Planetary Data Systems archives and
    distributes scientific data into one website from NASA planetary
    missions, astronomical observations, and laboratory measurements. It
    offers access to over 100 TB of space images, telemetry, models, and
    anything else associated with planetary missions from the past 30
    years.

    **Analysis**

    NASA's `Pleiades`_ supercomputer is used to help analyze the
    challenging projects, from solar flare and space weather scenarios
    to detailed space vehicle designs. Pleiades was recently used to
    process massive amounts of star data gathered from NASA's Kepler
    spacecraft, leading to the discovery of new Earth-sized planets in
    the Milky Way galaxy. More than 1,200 users across the country rely
    on the system to perform large, complex calculations. It was also
    used to generate the Bolshoi cosmological simulation which explores
    how galaxies and the large-scale structure of the universe has
    formed over billions of years.

    **Visualization**

    The `NASA Earth Exchange (NEX)`_ is a virtual laboratory that
    integrates supercomputer, data system, data visualization, large
    amount of online data, models and algorithms, with social network
    and collaborative technology.  Prior to NEX, scientists were
    required to invest tremendous amounts of time and effort to develop
    high-end computational methods rather than focus on important
    scientific problems. Now, scientists can use the supercomputer to
    visualize large Earth science data sets as well as run and share
    modeling algorithms and collaborate on new or existing projects.
    Recently, a research team from around the U.S. used the NEX
    environment to adjoin an atmospherically correct mosaic of 9,000
    Landsat Thematic Mapper scenes and retrieve global vegetation
    density at a 30- meter resolution. The entire processing of the
    nearly 340 billion pixels in the the composite took just a few hours
    on the Pleiades supercomputer, allowing the team to experiment with
    new algorithms and approaches with ease. We’ve also invested in a
    number of collaboration and knowledge-sharing platform for the Earth
    science community that combine supercomputing, Earth system
    modeling, workflow management and NASA remote sensing data feeds to
    enable a holistic view of our work for researchers. `More
    information on NEX.`_

    **Commercial cloud computing services**

    The recent Mars Science Laboratory mission demonstrates how NASA is
    modernizing its approach to Big Data by utilizing cloud computing
    and commercially available cloud storage solutions. In less than
    four months, NASA engineered and migrated legacy content management
    system and websites to Amazon Web Services. MSL relied heavily on
    mission-critical applications that could sustain failure of over a
    dozen data centers, while delivering over 150 Gigabits per second of
    traffic to a global community of operators, scientists, and general
    public. The team developed a solution that would download raw images
    and telemetry directly from Curiosity and place them into Amazon S3
    storage buckets. As the data streamed in, every image from Mars was
    uploaded, processed, stored, and delivered from the cloud. The data
    was then catalogued in highly available and scalable databases and
    exposed to applications and users via a Restful interface. This
    allowed the content managers for the Mars Web sites to easily create
    informative Web pages with powerful real–time images. This modern
    approach allowed NASA to deliver 120 TB of dynamic content and 30 TB
    of static content the first night, and meet the demands when over 8
    million hits were requested of their websites in less than one
    minute. It also allowed the team to take advantage of the JPL Galaxy
    and JPL Nebula supercomputers which ran close to 200 24-hour Monte
    Carlo simulations at 20 GB each during the mission.

**Real World application of what NASA is doing with Big Data**

The benefits of what NASA is doing in big data are not limited to just
the government! In fact, this work has very real implications for you.
One real world example of how NASA leverages its expertise in big data,
and directly affects your life, is in the field of airline safety. NASA
is involved in analyzing data collected from planes `to study safety
implications`_, which in turn will help with commercial airlines’
maintenance procedure improvements and potentially prevent equipment
failures. Using advanced algorithms, the agency helped tease out
relevant information from a mountain of unstructured data to help
predict and prevent safety problems. Using the open-source Multiple
Kernel Anomaly Detection (MKAD) algorithm, the agency determined how two
continuous data streams or networks are similar, and then analyzed them
using a single framework to detect patterns to automatically discovering
precursors related to adverse events while an airplane is in flight.

**A Big Data Opportunity**

From analyzing the real-time solar plasma ejections and monitoring
global climate change to optimizing large scale engineering designs and
modernizing the way we approach mission operations, NASA is a leader in
the application of big data. At NASA we are continuing to experiment
with new ways to harness this shifting environment and tackle the many
challenges it poses to government and the way we do business. Although
we are just in the beginning stages of in exploring the big data
universe, the opportunities are truly limitless.

The `Open Government Plan <http://open.nasa.gov/plan/>`__ outlines a
number of `specific actions`_ we are taking to drive innovations in
technology around big data. We’ve created `data.nasa.gov`_ as a starting
point to engage with our data, but this is simply a directory of all the
wonderful data NASA makes available. We will also continue to leverage
`data.gov`_ to enable users to locate relevant high quality data and
easy to use tools and applications.

We set a goal to "*create new opportunities for enhanced coordination
across NASA’s Big Data activities, and expanded cooperation with other
agencies*\ " with the intention of encouraging citizens to utilize raw
datasets and create applications relevant to NASA’s mission. Yesterday,
NASA joined the National Science Foundation and the Department of
Energy’s Office of Science to announce the "`Big Data Challenge`_\ ", a
series of competitions which will be hosted on the TopCoder platform.
Competitors will be tasked with imagining mobile apps that find new
value hidden in discrete government information domains and then
describing how they may be shared as universal, cross-agency solutions
that transcend the limitations of individual silos. This is a fresh new
opportunity to work with us and help conceptualize new and novel
approaches that our critical to the future success of government and we
encourage you to check it out.

*Special thanks to `Tom Soderstrom`_ and `Chris Mattmann`_ from
NASA/JPL, `Sean Herron`_ and `Sasi Pillay`_ from the NASA/HQ, and  `Madi
Sengupta`_ from Princeton University, all who contributed research and
insight to this post.*

.. _Open Government Plan: http://open.nasa.gov/plan
.. _big data: http://open.nasa.gov/plan/open-data/
.. _CBS TechLines: http://www.zdnet.com/techlines-big-data-debunked-live-stream-7000005052/
.. _Michael Cavaretta: http://www.zdnet.com/techlines-panelist-profile-fords-michael-cavaretta-on-internal-big-data-7000004000/
.. _Katrina Montinola: http://www.zdnet.com/techlines-panelist-profile-archimedes-katrina-montinola-7000004449/
.. _Christine Twiford: http://www.zdnet.com/techlines-panelist-profile-t-mobiles-christine-twiford-7000004728/
.. _James Kobielus: http://www.zdnet.com/techlines-panelist-profile-ibms-james-kobielus-on-big-data-talent-7000005003/
.. _Larry Dignan: http://www.zdnet.com/meet-the-team/us/larry.dignan/
.. _volume, velocity, variety: http://www.nsf.gov/events/event_summ.jsp?cntn_id=124058&org=CISE
.. _presentation: http://prezi.com/pupffr4ujwqa/what-is-big-data-and-why-does-it-matter-scsim/?auth_key=28ac73cbc9454fc3f1880bc60f328b48351a0000
.. _Tom Soderstrom: http://www.linkedin.com/pub/tom-soderstrom/4/100/a99
.. _Australian Square Kilometer Array Pathfinder (ASKAP): http://www.atnf.csiro.au/projects/mira/
.. _time lapse video: http://www.youtube.com/watch?feature=player_embedded&v=FDoDk4D2RAw#!
.. _Square Kilometre Array: http://www.skatelescope.org/
.. _700TB/second of data: http://www.slideshare.net/Hadoop_Summit/big-data-challenges-at-nasa
.. _Harvard Business Review: http://hbr.org/2012/10/big-data-the-management-revolution/ar/1
.. _Big Data Research and Development Initiative: http://www.whitehouse.gov/sites/default/files/microsites/ostp/big_data_press_release_final_2.pdf
.. _Science: http://science.nasa.gov/
.. _Human Space Exploration and Operations: http://www.nasa.gov/directorates/heo/home/index.html
.. _Aeronautics: http://www.aeronautics.nasa.gov/
.. _Technology: http://www.nasa.gov/offices/oct/home/index.html
.. _NASA Open Government Plan: http://open.nasa.gov/plan
.. _Mission Data Processing and Control System (MPCS): http://www.informationweek.com/government/information-management/nasa-makes-most-of-curiosity-rover-data/240007311
.. _NASA Center for Climate Simulation (NCCS): http://www.nccs.nasa.gov/
.. _source: http://www.csc.com/cscworld/publications/81769/81773-supercomputing_the_climate_nasa_s_big_data_mission
.. _Atmospheric Science Data Center (ASDC): http://eosweb.larc.nasa.gov/
.. _Planetary Data System (PDS): http://pds.nasa.gov/
.. _Pleiades: http://wiki.esipfed.org/images/8/89/Cloud_Computing_Talk_by_Adrian_Gartner.pdf
.. _NASA Earth Exchange (NEX): https://c3.nasa.gov/nex/
.. _More information on NEX.: http://www.nist.gov/itl/ssd/is/upload/NIST-Big-Data-06132012.pdf
.. _to study safety implications: http://www.allanalytics.com/author.asp?section_id=1411&doc_id=250894
.. _specific actions: http://open.nasa.gov/plan/open-data/
.. _data.nasa.gov: http://data.nasa.gov
.. _data.gov: http://www.data.gov
.. _Big Data Challenge: http://open.nasa.gov/blog/2012/10/03/nasa-tournament-labs-big-data-challenge/
.. _Chris Mattmann: http://www.twitter.com/chrismattmann
.. _Sean Herron: http://www.twitter.com/seanherron
.. _Sasi Pillay: http://www.nasa.gov/centers/glenn/about/bios/pillay_bio.html
.. _Madi Sengupta: http://www.twitter.com/msengupta
