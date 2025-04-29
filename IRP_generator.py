import os
import json

def create_empty_notebook(file_path):
    notebook_content = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

    with open(file_path, "w") as notebook_file:
        json.dump(notebook_content, notebook_file)

def create_paper_template(repo_name):
    # Create GitHub repository name
    os.system(f'git init {repo_name}')
    os.chdir(repo_name)

    # Create directories for sections
    sections = ['Abstract','Introduction', 'Methods', 'Results', 'Discussion', 'Conclusion', 'Appendix', 'References']
    for section in sections:
        os.mkdir(section)
        create_empty_notebook(f'{section}/{section}.ipynb')

    # Create directory for data
    os.mkdir('data')
    with open('data/README.md', 'w'):
        pass

    with open('README.md', 'w') as readme:
        readme.write(f'# {repo_name}\n\nReplace this text with your IRP description.')

    # Create .gitignore file
    with open('.gitignore', 'w') as gitignore:
        gitignore.write('# Ignore Jupyter notebook checkpoints\n.ipynb_checkpoints/\n\n# Ignore data files\nData/*')

    licenses = ['LICENSE', 'LICENSE.txt']
    for license_file in licenses:
        with open(license_file, 'w') as license:
            license.write('Copyright (c) [2024] [Your Name]\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n')

    # Create a template notebook as TOC
            
    template_notebook_content = {
        
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Project Title\n",
                    "\n",
                    "This Jupyter notebook serves as a template to link all sections of your scientific paper.\n",
                    "\n",
                    "### Table of Contents\n"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.7.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    
    for section in sections:
        template_notebook_content["cells"].append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"* [{section}](./{section}/{section}.ipynb)\n"]
        })
    
    with open("Paper_Template.ipynb", "w") as template_notebook:
        json.dump(template_notebook_content, template_notebook)


if __name__ == "__main__":
    repo_name = input("Enter the name of your IRP Github repository: ")
    create_paper_template(repo_name)
