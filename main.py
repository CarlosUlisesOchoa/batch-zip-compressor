import os
import pyminizip

def read_env(file_path):
    # print(f"Reading from {file_path}")
    env_vars = {}
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            env_vars[key] = value
    # print(f"Environment variables read: {env_vars}")
    return env_vars

def compress_and_protect_files(env_vars):
    # print("Inside compress_and_protect_files function.")
    input_dir = env_vars.get('INPUT_DIR')
    output_dir = env_vars.get('OUTPUT_DIR')
    password = env_vars.get('PASSWORD')
    
    if not input_dir or not output_dir or not password:
        print("Missing required environment variables.")
        return

    print(f"Input directory: {input_dir}, Output directory: {output_dir}, Password: {password}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        print(f"Compressing file: {filename}")
        input_filepath = os.path.join(input_dir, filename)
        # remove original extension from filename
        filename = os.path.splitext(filename)[0]
        output_filepath = os.path.join(output_dir, f"{filename}.zip")
        
        pyminizip.compress(input_filepath, None, output_filepath, password, int(0))

# Reading environment variables from .env file
env_file_path = ".env" 
env_vars = read_env(env_file_path)

compress_and_protect_files(env_vars)