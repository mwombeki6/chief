# 🔱 Chief Research Platfrom(backend-API) 🚧🎯

`👋🏾  Author: Erick Mwombeki`

## ⚙️ Getting Started

### 1.🏏 First, clone the github repository below by copying the code below to your terminal

```
git clone https://github.com/mwombeki6/chief.git
```

 ⚠️ NOTE: install `python3[latest_version]` by going to the official python website and download python3 latest version from there and follow its instructions on how to install in your specific computing architecture[linux,windows or mac]

`https://www.python.org/downloads/`

### 2.📌 Create a virtual environment in the cloned project directory where you'll install all the python libraries

### 💻 In windows PC

```
# copy the code below to create a virtual environment with venv
python3 -m venv venv
# or
python -m venv venv

# then activate your virtual environment
venv\Scripts\activate
```

### 🖥️ In Linux PC

```
python3 -m venv venv

#then activate the virtual environment
source venv/bin/activate

```

### 3.🥅 install the python libraries and dependencies by installing the requirements.txt file, the file is located in within the project you cloned

```
#before| make sure that pip is installed globally in your system PC, by typing code below in your terminal
pip --version

#after| within the same virtual environment you are activated in type
pip install -r requirements.txt
```

### ⛓️4. Run the development server

```
python3 manage.py runserver
# the server will start and run on port 8000, 'http://127.0.0.1:8000/' as a default port for django
```
