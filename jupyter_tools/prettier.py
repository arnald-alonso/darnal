from bs4 import BeautifulSoup
import webbrowser
import os


def fmt_jupyter_html(input_file, output_file, remove_code_cells=True,
                     remove_warnings=True, open_output=False):
    class_code = 'input'
    class_warn = 'output_subarea output_stream output_stderr output_text'
    # Part of this code is based on:
    # https://stackoverflow.com/questions/32063985/
    # deleting-a-div-with-a-particlular-class-using-beautifulsoup
    with open(input_file, 'r') as content_file:
        content = content_file.read()
    soup = BeautifulSoup(content, "html.parser")
    if remove_code_cells:
        for div in soup.find_all("div", {'class': class_code}):
            div.decompose()
    if remove_warnings:
        for div in soup.find_all("div", {'class': class_warn}):
            div.decompose()
    with open(output_file, 'w') as content_file:
        content_file.write(str(soup))
    if open_output:
        _ = webbrowser.open('file://' + os.path.realpath(output_file))
