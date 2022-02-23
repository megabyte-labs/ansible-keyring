""" furl is used to parse and manipulate URLs with ease """

from furl import furl


# Create furl object
f = furl("https://github.com/")

# Append path
f /= 'search'

# Add URL params
f.add({"q": "python", "type": "code"})

# Modify URL params
f.set({"q": "ansible"})

# Remove URL params
f.remove(["type"])

# URL encoding is handled automatically
new_query = "python machine learning"
f.set({"q": new_query})

# URL metadata
metadata = [f.scheme, f.host, f.port, f.path, f.query]
