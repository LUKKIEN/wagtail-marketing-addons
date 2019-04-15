# About wagtail-marketing-addons

An (opinionated) overview of all pages and their corresponding promotion settings.

## Use-case

When dealing with large amounts of pages the content editor experience differs from a marketeer's editor experience. A marketeer would more likely want to see what page options were set for SEO and SEA purposes. In this case it can be quite a burden to go through the page explorer, verifying whether the page title, SEO title and search description were set properly.

## Solution

The SEO Listing within the `wagtail-marketing-addons` will show: 

* An overview of all pages in a single list;
* Relevant properties: page title, SEO title, search description;
* A preview what it could look like in a search engine;
* A basic score indicating how this would perform in terms of word and character count.

![wagtail-marketing-addons screenshot](https://raw.githubusercontent.com/LUKKIEN/wagtail-marketing-addons/master/.github/overview.jpg)

## Things to consider

As stated this plugin contains an opinionated perspective on how you would handle your HTML rendering. With this use-case and solution we're assuming the following rationale on your page:

```html
<title>{% if self.seo_title %}{{ self.seo_title }}{% else %}{{ self.title }}{% endif %} | Your Site</title>
<meta name="description" content="{% if self.search_description %}{{ self.search_description }}{% endif %}">
```

In this case your SEO title (when filled in) has a greater priority over the Page Title.

## Documentation

For more information on getting started, an overview of all available settings and the rationale behind the scoring mechanism please see [our documentation on Read the Docs](https://wagtail-marketing-addons.readthedocs.io).

---

[![Build Status](https://travis-ci.org/LUKKIEN/wagtail-marketing-addons.svg?branch=master)](https://travis-ci.org/LUKKIEN/wagtail-marketing-addons)
[![Documentation Status](https://readthedocs.org/projects/wagtail-marketing-addons/badge/?version=latest)](https://wagtail-marketing-addons.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/wagtail-marketing-addons.svg)](https://badge.fury.io/py/wagtail-marketing-addons)
![GitHub](https://img.shields.io/github/license/lukkien/wagtail-marketing-addons.svg)
