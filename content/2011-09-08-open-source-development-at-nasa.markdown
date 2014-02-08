---
author: weshagh
comments: false
date: 2011-09-08 23:52:22+00:00
layout: post
slug: open-source-development-at-nasa
Title: Open Source Development at NASA
wordpress_id: 4576
categories:
- OpenGov
tags:
- code
- Gov 2.0
- Inspiration
- Nebula
- Open Source
- Participation
---

_This post complements a presentation given at the [2011 NASA IT Summit](http://www.nasa.gov/offices/ocio/itsummit/) entitled_ [A Case for Bi-lateral Open Source Development: The Nebula Story and Key Findings from the Open Source Summit](http://open.nasa.gov/william/open-source-presentation).  _Although written by an attorney, this post is not legal advice or analysis and should not be taken as such._




NASA has a special association with the principles of openness and transparency characteristic of the open source software movement.  Signed into law on July 29, 1958 by President Eisenhower, the [National Aeronautics and Space Act](http://www.nasa.gov/offices/ogc/about/space_act1.html) created NASA and charged it with, among other things, providing for the widest practicable and appropriate dissemination of information concerning its activities and the results thereof.  Manifestations of this duty can be observed across all of the Agency’s mission and business functions, from [high resolution photography](http://www.nasa.gov/multimedia/imagegallery/iotd.html) and reports on [planetary discovery](http://kepler.nasa.gov/Mission/discoveries/) to [financial transparency](http://www.nasa.gov/offices/ocfo/budget/fin_rpts.html) and [independent oversight](http://oig.nasa.gov/audits/reports/FY11/index.html).




A particularly direct form of this transparency can be seen in NASA’s efforts to release open source software.  In 2003, NASA published [a report](http://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20030054432_2003061119.pdf) assessing the formal barriers to distributing NASA software as open source and reviewing the state of open source licenses.  Subsequently, NASA developed an [open source license](http://ti.arc.nasa.gov/opensource/nosa/) and changed [relevant policies](http://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C) to permit the release of NASA software under this license.  [Several projects](http://ti.arc.nasa.gov/opensource/projects/) have since taken advantage of this work by releasing their code as open source.




[NASA World Wind](http://worldwind.arc.nasa.gov/java/), a 3D interactive world viewer and winner of the [2009 NASA Software of the Year award](http://www.nasa.gov/offices/oce/icb/winners/soy/2009_soy.html), stands out as a shining example of the potential impact of open source NASA software.  Used by citizens, scientists, and organizations such as the European Space Agency, the Japan Aerospace Exploration Agency, PEMEX (Mexico Petroleum Company), General Dynamics, World Bank, Sun Microsystems, IBM, Northrop Grumman, and the Government of Australia, World Wind has made a significant impact on increasing public access to geologic data.




These efforts have validated the benefits inherent to releasing open source software.  In furtherance of NASA’s open source efforts, we are currently working toward expanding our flexibility to engage in [bazaar-style](http://catb.org/~esr/writings/homesteading/cathedral-bazaar/), bi-lateral open development where code is developed over the Internet in full view of the public from the outset.  This approach holds the promise of increased software quality, reduced development costs, accelerated software development cycles, reduced barriers for public-private collaboration, commercialization of Agency technology, and a higher rate of technology transfer both to and from NASA.




NASA’s first foray into this area was through the [Nebula Cloud Computing project](http://nebula.nasa.gov/).  Nebula started as a software development effort in 2008 to create a private cloud computing platform utilizing free and open source software.  As a corollary of this architectural direction, the team set about releasing its software under free and open source licenses to engage a community in expeditiously advancing the state and capabilities of open cloud computing.  Towards this end, the [Nebula project worked with policy makers and stake holders across the Agency](http://nodis3.gsfc.nasa.gov/NRW_Docs/NRW_2210-35_.pdf) to enable a construct wherein the team would be able to engage in ongoing public development of the Nebula software under the Apache 2.0 license.  In this way, the project was able to work with other interested developers at an early stage, building the software alongside a diverse array of individuals and organizations.  After taking notice of NASA’s work in this area, [Rackspace open sourced their Cloud Files platform](http://www.openstack.org/blog/2010/07/introducing-openstack/).  This act provided the impetus for NASA and Rackspace to join their respective efforts under a common banner: [OpenStack](http://www.openstack.org/).  The ensuing public interest in OpenStack has been staggering, with nearly [1500 individuals](http://www.openstack.org/community/) and [110 organizations](http://www.openstack.org/community/companies/) currently participating in some way to advance the project.




Given Nebula and OpenStack’s success, it became apparent that bazaar-style development held the potential for bringing significant value to NASA projects.  However, the Nebula experience illustrated that NASA’s open source policies favor the [cathedral model](http://catb.org/~esr/writings/homesteading/cathedral-bazaar/) of development where an isolated group of developers work on a project and release infrequent iterations at the conclusion of development cycles. To better understand NASA’s open source posture and to advance open development as a formal option for NASA developers, we held an [Open Source Summit](http://www.nasa.gov/open/source/) in March at [NASA Ames Research Center](http://www.nasa.gov/centers/ames/home/index.html).  This event brought together engineers, policy makers, and members of the open source community to discuss our existing open source policy framework and to chart a course toward bi-lateral open source development.  There were a number of [key recommendations from the summit](http://www.slideshare.net/skytland/nasa-open-source-proceedings), among them:








	
  * Imbue an Open Source-First Culture.  Work to promote open source development and release in NASA software projects through project, budgetary, and organizational incentives.

	
  * Knock Down Barriers to Community. Clarify and reduce barriers to direct NASA participation in open source communities, governing boards, and related structures.  Clarify contributor license agreement requirements to facilitate code contributions to NASA projects.  Further, clearly describe restrictions and regulations which are peculiar to the government, such as the [International Traffic in Arms Regulations](http://www.pmddtc.state.gov/regulations_laws/itar_official.html).

	
  * Communicate. Highly visible communication about NASA’s open source process and projects along with community management and ongoing fora for discussion will increase awareness and help more projects explore open source options.  Activities like the summit, coding contests, hackathons, and similar events will highlight open source opportunities for internal and external parties.

	
  * Deprecate NASA’s License. The [NASA Open Source Software Agreement](http://ti.arc.nasa.gov/opensource/nosa/) was developed in 2003 as a means to enable public release of NASA source code.  This license received Open Source Initiative [approval](http://www.opensource.org/licenses/NASA-1.3), but [has been criticized](http://www.gnu.org/licenses/license-list.html#NASA) for potentially hindering code reuse. In 2006, the Open Source Initiative issued a [report](http://www.opensource.org/proliferation-report) on the problem of license proliferation identifying three consequences:


	
    1. the perception that there are too many licenses,

	
    2. difficulty arising from license incompatibility,

	
    3. and the expense of having to read and understand so many varied licenses.


	
  * Although the report excepts NASA’s license as necessary due to unique government constraints, Summit participants suggested that NASA should deprecate this license and re-license previously released software under a mainstream open source license.  Further, they suggested that NASA should approve a subset of mainstream licenses for NASA use and centralize guidance for license selection for new projects.







In the coming months, the Open Government team along with others throughout the Agency will work toward implementing these and other suggestions to expand the open source options available to NASA developers.  The benefits of bi-lateral open source development are undeniable, and NASA is uniquely positioned to inspire the public to directly participate in building the systems that will enable us to expand human knowledge of the Earth and propel us deeper into the recesses of space.
