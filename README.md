# wagtail-marketing-addons

An (opiniated) overview of all pages and there corresponding promotion settings.

## Use-case

When dealing with large amounts of pages the content editor experience differs from a marketeers editor experience. A marketeer would more likely to see what page options were set for SEO and SEA purposes. In this case it can be quite a burden to go through page explorer and verifying whether the page title, seo title and search description were set properly.

## Solution

The SEO Listing within the `wagtail-marketing-addons` will show: 

* An overview of all pages in a single list;
* Show relevant properties: page title, SEO title, search description;
* Show a preview what it could look like in a search engine;
* Add a basic score indication in how this would perform in terms of word and character count.

![Wagtail screenshot](https://cdn.rawgit.com/lukkien/wagtail-marketing-addons/master/.github/overview.jpg)

## Things to consider

As stated this plugin contains an opinionated perspective on how you would handle your HTML rendering.
With this use-case and solution we're assuming the following rationale on your page:

```
    <title>{% if self.seo_title %}{{ self.seo_title }}{% else %}{{ self.title }}{% endif %} | Your Site</title>
    <meta name="description" content="{% if self.search_description %}{{ self.search_description }}{% endif %}">
```

In this case your SEO title (when filled in) has a greater priority over the Page Title.
