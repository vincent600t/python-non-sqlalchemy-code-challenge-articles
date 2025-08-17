from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

a1 = Author("Vincent")
a2 = Author("Rosa")

m1 = Magazine("TechWorld", "Technology")
m2 = Magazine("Foodie", "Cooking")

art1 = a1.add_article(m1, "The Future of AI")
art2 = a1.add_article(m1, "Machine Learning Today")
art3 = a2.add_article(m2, "Delicious Pasta Recipes")

print("Author1 Articles:", [a.title for a in a1.articles()])
print("Author1 Magazines:", [m.name for m in a1.magazines()])
print("Magazine1 Articles:", [a.title for a in m1.articles()])
print("Magazine1 Contributors:", [au.name for au in m1.contributors()])
print("Magazine1 Article Titles:", m1.article_titles())
print("Magazine2 Contributing Authors:", [au.name for au in m2.contributing_authors()] if m2.contributing_authors() else None)
