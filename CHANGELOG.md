# 0.9 (28-04-2024)

- Dropped official support for Wagtail 5 and lower
- Officially supports up to Wagtail 6.3

# 0.8 (07-03-2024)

- Dropped official support for Wagtail 4 and lower
- Officially supports up to Wagtail 5.2
- Added a permission helper to remove the add button on the seo listing page

# 0.7 (22-09-2022)

- Dropped official support for Python 3.6. While this Python version is still supported up to Wagtail 2.15,
  it is no longer maintained. There are no known issues with Python 3.6.
- Officially supports up to Wagtail 4.0

# 0.6 (03-12-2020)

- Dropped official support for Wagtail versions lower than 2.11, earlier versions are no longer supported. 
  However there are no particular breaking changes if you are still using an older version of Wagtail
- Removed the redirect import feature as its part of Wagtail since version 2.10
- Use Wagtail core icons as there is no required dependency for wagtailfontawesome (JanMalte)

# 0.5 (15-05-2020)

- Replaces ugettext_lazy with gettext_lazy as introduced in Django 2.0.
- Officially supports Wagtail 2.7 and up, earlier versions are no longer supported.

# 0.4.1 (05-12-2019)

- Bugfix: Double old-path record will cause the import to throw a 500

# 0.4 (27-11-2019)

- Bulk redirect imports can be assigned to all sites or a specific site. (BramManuel)

# 0.3 (04-10-2019)

- Add `WAGTAIL_MARKETING_SEO_SCORE_ICONS` for overriding the current icon set.

# 0.2 (12-08-2019)

- Add the bulk redirect import on top of wagtail.contrib.redirects

# 0.1 (15-04-2019)

- No breaking changes, updated classifiers for a proper stable release


# 0.0.1 (01-04-2019)

- Initial release of wagtail-marketing-addons
