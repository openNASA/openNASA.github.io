Space Mission Design for Everyone
#################################
:date: 2011-07-28 18:15
:author: nskytlan
:category: OpenGov
:tags: engineering, gmat, Open Source, space
:slug: space-mission-design-for-everyone

NASA has a long history releasing code open source in support of its
exploration mission.  You may have heard about some successful NASA open
source project before, like `NASA WorldWind`_ which has over 20 million
downloads since 2005.  One of the exciting projects currently being
undertaken at NASA is an open source space mission design and analysis
tool called GMAT - The General Mission Analysis Tool.  `Joel Parker`_
from NASA’s Goddard Space Flight Center presented on the latest
developments of the project today at the `OSCON conference in Portland,
Oregon`_.  In case you missed it, we summarized his presentation and all
the exciting developments for you here.

The GMAT software has been a collaborative development since 2005. NASA,
other space agencies, academia, private industry, Thinking Systems Inc,
Air Force Research Lab and others actively contribute to its
development. GMAT is released under the NASA Open Source Agreement
(NOSA) and hosted on sourceforge meaning you can download it today and
start designing your own space missions!  The team actually ships the
software with 40 example mission scripts including geostationary,
LCROSS, Mars transfer, Lunar transfer, Libration points.  You can find
even more on their project wiki http://gmat.ed-pages.com/wiki

.. raw:: html

   <div>

I provided some more detailed information below as well as the
presentation from Joel’s talk today, if you are interested.  What is
most exciting to me is that the product has the potential to
fundamentaly shift the business model behind NASA mission planning.
 NASA currently spends a lot of funding on proprietary closed mission
trajectory planning software.  Last year the Navigation and Mission
Design Branch spent $800k on software licenses alone!  This is software
that NASA can't examine, modify, or learn from.  Therefore, this
development of an Open Source solution is a very valuable initiative and
serves as a great example of the value of Open Government at NASA!

.. raw:: html

   </div>

| **What NASA missions has the GMAT software supported?**
|  The system has been used in support of the `Lunar Crater Observation
and Sensing Satellite (LCROSS)`_, `ARTEMIS (Acceleration, Reconnection,
Turbulence and Electrodynamics of the Moon’s Interaction with the
Sun)`_, `Lunar Reconnaissance Orbiter (LRO)`_ and the `Magnetospheric
Multiscale (MMS) Mission`_.

| **How often does the team release a new version of GMAT?**
|  On average, the team is releasing a new version of the software every
six months. The development team does internal builds and testing
nightly.

| **What are the features of the GMAT software?**
|  GMAT’s state of the art features include high fidelity orbit
propagation, impulsive and finite maneuver models,  parameter
optimization solvers, boundary solvers, MATLAB integration,  command
line and GUI interfaces, 2-D and 3D graphics, custom scripting and
plug-ins, among many others and it provides these features in a
transparent and verifiable way through release of source code.

Major features include:

-  Cross-platform desktop application (Windows, Mac, Linux)
-  Extensive force models, differential corrector, optimizer
-  Graphics: 3D OpenGL, 2D plotting, 2D mapping
-  Custom mission scripting language
-  Extensible via plugins, native functions, MATLAB functions
-  Automation via C, TCP/IP
-  Written in C++ with wxWidgets

| **I’m interested in contributing to the project, how can you help?**
|  The GMAT team is developing this tool to be used for NASA’s mission
and is looking for help on developing the software:

For experts...

-  Look through our algorithms, math spec, design documents
-  Help build our mission library

If you know code...

-  Help improve code quality
-  Submit, verify, and quash bugs

.. raw:: html

   <div>

If you care about what we're doing and just want to help...

.. raw:: html

   </div>

-  Hang out on the wiki and forum
-  Help improve our documentation
-  Publicize!

Visit http://gmat.ed-pages.com/wiki/HowCanIHelp

| **Where can I download this software?**
|  GMAT is offered free of charge to use, modify, and share as described
under the terms of the NASA Open Source Agreement v1.3.  GMAT runs on
Windows, Mac, and Linux.  While GMAT has undergone extensive testing and
is mature software, the team considers the software to be in Beta form
(alpha on Mac and Linux). GMAT is part of an open source ecosystem at
Goddard Space Flight Center that includes both research-level and
operational-level software.

-  Download the app: http://sf.net/projects/gmat
-  Look at the docs: http://gmat.sf.net/docs
-  Check out the wiki: http://gmat.ed-pages.com/wiki
-  Follow the blog: http://gmat.sf.net/blog
-  Help find bugs: \ http://pows003.gsfc.nasa.gov/bugzilla/

Discuss with others: http://gmat.ed-pages.com/forum

| **What are the plans for future development of GMAT?**
|  Because GMAT is collaboratively developed and is in constant
development to enable the planning of new mission concepts, there are a
number of new and exciting capabilities being planned.   Ongoing
development includes:

-  Event detection
-  Ground track plot
-  Orbit Wizard
-  Force models (Mars atmosphere, general relativity, Earth tides)
-  User experience: GUI improvements, interface options

| What are the other trajectory planning tools that NASA uses?
|  NASA uses a suite of tools for trajectory planning including:

-  STK
-  FreeFlyer
-  MATLAB
-  Copernicus, Pyxis, MALTO, SPICE, CHEBYTOP, VARITOP, OTIS, Mystic,
   SBC, LTOC, MAnE, ...
-  Lots of self-written tools in Perl, Python, C/C++, VB, Java...

| **What are some other Open Source projects at NASA?  **
|  We encourage you to check out `opensource.gsfc.nasa.gov`_ which
currently has 46 registered projects and `opensource.arc.nasa.gov`_ has
23 registered projects.

.. _NASA WorldWind: http://worldwind.arc.nasa.gov/
.. _Joel Parker: http://www.slideshare.net/jjkparker
.. _OSCON conference in Portland, Oregon: http://www.oscon.com/
.. _Lunar Crater Observation and Sensing Satellite (LCROSS): http://lcross.arc.nasa.gov/
.. _ARTEMIS (Acceleration, Reconnection, Turbulence and Electrodynamics of the Moon’s Interaction with the Sun): http://www.nasa.gov/mission_pages/artemis/
.. _Lunar Reconnaissance Orbiter (LRO): http://lunar.gsfc.nasa.gov/
.. _Magnetospheric Multiscale (MMS) Mission: http://mms.gsfc.nasa.gov/
.. _opensource.gsfc.nasa.gov: http://opensource.gsfc.nasa.gov
.. _opensource.arc.nasa.gov: http://opensource.arc.nasa.gov
