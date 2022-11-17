# Pickled-Vegetables

When you think about pickles in the real world, a jar full of small cucumbers or some other vegetable immersed in a vinegary brine probably comes to mind. And if you take a moment to ponder pickles a bit further, a few additional thoughts may come to mind — for one, pickles are delicious. But two, the process of pickling is all about preserving and extending the shelf life of a food for later use.

The Pickle in Python is more or less the same idea; preserving Python objects for later use.

Pickle allows you to preserve your model that you’ve just trained, fit and tested to predict on new data at a later time. This is particularly useful if your model took hours to train — instead of having to train it again, you can just preserve (pickle) it and then unload it later for immediate use! But, how exactly does it work, and why?

In technical terms, the Python pickle is a Python module used to serialize (and deserialize) an object structure into (and from) a byte stream. Essentially, serializing an object means transforming it into a format that can be stored, and then deserializing it later, recreating the original object from the serialized format. The character (byte) stream contains all the information necessary to reconstruct the object in another Python script.

# Main
This program keeps vegetable names and prices in a dictionary as key-value pairs. 
The program can display a menu that lets the user see a list of all vegetables and their prices, add a new vegetable and price, change the price of an existing vegetable, and delete an existing vegetable and price. The program pickles the dictionary and saves it to a file when the user exits the program. Each time the program starts, it retrieves the dictionary from the file and unpickles it.

Thiks is a menu driven program that uses the process of pickling in order to create or open a file to "pickle vegetables", the user is allowed to choose if they want to view the vegetables, which are then unpickled and printed into the console, add, change, or delete a vegatable. These options require vegetable pickling where they are dumped into a .txt file and the file is closed. 
