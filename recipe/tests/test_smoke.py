# The main tests from the package at starting freezes for an indefinite time, 
# the test is written monolithic and there is no way to skip tests.

import feedparser

def test_parse_simple_rss():
    rss = b"""<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
      <channel>
        <title>Example Feed</title>
        <link>http://example.org/</link>
        <description>Just a test feed</description>
        <item>
          <title>Item 1</title>
          <link>http://example.org/item1</link>
          <description>First item</description>
        </item>
      </channel>
    </rss>
    """
    parsed = feedparser.parse(rss)
    # sanity checks
    assert parsed.feed.title == "Example Feed"
    assert parsed.feed.link == "http://example.org/"
    assert len(parsed.entries) == 1
    assert parsed.entries[0].title == "Item 1"
