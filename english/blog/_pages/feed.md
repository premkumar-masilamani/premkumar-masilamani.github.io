---
layout: empty
lang: english
type: blog
date: 2025-06-01
category: english-blog
permalink: /english/blog/feed.xml
---

<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
	<channel>
		<title>{{ site.english.blog.title }}</title>
		<link>{{ site.english.blog.url }}</link>
		<description>{{ site.english.blog.tagline }}</description>
		<copyright>{{site.copyright}}</copyright>
		<category>Blogs</category>
		<language>en-US</language>
		<pubDate>{{ site.time | date_to_rfc822  }}</pubDate>
		<lastBuildDate>{{ site.time | date_to_rfc822  }}</lastBuildDate>
		<atom:link href="{{ site.english.blog.url }}/feed.xml" rel="self" type="application/rss+xml" />
		<docs>https://www.rssboard.org/rss-specification</docs>
		<generator>Jekyll Liquid Template in Github</generator>
		<managingEditor>{{ site.email }} ({{ site.english.blog.author }})</managingEditor>
		<webMaster>{{ site.email }} ({{ site.english.blog.author }})</webMaster>
		{% for post in site.categories.english-blog limit:10 %}
			<item>
				<title>{{ post.title | xml_escape }}</title>
				<link>{{ site.home }}{{ post.url }}</link>
				<description>{{ post.content | xml_escape }}</description>
			{% if post.author-name != null %}
				<author>{{ post.author-email }} ({{ post.author-name }})</author>
			{% else %}
				<author>{{ site.email }} ({{ site.english.blog.author }})</author>
			{% endif %}
				<category>{{ post.category }}</category>
				<pubDate>{{ post.date | date_to_rfc822  }}</pubDate>
				<guid isPermaLink="true">{{ site.home }}{{ post.url }}</guid>
			</item>
		{% endfor %}
	</channel>
</rss>
