---
layout: empty
lang: tamil
type: podcast
date: 2025-06-30
category: tamil-podcast
permalink: /tamil/podcast/feed.xml
---

<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0" xmlns:anchor="https://anchor.fm/xmlns" xmlns:podcast="https://podcastindex.org/namespace/1.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:psc="http://podlove.org/simple-chapters">
  <channel>
    <title>{{ site[include.lang][include.type].title }}</title>
    <link>TODO - {{ site[include.lang][include.type].url }}</link>
    <description>TODO - {{ site[include.lang][include.type].description }}</description>
    <copyright>TODO - {{ site[include.lang][include.type].author }}</copyright>
    <language>ta</language>
    <category>Podcasts</category>
    <pubDate>{{ site.time | date_to_rfc822 }}</pubDate>
    <lastBuildDate>{{ site.time | date_to_rfc822 }}</lastBuildDate>
    <docs>https://www.rssboard.org/rss-specification</docs>
    <generator>Jekyll Liquid Template in GitHub</generator>
    <atom:link href="{{ site[include.lang][include.type].url }}/feed.xml" rel="self" type="application/rss+xml" />
    <atom:link rel="hub" href="https://pubsubhubbub.appspot.com/"/>
    <author>TODO - {{ site[include.lang][include.type].author }}</author>
    <managingEditor>{{ site[include.lang].email }} ({{ site[include.lang][include.type].author }})</managingEditor>
    <webMaster>{{ site[include.lang].email }} ({{ site[include.lang][include.type].author }})</webMaster>
    <itunes:author>{{ site[include.lang][include.type].author }}</itunes:author>
    <itunes:summary>{{ site[include.lang][include.type].description }}</itunes:summary>
    <itunes:owner>
      <itunes:name>{{ site[include.lang][include.type].author }}</itunes:name>
      <itunes:email>{{ site[include.lang].email }}</itunes:email>
    </itunes:owner>
    <itunes:explicit>false</itunes:explicit>
    <itunes:image href="{{ site[include.lang][include.type].image }}" />
    <itunes:category text="Society &amp; Culture">
      <itunes:category text="Personal Journals" />
    </itunes:category>
    <itunes:type>episodic</itunes:type>

    {% assign filtered_posts = site.posts | where: "lang", "tamil" | where: "type", "podcast" %}
    {% assign sorted_posts = filtered_posts | sort: "date" | reverse %}

    {% for post in sorted_posts %}
      <item>
        <title>{{ post.title | xml_escape }}</title>
        <link>{{ site.home }}{{ post.url }}</link>
        <description>{{ post.content | xml_escape }}</description>
        <dc:creator>Premkumar Masilamani</dc:creator>
        <itunes:summary>{{ post.excerpt | xml_escape }}</itunes:summary>
        <itunes:explicit>false</itunes:explicit>
        {% if post.image %}
          <itunes:image href="{{ post.image }}" />
        {% endif %}
        {% if post.duration %}
          <itunes:duration>{{ post.duration }}</itunes:duration>
        {% endif %}
        {% if post.season %}
          <itunes:season>{{ post.season }}</itunes:season>
        {% endif %}
        {% if post.episode %}
          <itunes:episode>{{ post.episode }}</itunes:episode>
        {% endif %}
        <itunes:episodeType>full</itunes:episodeType>
        <guid isPermaLink="true">{{ site.home }}{{ post.url }}</guid>
        <pubDate>{{ post.date | date_to_rfc822 }}</pubDate>
        <enclosure url="{{ post.audio_url }}" type="audio/mpeg" />
      </item>
    {% endfor %}
  </channel>
</rss>
