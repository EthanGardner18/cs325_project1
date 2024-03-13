# This module takes the data from raw text files, then it makes them more readable
# after processing them they are stored in data/processed with the name of processed1.txt.......
# the input are the raw files and the output are the processed files
import os

class DataProcessor:
    def __init__(self):
        pass

    def read_raw_files(self, input_dir):
        raw_texts = []
        for filename in os.listdir(input_dir):
            if filename.endswith(".txt"):
                input_path = os.path.join(input_dir, filename)
                with open(input_path, "r", encoding="utf-8") as input_file:
                    raw_texts.append(input_file.read())
        return raw_texts

    def process_data(self, raw_texts):
        processed_texts = []
        for raw_text in raw_texts:
            words = raw_text.split()
            formatted_text = '\n'.join(' '.join(words[i:i+12]) for i in range(0, len(words), 15))
            processed_texts.append(formatted_text)
        return processed_texts

    def save_processed_files(self, processed_texts, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        for idx, processed_text in enumerate(processed_texts, start=1):
            output_path = os.path.join(output_dir, f"processed{idx}.txt")
            with open(output_path, "w", encoding="utf-8") as output_file:
                output_file.write(processed_text)

def formatFiles(input_dir, output_dir):
    processor = DataProcessor()
    raw_texts = processor.read_raw_files(input_dir)
    processed_texts = processor.process_data(raw_texts)
    processor.save_processed_files(processed_texts, output_dir)

