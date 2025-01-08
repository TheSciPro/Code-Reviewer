# Code Reviewer POC

This is a proof of concept (POC) for a code review application built using the `microsoft/codereviewer` model. The application tokenizes code diffs and generates feedback as if a senior software engineer is reviewing their peer's code.


## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/TheSciPro/Code-Reviewer.git
cd backend
```

### 2. Install dependencies
Navigate to the backend directory and install the required Python packages.

```bash
cd backend
pip install -r requirements.txt
```

### 3. Run the application
Once the dependencies are installed, you can run the application using the following command:

```bash
python main.py
```

### 4. Enter code diff
After running the program, you will be prompted to enter the code diff. Paste the code diff into the space provided in the terminal.
```
A code diff represents the changes made between two versions of a file or set of files. Developers can generate these diffs using version control tools like Git. For instance, running git diff will provide a snapshot of code changes. Insert your generated code diff below to analyze and receive automated feedback.
```

### 5. Review response
The model will generate a response, simulating a senior software engineer reviewing the code, highlighting potential improvements, and offering feedback.

## Chatbot
![image](https://github.com/user-attachments/assets/423d00a3-6c22-405a-a308-1a1b5c720f47)

enter code diff, get it reviewed!

![image](https://github.com/user-attachments/assets/fdf9a35c-a1f0-47ee-9f35-eeee53c5bd3c)


