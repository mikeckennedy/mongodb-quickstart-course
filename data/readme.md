# Restore this database

If you want to use the exact, final data from the videos, you can restore this database into MongoDB.

1. Make sure MongoDB is running (steps here: [Windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/), [macOS](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/), [Linux](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/))
2. Run this command: `mongorestore --drop --db snake_bnb ./snake_bnb/` in the same folder 
as you unzipped the data files (containing the snake_bnb folder).

You'll need mongorestore in your path for this to work. Otherwise use the full path.
