import os

def replace_text_in_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r+') as f:
                    file_content = f.read()
                    f.seek(0)
                    f.write(file_content.replace("https://raw.githubusercontent.com/TobinCavanaugh/fstr_docs/master/docs/fstr_style.css", "/fstr_style.css"))
                    f.truncate()

replace_text_in_files(".")
