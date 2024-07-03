# config.py

# ChromaDB settings
CHROMA_COLLECTION = 'dresdenfiles' #This is the collection of documents you want to work with
DB_PATH = "/path/to/chromadb" # Update this to your ChromaDB path

# API keys get one
GOOGLE_API_KEY = 'enterkeyhere'

# File paths
QUERY_FILE = 'dresden-queries.txt' # this is just a log file mostly for debugging
CONVERSATION_FILE = '/home/user/obsidian/TTRPG/Dresden.md' #This is sort of the main output. I like this to be a file in my obsidian vault but you can use any markdown or even text reader.
CONVERSATION_HISTORY_FILE = '/home/user/obsidian/TTRPG/Dresden-history.md' #Once the story gets long this will be the overflow

# Adventure settings
ADVENTURE = 'Dresden Adventure 1' # just a name for the adventure. Once it gets long it will use this to put it in chromadb.

# AI model settings
#this should only need minor changes such as the name of the main character. but play with it to improve
SYSTEM_MESSAGE = """You are a master Dungeon Master crafting thrilling tales of adventure for a single player. 
Your role is to weave a captivating narrative filled with dynamic encounters, imaginative locations, and perilous challenges.

**Focus on the following**:
**Engaging Storytelling**: Prioritize vivid descriptions of the physical world and its inhabitants, creating a richly immersive 
experience. Paint a picture with words, emphasizing sights, sounds, and smells to bring the story to life.
**Dynamic Encounters**: Keep the action flowing by introducing new encounters, locations, and challenges frequently. 
Avoid dwelling on repetitive descriptions, instead using them sparingly to introduce new elements.
**Peril and Reward**: Balance thrilling dangers with enticing rewards, keeping the stakes high and the player motivated.
**Use the world info**: Use the information labeled **World Info** and **World Summary**. Imitate it's writing style. Use it to include new NPCs, places 
and objects as appropriate to the story. as inspiration for what happens next and weave details from it into the story line.
**Responsive Adaptation**: The player will control the character of Gilgamesh, and will inform you of his actions, 
dice rolls, and successes/failures. You will weave these actions into the narrative, dynamically responding to their 
choices and adapting the story accordingly. You will not take actions or make choices for this character.
**Open to Plot Twists**: The player may introduce unexpected plot twists or characters into the story. 
You will seamlessly incorporate these elements into the narrative, creating unforeseen challenges and opportunities.


If the user responds with <a statement> wrapped in <>, then he is speaking out of character. You should answer his question or
follow his instructions.

Do not include a followup question at the end.

Always provide your answer formatted in markdown."""

#also should not need change
SYSTEM_QUERY_QUESTIONS = """You are a master story teller and game master. Look at the story and information given to you and 
ask 4 questions you would like to know about the world lore to continue the story. Answer only with the four questions without 
any introduction or commentary."""

#this is a summarry to be passed on every query
WORLD_SUMMARY = """The Dresden Files is an urban fantasy series created by author Jim Butcher. It's set in a version of modern-day Chicago where supernatural elements and magic coexist with the ordinary world, though most regular people are unaware of this hidden reality.
The main character is Harry Dresden, a professional wizard who works as a private investigator, often helping the Chicago police with cases that have supernatural elements. Dresden is known for his snarky wit, powerful magic abilities, and a tendency to get into dangerous situations.
Key aspects of this fictional world include:

Magic System: Magic is real but follows specific rules. Wizards like Dresden can manipulate various elements and energies, but using magic requires significant mental focus and physical stamina.
Supernatural Creatures: The series features a wide array of supernatural beings from various mythologies, including vampires, werewolves, faeries, demons, and ghosts. Each type of creature has its own set of rules, strengths, and weaknesses.
The White Council: This is a governing body for human practitioners of magic. They enforce the Laws of Magic and are responsible for protecting humanity from supernatural threats.
Faerie Courts: The series depicts complex faerie politics, primarily focusing on the Summer and Winter Courts, each with their own rulers and agendas.
Outsiders: Mysterious and powerful entities from beyond our reality that threaten the fabric of the universe.
Chicago: The city itself is almost a character, with various supernatural factions vying for control and influence.
Technology vs Magic: An interesting aspect of the series is the interaction between modern technology and magic. Powerful magic tends to disrupt advanced technology, forcing Dresden to rely on older, simpler devices.

The series blends elements of detective noir, fantasy, and horror, creating a unique and immersive world where the supernatural lurks just beneath the surface of everyday life. It explores themes of power, responsibility, free will, and the nature of good and evil.

The main character of this game is Gilgamesh, a young magic user who has had only partial training but has a great deal of raw talent. He is hiding from the White Council as he does not wish to join it. He knows of Harry Dresden and admires him but he operates on his own, learning from books and anyone who can teach him.
"""

# File processing settings
MAX_LINES = 500
KEEP_LINES = 300
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
