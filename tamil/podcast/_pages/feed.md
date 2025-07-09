---
layout: empty
lang: tamil
type: podcast
date: 2025-06-30
category: tamil-podcast
permalink: /tamil/podcast/feed.xml
---

<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
	<channel>
		<title>{{ site.tamil.podcast.title }}</title>
		<link>{{ site.tamil.podcast.url }}</link>
		<description>{{ site.tamil.podcast.tagline }}</description>
		<copyright>{{site.copyright}}</copyright>
		<category>Blogs</category>
		<language>ta-US</language>
		<pubDate>{{ site.time | date_to_rfc822  }}</pubDate>
		<lastBuildDate>{{ site.time | date_to_rfc822  }}</lastBuildDate>
		<atom:link href="{{ site.tamil.podcast.url }}/feed.xml" rel="self" type="application/rss+xml" />
		<docs>https://www.rssboard.org/rss-specification</docs>
		<generator>Jekyll Liquid Template in Github</generator>
		<managingEditor>{{ site.tamil.email }} ({{ site.tamil.podcast.author }})</managingEditor>
		<webMaster>{{ site.tamil.email }} ({{ site.tamil.podcast.author }})</webMaster>
		{% for post in site.categories.tamil-podcast limit:10 %}
			<item>
				<title>{{ post.title | xml_escape }}</title>
				<link>{{ site.home }}{{ post.url }}</link>
				<description>{{ post.content | xml_escape }}</description>
			{% if post.author-name != null %}
				<author>{{ post.author-email }} ({{ post.author-name }})</author>
			{% else %}
				<author>{{ site.tamil.email }} ({{ site.tamil.podcast.author }})</author>
			{% endif %}
				<category>{{ post.category }}</category>
				<pubDate>{{ post.date | date_to_rfc822  }}</pubDate>
				<guid isPermaLink="true">{{ site.home }}{{ post.url }}</guid>
			</item>
		{% endfor %}
	</channel>
</rss>
