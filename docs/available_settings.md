There are few settings which can be used to configure wagtail-marketing-addons to suit your needs. By default this package makes a few assumptions on what the "best" text lengths are in order for pages to be properly crawled by search engines (Google, Bing). But every search engine has its own rationale and viewport states for displaying.

---

### Mimimum length of characters in the title

```python
WAGTAIL_MARKETING_MIN_TITLE_LENGTH = 20
```

**Default:** 20

This value determines the minimum length of a title in order to be considered optimal for SEO.

---

### Maximum length of characters in the title

```python
WAGTAIL_MARKETING_MAX_TITLE_LENGTH = 60
```

**Default:** 60

This value determines the maximum length of a title in order to be considered optimal for SEO. 
Also this value is responsible for the truncating indication within search engines.

---

### Minimum amount of words in the title

```python
WAGTAIL_MARKETING_MIN_TITLE_WORD_COUNT = 4
```

**Default:** 4

This value determines the minimum amount of words in a title in order to be considered optimal for SEO.

---

### Maximum amount of words in the title

```python
WAGTAIL_MARKETING_MAX_TITLE_WORD_COUNT = 7
```

**Default:** 7

This value determines the maximum amount of words in a title in order to be considered optimal for SEO.

---

### Minimum description length

```python
WAGTAIL_MARKETING_MIN_DESCRIPTION_LENGTH = 70
```

**Default:** 70

This value determines the minimum length of the search description in order to be considered optimal for SEO.

---

### Maximum description length

```python
WAGTAIL_MARKETING_MAX_DESCRIPTION_LENGTH = 150
```

**Default:** 150

This value determines the maximum length of the search description in order to be considered optimal for SEO.
Also this value is responsible for the truncating indication within search engines.

---

### Fields for list_filter usage

```python
WAGTAIL_MARKETING_LIST_FILTER = ('language',)
```

**Default:** ()

---

## Advanced settings

### Page model reference

```python
WAGTAIL_MARKETING_PAGE_MODEL = 'wagtailcore.Page'
```

**Default:** wagtailcore.Page

When using an add-on like wagtailtrans or extending the wagtail page model to your own needs, it might be relevant to have the option to pass a custom page model reference. For example the following can be configured for wagtailtrans:

```python
WAGTAIL_MARKETING_PAGE_MODEL = 'wagtailtrans.TranslatablePage'
```
