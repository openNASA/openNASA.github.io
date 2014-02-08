---
author: sherron
comments: false
date: 2011-07-28 22:23:25+00:00
layout: post
slug: publishing-the-open-source-way
Title: Publishing the Open Source Way
wordpress_id: 4298
categories:
- OpenGov
tags:
- Open Source
- open.NASA
- web development
---

Developing open.nasa.gov was, to say the least, an interesting process. Born out of an effort by [Nick Skytland](http://open.nasa.gov/blog/author/skytland/) over five years ago, we first began drafting some ideas on how the site will look, feel, and function last fall. The preliminary designs we created were the designs we were working with until roughly 48 hours ago (less than two days before the launch of the site). For the most part, the site was very “traditional NASA” - starscape background, bold red and blue colors scheme, and a ton of functionality that wasn’t really necessary but that we thought would be nice to have. While sitting at [OSCON 201](https://twitter.com/#!/search/%23oscon)1, however, we realized something. If we really, really wanted open.NASA to be a new, fresh look on what’s happening at NASA, we needed to so something bold. So, we deleted all of our work and started from scratch. That’s right - this entire site was created in just a few (crazy, late-night) hours. Doing all this work in such a short time span, however, wouldn’t have been possible without a little bit of help. I’m talking, of course, about open source.

Open Source is big at NASA. It’s one of the [flagship initiatives](http://www.nasa.gov/open/plan/open-source-development.html) in our [Open Government plan](http://www.nasa.gov/open). Last spring, we hosted our first ever [Open Source Summit](http://www.nasa.gov/open/plan/open-source-development.html). It drew 700+ attendees to discuss the issues and solutions about developing open source applications at the agency. Our most popular open source application, [World Wind](http://worldwind.arc.nasa.gov), has had millions of downloads. open.NASA is no exception - it’s built entirely on open source and Software as a Service technologies, meaning you can take everything you see here today and do it on your own. Here’s how:

Server Platform
**LAMP
**open.NASA is hosted on a [LAMP stack](http://en.wikipedia.org/wiki/LAMP_(software_bundle)) ([Linux](http://en.wikipedia.org/wiki/Linux), [Apache](http://httpd.apache.org/), [MySQL](http://www.mysql.com/), [PHP](http://www.php.net/)). All of these are open source applications that are near-universal. If you’ve built a website before, it’s most likely been on LAMP.

**Wordpress**
The core of open.NASA is [Wordpress 3.2.1](http://www.wordpress.org), an open source content management system approved for use by both NASA and the [General Services Administration](http://www.apps.gov). We made no tweaks to the Wordpress core for the site - it grabbed from the [SVN repository](http://codex.wordpress.org/Installing/Updating_WordPress_with_Subversion) and set up out of the box.

**Theme**
The site is running a modified version of [Landau Reece’](http://www.landaureece.com/)s free [Protean theme](https://github.com/landaureece/Protean/blame/master/archive.php) for Wordpress. We made a few changes to the theme to create a unique look and feel to the site. We really like the design due to how clean and simple it presents the content. Plus, each post allows for customization by the author to give everyone a bit of personality.

**Disqus**
Our comments are driven by [Disqus](http://disqus.com/), a GSA approved commenting system that connects conversations happening across the web.

**UserVoice**
We want to hear from you! We’ve opened a [UserVoice account](http://nasa.uservoice.com) to get your feedback on our site, our projects, and hear your ideas for new ways NASA can be more participatory, collaborative, and transparent with the public. Be sure to also let us know via UserVoice if you see any errors or bugs on the site. None of us are web developers by day, and we definitely want to know if there’s something that need to be fixed.

We sincerely hope you enjoy open.NASA. Feel free to use anything you see on this site - we want you to benefit from the wonders of open source, too! open.NASA is a constantly evolving platform. Our goal is to make this site a way for you to learn how we’re working every day to make NASA more accessible to the world. Your feedback and ideas are critical in helping us do our jobs better. This is your space agency, and we hope you are as excited as we are for the future. Let’s do great things together.
