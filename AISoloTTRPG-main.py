import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as genai
import os
from datetime import datetime
import argparse
import importlib.util

def load_config(config_path):
    spec = importlib.util.spec_from_file_location("config", config_path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config

def setup_chroma_client(db_path, collection_name):
    client = chromadb.PersistentClient(path=db_path)
    collection = client.get_collection(collection_name)
    return collection

def query_chroma(collection, query, n_results=10):
    embedding_func = embedding_functions.DefaultEmbeddingFunction()
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )
    return results

def setup_gemini(model_name, system_instruction, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name=model_name, safety_settings=None, system_instruction=system_instruction)
    return model

def query_gemini(model, context, question):
    prompt = f"""**World Info**\n{context}\n\n{question}"""
    response = model.generate_content(prompt)
    return response.text

def log_full_query(query, context, query_file):
    with open(query_file, 'a') as f:
        f.write(f"--- Query at {datetime.now()} ---\n")
        f.write(f"Question: {query}\n")
        f.write(f"Context:\n{context}\n\n")

def log_conversation(question, answer, conversation_file):
    with open(conversation_file, 'a') as f:
        f.write(f"---\nConversation at {datetime.now()} \n---\n")
        f.write(f"> [!Player]\n{question}\n\n")
        f.write(f"Game Master: {answer}\n\n")

def read_last_lines(filename, n_lines):
    try:
        with open(filename, 'r') as file:
            all_lines = file.readlines()
            last_lines = all_lines[-n_lines:]
            history = '\n\n**Conversation History**\n\n' + ''.join(last_lines)
            return history
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def chunk_text(text, chunk_size, chunk_overlap):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def trim_file(collection, input_file, output_file, max_lines, keep_lines, chunk_size, chunk_overlap, adventure):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    if len(lines) > max_lines:
        lines_to_keep = lines[-keep_lines:]
        lines_to_move = lines[:-keep_lines]

        with open(input_file, 'w') as f:
            f.writelines(lines_to_keep)

        mode = 'a' if os.path.exists(output_file) else 'w'
        with open(output_file, mode) as f:
            f.writelines(lines_to_move)

        chunks = chunk_text(''.join(lines_to_move), chunk_size, chunk_overlap)
        
        print('Inserting answer into DB\n')

        for i, chunk in enumerate(chunks):
            unique = f"{datetime.now()}_[{i}]"
            collection.add(
                documents=[chunk],
                metadatas=[{"source": adventure, "chunk": unique}],
                ids=[f"{adventure}_chunk_{unique}"]
            )
        
        print(f"Processed history file")
        print(f"Moved {len(lines_to_move)} lines from {input_file} to {output_file}")
    else:
        print(f"{input_file} has {len(lines)} lines, no action needed")

def main(config):
    collection = setup_chroma_client(config.DB_PATH, config.CHROMA_COLLECTION)
    gemini_model = setup_gemini('gemini-1.5-pro', config.SYSTEM_MESSAGE, config.GOOGLE_API_KEY)
    gemini_model_questions = setup_gemini('gemini-1.5-flash', config.SYSTEM_QUERY_QUESTIONS, config.GOOGLE_API_KEY)
    
    while True:
        query = input("\nWhat now? (or 'quit'): ")
        if query.lower() == 'quit':
            break
        if query.lower() == 'forget':
            history = ''

        history = '\n\n**The Story so far**\n\n'
        history += read_last_lines(config.CONVERSATION_FILE, 500)
        history_query = history + '\n\n' + query

        questions = query_gemini(gemini_model_questions, config.WORLD_SUMMARY, history_query)

        print(questions)

        results = query_chroma(collection, questions)
        
        context = "\n\n".join([doc for doc in results['documents'][0]])
        
        log_full_query(query, context, config.QUERY_FILE)
        
        context_summary = context + f"\n\n**World Summary**\n{config.WORLD_SUMMARY}\n\n"

        answer = query_gemini(gemini_model, context_summary, history_query)
        
        log_conversation(query, answer, config.CONVERSATION_FILE)
        
        print("\nGemini's answer:")
        print(answer)

        trim_file(collection, config.CONVERSATION_FILE, config.CONVERSATION_HISTORY_FILE, 
                  config.MAX_LINES, config.KEEP_LINES, config.CHUNK_SIZE, config.CHUNK_OVERLAP, config.ADVENTURE)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the AI-powered storytelling system.")
    parser.add_argument("--config", default="config.py", help="Path to the configuration file")
    args = parser.parse_args()

    config = load_config(args.config)
    main(config)