# DSPy_poc

Create a virtual environment :
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Install the required dependencies in the virtual environment :
```bash
pip install -r requirements.txt
```

To use ProgramOfThought need to install Deno
For Windows (PowerShell):
```bash
irm https://deno.land/install.ps1 | iex
```
For macOS with Homebrew:
```bash
brew install deno
```
For Linux/macOS using curl:
```bash
curl -fsSL https://deno.land/install.sh | sh
```

After installation, you'll need to restart your terminal/IDE for the changes to take effect. Deno will be available in your system PATH.

To verify the installation:

deno --version


