# This is the library for counting tokens
import tiktoken
# This allows interaction with the OS and file structures
from pathlib import Path
from PyPDF2 import PdfReader

model = "gpt-4"

# In it's most basic form, running this script inputs sample text into
# process_text, which then uses count_tokens as part of its output.

# This function is called in the script below. It uses the count_token
# function to return token count.
def process_text(text: str) -> dict:
    
    if not text:
        raise ValueError("No text provided for token counting")
    
    return {
        'tokens': count_tokens(text),
        'characters': len(text)
    }

# This is called by the process_text function. It counts the tokens
def count_tokens(text: str) -> int:
    # Get encoding for GPT-4
    encoding = tiktoken.encoding_for_model(model)
    
    # Encode the text and count tokens.
    token_integers = encoding.encode(text)
    return len(token_integers)


# This is the process that takes a file, reads the text
# and returns it as a variable "text"
def process_file(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Could not find file: {file_path}")
    
    # Handle PDF files
    if path.suffix.lower() == '.pdf':
        reader = PdfReader(str(path))
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    else:
        # Handle text files
        text = path.read_text(encoding='utf-8')
    
    return process_text(text)
