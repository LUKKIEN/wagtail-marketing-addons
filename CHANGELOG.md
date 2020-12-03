# 0.6 (XX-XX-XXXX)

- Dropped official support for Wagtail versions lower than 2.11, earlier versions are no longer supported. 
  However there are no particular breaking changes if you are still using an older version of Wagtail
- Removed the redirect import feature as its part of Wagtail since version 2.10

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
