class Magazine:
    all = []   # optional: track all magazines if needed later

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name      # triggers setter validation
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value.strip()) == 0:
            raise Exception("Category must not be empty")
        self._category = value

    def articles(self):
        """Return all articles belonging to this magazine"""
        from lib.article import Article   # delayed import to avoid circular dependency
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Return unique authors who have written for this magazine"""
        return list({article.author for article in self.articles()})

    def article_titles(self):
        """Return list of article titles in this magazine"""
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """Return authors who have written more than 2 articles for this magazine"""
        authors = [article.author for article in self.articles()]
        frequent_authors = [author for author in set(authors) if authors.count(author) > 2]
        return frequent_authors if frequent_authors else None
