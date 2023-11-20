import feedparser
import threading
import requests


def fetch_data_and_write(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            
            content = response.text
            
                      
            filepath= r'C:\Users\nevis\OneDrive\Documents\python_projects\content\Six\output.txt'
            with open(filepath, 'a', encoding='utf-8') as file:
                file.write(content)
                print(f"Content from {link} written to {filepath}")
        else:
            print(f"Failed to fetch content from {link}")
    except Exception as e:
        print(f"Error fetching content from {link}: {e}")


def process_rss_file_with_threads(file_path):
    feed = feedparser.parse(file_path)
    
   
    threads = []
    
    for entry in feed.entries:
        link = entry.link
        
       
        thread = threading.Thread(target=fetch_data_and_write, args=(link,))
        threads.append(thread)
        thread.start()
    
  
    for thread in threads:
        thread.join()


rss_file_path = r'C:\Users\nevis\OneDrive\Documents\python_projects\content\Six\rss_file.xml'


process_rss_file_with_threads(rss_file_path)