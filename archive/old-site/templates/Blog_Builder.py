import os
import markdown
import yaml # pip install pyyaml
from jinja2 import Environment, FileSystemLoader # pip install jinja2
import datetime

# CONFIGURATION
CONTENT_DIR = 'content'
OUTPUT_DIR = 'blog'
TEMPLATE_DIR = 'templates'

# Setup Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template('post_template.html')

def build_blog():
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Loop through all markdown files
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(CONTENT_DIR, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                raw_content = f.read()
                
            # Separate Frontmatter (YAML) from Content
            # We manually parse to avoid extra dependencies if possible, 
            # but "python-frontmatter" library is safer. 
            # For now, let's assume standard "---" split.
            parts = raw_content.split('---', 2)
            if len(parts) < 3:
                print(f"Skipping {filename}: Invalid Frontmatter format")
                continue
                
            metadata = yaml.safe_load(parts[1])
            markdown_text = parts[2]
            
            # Convert Markdown to HTML
            html_content = markdown.markdown(markdown_text, extensions=['fenced_code', 'tables'])
            
            # Calculate read time (approx 200 words per min)
            word_count = len(markdown_text.split())
            read_time = max(1, round(word_count / 200))
            
            # Render Template
            output_html = template.render(
                title=metadata.get('title', 'Untitled'),
                subtitle=metadata.get('subtitle', ''),
                description=metadata.get('description', ''),
                category=metadata.get('category', 'General'),
                author=metadata.get('author', 'Nicholas Thomas'),
                role=metadata.get('role', 'Founder'),
                date=metadata.get('date', datetime.date.today()),
                read_time=read_time,
                content_html=html_content
            )
            
            # Save HTML
            output_filename = filename.replace('.md', '.html')
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output_html)
                
            print(f"✅ Generated: {output_filename}")

if __name__ == "__main__":
    build_blog()
