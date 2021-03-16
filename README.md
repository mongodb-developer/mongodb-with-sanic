# MongoDB with Sanic

This is a small sample project demonstrating how to build an API with [MongoDB](https://developer.mongodb.com/) and [Sanic](https://sanic.readthedocs.io/en/stable/).
It was written to accompany a [blog post](https://developer.mongodb.com/quickstart/python-quickstart-sanic/) - you should go read it!

## TL;DR

If you really don't want to read the [blog post](https://developer.mongodb.com/quickstart/python-quickstart-sanic/) and want to get up and running,
activate your Python virtualenv, and then run the following from your terminal (edit the `DB_URL` first!):

```bash
# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
export DB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
python app.py
```

(Check out [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) if you need a MongoDB database.)

Now you can load http://localhost:8000 in your browser ... but there won't be much to see until you've inserted some data.

If you have any questions or suggestions, check out the [MongoDB Community Forums](https://developer.mongodb.com/community/forums/)!