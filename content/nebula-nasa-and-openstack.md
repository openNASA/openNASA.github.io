Title: Nebula, NASA, and OpenStack
Date: 2012-06-04 15:35
Author: agllewel
Category: OpenGov
Tags: Ames Research Center, cloud computing, code.nasa.gov, Nebula, Open Source, Open Stack
Slug: nebula-nasa-and-openstack

* This post by Ray O’Brien (Former Nebula Project Manager, NASA Ames
Research Center CIO, Acting) was originally posted to
[nebula.nasa.gov][]. The Nebula Cloud Computing Platform was the
[Flagship Initiative for NASA's first Open Government Plan][], and much
has been learned, accomplished, and created over the course of this
project. Thanks to the team who worked so hard and invested so much in
this groundbreaking effort.*

When we started Nebula in 2008, it was for a somewhat different purpose
than what it eventually became. Under the project name NASA.net, we
initially set out to consolidate NASA’s web space onto a unified
platform. By offering common web development tools and resources as a
centralized service, it was hoped that a convergence effect could be
achieved that would result in heightened efficiency and greater
visibility into a diverse array of Agency activities.

As with so many great startup stories, in building this system and
advocating for its use, it became apparent that flexible infrastructure
was a prerequisite to the platform layer. Still with the aim of tackling
the web problem, the team took a step back and set out to characterize
the state of generic, on-demand, API-driven compute and storage systems.
At this point, two interesting things happened. One, we found the state
of open systems for enabling cloud-like infrastructure service delivery
to be in an early state of development with low overall supported
capacity. Second, we noticed considerable opportunity for providing
infrastructure as a service in the communities we were courting for the
platform layer. With the confluence of these two findings, the team
decided to pivot into the infrastructure layer. We eventually came upon
the name “Nebula” and set about the construction of an open source
compute controller.

Later, on the first open source release of our Nova controller, we found
that Rackspace had taken a strikingly similar technical approach to
their storage systems and were set to begin the construction of a
compute controller just as we were preparing to focus on storage. Given
our technical alignment and with the open source release of Rackspace’s
Swift storage software, we joined forces to create [OpenStack][]. Our
hope was that a community would form around these two pieces of software
toward the construction of an open source cloud operating system. To say
that our greatest hopes in this regard were met would be an
understatement. [OpenStack][1] today has the support of hundreds of
individuals and organizations around the world, all set on realizing the
original vision for the project.

Recently, on May 15, NASA announced a new cloud computing strategy for
the Agency at the Uptime Institute’s symposium in Santa Clara, CA. Among
its facets is a reduction to our OpenStack development efforts in favor
of becoming a “smart consumer” of commercial cloud services. In
understanding this shift, it is important to consider that the majority
of NASA’s code contributions to OpenStack were during its early stages
while its developer and industry communities were still forming. Since
those early days, the [OpenStack][1] community has grown considerably,
and we have borne witness to accelerated development in key areas
directly bearing on NASA’s originally identified needs. In fact, the
vast majority of code contributions over the past year of intense
OpenStack development have come from community members other than NASA.

As the community continues to overtake many of our original internal
development objectives, it is appropriate that NASA ramp down its
involvement with [OpenStack][1] in-line with our announcement at the
Uptime Conference. We celebrate this milestone in OpenStack’s
development: it has reached a point of self-sustaining growth along a
community-driven trajectory such that the project will continue to go
forward without our direct involvement. This outcome has always been one
of our highest goals for Nebula, and now permits us to transition from
the role of developer to that of enthusiastic adopter of a broad range
of cloud services, including those based on OpenStack, delivered by a
larger number of cloud providers and vendors than existed when the
Nebula project was started. NASA has a rich heritage of developing and
transferring technology to the private sector for continued commercial
development, and OpenStack adds one more stunningly successful entry to
that list.

While it is true that our public development activities will no longer
be a driving force in OpenStack, should a special requirement be
identified by a NASA project wishing to use OpenStack in the future, the
possibility of contributing can be explored on a project-by-project
basis. That’s the beauty of the community driven open source development
model and the key reason Nova, NASA’s contribution to OpenStack, was
developed as open source software in the first place.

The announcement should not be interpreted in any way as NASA abandoning
or being dissatisfied with OpenStack and its community. Nothing could be
further from the truth -- NASA is extremely proud of its role in helping
to create the OpenStack community. With that success firmly established
and many in the industry now likening [OpenStack][1] to the “Linux of
the cloud,” we are turning our attention to exploring how available
cloud solutions of all types can best be used to address a broad set of
Agency requirements.

  [nebula.nasa.gov]: http://nebula.nasa.gov/
  [Flagship Initiative for NASA's first Open Government Plan]: http://www.nasa.gov/open/plan/nebula.html
  [OpenStack]: http://openstack.org
  [1]: http://openstack.org/
