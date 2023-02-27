<h1> ¡Video Sound Dowloader! </h1>

## Explanation

This 🔵 **Python code** 🔵 uses the **pytube** library to download the audio of a YouTube video specified by the given URL.

First, it imports the **YouTube** class from the **pytube** module. 
It then creates an instance of the **YouTube** class by passing the URL of the video as an argument.

Next, it uses the **filter()** method on the **streams** attribute of the **YouTube** instance to filter out only the audio streams. 
It then selects the first audio stream using the **first()** method.

Finally, it specifies the path where the downloaded audio file will be saved using the **output_path** parameter of the **download()** method, 
and calls the **download()** method on the audio stream object to download the audio file to the specified location.

Note that the **output_path** parameter should specify a directory where the downloaded audio file will be saved, not the full file path including the file name.
If you want to specify a file name for the downloaded audio file, you can do so by passing a **filename** parameter to the **download()** method.
