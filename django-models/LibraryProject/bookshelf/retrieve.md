
---

### **5b: Retrieve the Book**

```python
# Retrieve
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
