---
layout: common/empty
date: 2025-06-01
category: english
permalink: /english/feed.xml
---

<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
	<channel>
		<title>{{ site.english.title }}</title>
		<link>{{ site.english.url }}</link>
		<description>{{ site.english.tagline }}</description>
		<copyright>{{site.copyright}}</copyright>
		<category>Blogs</category>
		<language>en-US</language>
		<pubDate>{{ site.time | date_to_rfc822  }}</pubDate>
		<lastBuildDate>{{ site.time | date_to_rfc822  }}</lastBuildDate>
		<atom:link href="{{ site.english.url }}/feed.xml" rel="self" type="application/rss+xml" />
		<docs>https://www.rssboard.org/rss-specification</docs>
		<generator>Jekyll Liquid Template in Github</generator>
		<managingEditor>{{ site.english.email }} ({{ site.english.author }})</managingEditor>
		<webMaster>{{ site.english.email }} ({{ site.english.author }})</webMaster>
		{% for post in site.categories.english limit:100 %}
			<item>
				<title>{{ post.title | xml_escape }}</title>
				<link>{{ site.url }}{{ post.url }}</link>
				<description>{{ post.content | xml_escape }}</description>
			{% if post.author-name != null %}
				<author>{{ post.author-email }} ({{ post.author-name }})</author>
			{% else %}
				<author>{{ site.english.email }} ({{ site.english.author }})</author>
			{% endif %}
				<category>{{ post.category }}</category>
				<pubDate>{{ post.date | date_to_rfc822  }}</pubDate>
				<guid isPermaLink="true">{{ site.url }}{{ post.url }}</guid>
			</item>
		{% endfor %}
	</channel>
</rss>
