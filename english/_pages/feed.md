---
layout: common/empty
date: 2023-10-11
category: english
permalink: /english/feed.xml
---

<rss version="2.0" xmlns:atom="https://www.w3.org/2005/Atom">
	<channel>
		<title>{{ site.english.title }}</title>
		<link href="{{ site.english.url | xml_escape }}" rel="alternate" type="text/html"/>
		<description>{{ site.english.tagline }}</description>
		<copyright>{{site.copyright}}</copyright>
		<category>Blogs</category>
		<language>en-us</language>
		<pubDate>{{ site.time | date_to_rfc822  }}</pubDate>
		<lastBuildDate>{{ site.time | date_to_rfc822  }}</lastBuildDate>
		<atom:link href="{{ site.english.url }}/feed.xml" rel="self" type="application/rss+xml" />
		<docs>https://cyber.law.harvard.edu/rss/rss.html</docs>
		<generator>Jekyll Liquid Template in Github</generator>
		<managingEditor>{{ site.english.email }} ({{ site.english.author }})</managingEditor>
		<webMaster>{{ site.english.email }} ({{ site.english.author }})</webMaster>
		{% for post in site.categories.english limit:100 %}
			<item>
				<title>{{ post.title | xml_escape }}</title>
				<link href="{{ site.url | xml_escape }}" rel="alternate" type="text/html"/>
				<description>{{ post.content | xml_escape }}</description>
			{% if post.author-name != null %}
				<author>{{ post.author-email }} ({{ post.author-name }})</author>
			{% else %}
				<author>{{ site.english.email }} ({{ site.english.author }})</author>
			{% endif %}
				<category>{{ post.category }}</category>
				<pubDate>{{ post.date | date_to_rfc822  }}</pubDate>
				<guid>{{ site.url }}{{ post.url }}</guid>
			</item>
		{% endfor %}
	</channel>
</rss>
