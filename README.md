# AIDungeon-Delver

This is a simple set of files for playing a Table Top Role Playing Game (TTRPG) using AI and RAG, Specifically using Chromadb and Google Gemini. It is not overly sophisticated but nothing out there did what I wanted it to do so I am sharing this hoping someone might get some fun out of it. Currently Google Gemini is free for this level of usage. In future I may try other AI tools. It would not be hard to change it out for Ollama, Claude, GPT-4o or whatever.

# Installation
1. create a new virtual environment
   > conda create -n "delver" python=3.11
   
   > conda activate delver
2. Get an API key from Google
    > https://aistudio.google.com/app/apikey
3. Install Chromadb
    > pip install chromadb
4. Install dependancies
    > pip install -r requirements.txt
5. Collect source material

    The script will import PDF, epub, txt, markdown. This is all text based so it won't work with maps, etc. I find a collection of RPG books, novels, fan fiction, etc works well. Make sure everything is all from the same world. Use a new collection name for each world. You want it to return information relevant to the specific world you are playing in.
6. Import source material to Chroma

    Edit the script to reflect the location of your source material, your collection name and your database location. For large books it may take a while to import but it should handle dozens or even hundreds of books on ordinary hardware. Embedding as all handled by Chroma making it very easy.
   > python3 importall.py
7. Set up config script

     There are a couple of example configs included. Make your own config file, one file for each world. Have AI help you write a summary of your world or write one yourself. I like to direct the output to a markdown file in Obsidian but any text reader will work, though a markdown reader will be nicer.  
8. Play game
   > python3 AISoloTTRPG.py --config config_world.py

   You will type your actions into the terminal and you can either read the response there or much nicer is to just follow the output in Obsidian. I use the plugin Admonition to make some nicer callout formatting. It helps to set up the opening scene a bit at least with a few sentences to make a hook. You can place the Intro in the markdown file you intend to output to. A couple of actual plays are included to give you an idea of how this works and the quality of the experience. They are all completely unedited. Both had a significant number of books both novels and TTRPG books loaded in as data.
