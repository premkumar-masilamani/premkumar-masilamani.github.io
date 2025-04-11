---
layout: common/empty
date: 2023-10-11
category: tamil
permalink: /tamil/feed.xml
---

<rss version="2.0" xmlns:atom="https://www.w3.org/2005/Atom">
	<channel>
		<title>{{ site.tamil.title }}</title>
		<link>{{ site.tamil.url }}</link>
		<description>{{ site.tamil.tagline }}</description>
		<copyright>{{site.copyright}}</copyright>
		<category>Blogs</category>
		<language>en-us</language>
		<pubDate>{{ site.time | date_to_rfc822  }}</pubDate>
		<lastBuildDate>{{ site.time | date_to_rfc822  }}</lastBuildDate>
		<atom:link href="{{ site.tamil.url }}/feed.xml" rel="self" type="application/rss+xml" />
		<docs>https://cyber.law.harvard.edu/rss/rss.html</docs>
		<generator>Jekyll Liquid Template in Github</generator>
		<managingEditor>{{ site.tamil.email }} ({{ site.tamil.author }})</managingEditor>
		<webMaster>{{ site.tamil.email }} ({{ site.tamil.author }})</webMaster>
		{% for post in site.categories.tamil limit:1000 %}
			<item>
				<title>{{ post.title | xml_escape }}</title>
				<link>{{ site.url }}{{ post.url }}</link>
				<description>{{ post.content | xml_escape }}</description>
			{% if post.author-name != null %}
				<author>{{ post.author-email }} ({{ post.author-name }})</author>
			{% else %}
				<author>{{ site.tamil.email }} ({{ site.tamil.author }})</author>
			{% endif %}
				<category>{{ post.category }}</category>
				<pubDate>{{ post.date | date_to_rfc822  }}</pubDate>
				<guid>{{ site.url }}{{ post.url }}</guid>
			</item>
		{% endfor %}
	</channel>
</rss>
