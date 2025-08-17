class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        if len(name.strip()) == 0:
            raise Exception("Author name must have length > 0")

        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise Exception("Author name cannot be changed")

    def articles(self):
        from lib.article import Article   # delayed import to break circular dependency
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        from lib.article import Article   # import here to avoid circular import
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = [article.magazine.category for article in self.articles()]
        return list(set(topics)) if topics else None
