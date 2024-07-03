# config.py

# ChromaDB settings
CHROMA_COLLECTION = 'startrek' #This is the collection of documents you want to work with
DB_PATH = "/path/to/chromadb" # Update this to your ChromaDB path

# API keys get one
GOOGLE_API_KEY = 'enterkeyhere'

# File paths
QUERY_FILE = 'startrek-queries.txt' # this is just a log file mostly for debugging
CONVERSATION_FILE = '/home/user/obsidian/TTRPG/StarTrek.md' #This is sort of the main output. I like this to be a file in my obsidian vault but you can use any markdown or even text reader.
CONVERSATION_HISTORY_FILE = '/home/user/obsidian/TTRPG/StarTrek-history.md' #Once the story gets long this will be the overflow

# Adventure settings
ADVENTURE = 'Star Trek Adventure 1' # just a name for the adventure. Once it gets long it will use this to put it in chromadb.

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
WORLD_SUMMARY = """Captain Gilgamesh (Commanding Officer): a brilliant but unconventional starship captain. He has a reputation for being a maverick, often bending the rules to achieve his goals. However, he is also a highly effective leader with a deep understanding of Starfleet protocols and procedures. He has a talent for inspiring his crew to achieve the impossible. He has a dry wit and is known to make sarcastic remarks, even in tense situations. His somewhat unorthodox approach to problem solving, often seen by superiors as a disregard for regulations and protocol, is tempered by consistently successful outcomes. He is particularly adept at identifying the talents of his crew and finding ways to use them to their fullest potential.
Backstory: Gilgamesh was raised on a series of starbases and starships, his parents both high-ranking Starfleet officers. As a child, he spent countless hours exploring the inner workings of starships and starbases, developing a deep fascination with starship design. He excelled at Starfleet Academy, graduating top of his class. He chose to specialize in Conn, demonstrating exceptional skills as a pilot. During his early career, he served as a conn officer on several starships, quickly earning a reputation for his piloting skills and his ability to remain calm under pressure.
Personality Quirks and Backstory Details:
Saval always carries a small, worn copy of "The Canterbury Tales" with him, a memento from his grandmother, a noted Shakespearean scholar who instilled in him a love of literature and history.
He is fiercely loyal to his crew and would risk his own life for theirs without hesitation.


Bridge Crew of the Starship Atlantis
The most important crew members on a starship are the Player Characters.
Commander T'Lin (Science Officer and Executive Officer): T'Lin is a tall Vulcan woman with the characteristic pointed ears and stoic expression of her species. She typically wears a standard Starfleet uniform. She is highly logical and prefers to make decisions based on data and analysis. She has a dry wit and occasionally makes sarcastic remarks, though her tone rarely betrays her amusement.
Lieutenant Saavik (Helm): Saavik, also Vulcan, is a young woman early in her Starfleet career. Her short, dark hair is usually styled in a severe manner. Like T'Lin, she prefers standard Starfleet uniforms. Despite her youth, Saavik is an excellent pilot. She has a calm demeanor and rarely speaks unless she has something relevant to contribute.
Lieutenant Junior Grade Vagh (Navigator): Vagh is a boisterous Klingon eager to prove himself. He is a skilled warrior and sometimes struggles to adapt to the strictness of Starfleet protocols. He frequently clashes with Saavik, whom he sees as overly cautious.
Ensign Josephs (Tactical and Security Oversight): Josephs is a quiet, unassuming human. He prefers to observe situations carefully before taking action. Josephs is highly intelligent and excels at tactical analysis, but he is sometimes overwhelmed by the responsibility of his position.
Ensign K'Rat (Sensor Operations): K'Rat is an Andorian distinguished by his blue skin and white hair. He is fascinated by new technologies and frequently tinkers with his own personal equipment.
Crewman Zarn (Internal Systems): Zarn is a Tellarite known for being argumentative. He enjoys debating even insignificant details. Zarn is a valuable asset to the crew due to his attention to detail and thoroughness.
Crewman T'Pring (Communications): T'Pring is a Vulcan. She is engaged to her childhood friend, Stonn.

Starship Description
Name: U.S.S. Atlantis (NCC-72175)
Class: Oberth-Class
Mission Profile: Scientific Research
Traits:
Federation Starship
Prototype: The U.S.S. Atlantis is the first of a new generation of Oberth-class starships, designed to be more efficient and have a smaller crew complement than its predecessors.
Rugged Design: The ship is built to withstand the rigors of deep space exploration, making it more resilient to damage.
Description:
The U.S.S. Atlantis (NCC-72175) is a prototype starship, representing a significant redesign of the Oberth-class for scientific research. While retaining the classic saucer-shaped primary hull, the Atlantis features redesigned warp nacelles for increased efficiency and a compact engineering section. Its secondary hull, housing the deflector array and sensor systems, is slung below the primary hull and connected by two thin pylons. This unique design minimizes resource requirements while maximizing scientific capabilities.
Key Locations:
Stellar Cartography Lab: Equipped with advanced holographic projectors and analytical tools for recording, classifying, and tracking stellar phenomena.
Recreation Lounge: A spacious lounge where the crew can unwind and socialize after shifts, featuring a bar/restaurant area.
Cargo Bays: Dedicated cargo bays with transporter facilities for transporting scientific equipment, supplies, and research specimens. Transporters are typically set to transport non-life-forms for security reasons.
Crew:
The U.S.S. Atlantis has a crew of approximately 100, a smaller complement than earlier Oberth-class vessels due to its efficient design. The crew is composed of a diverse range of specialists with expertise in various scientific disciplines, engineering, and operations.
Mission:
The U.S.S. Atlantis is tasked with exploring the Shackleton Expanse, a region of space teeming with uncharted systems and scientific anomalies. The ship's mission includes charting new star systems, studying unusual spatial phenomena, and making contact with new lifeforms. Their research contributes to the Federation's understanding of the galaxy and advances scientific knowledge.
"""

# File processing settings
MAX_LINES = 500
KEEP_LINES = 300
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
