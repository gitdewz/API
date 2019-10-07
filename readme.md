Setup:
**1. Setup Python 3.7.X, a virtual environment, and the modules**
    * Link to download Python: https://www.python.org/downloads/
    * Create a virtual environment in the project base directory
        * Virtual environment documentation: https://docs.python.org/3/tutorial/venv.html
        * Check your python version in the terminal `python -V`, if it isn't 3.7.X try `python3 -V`
        * Use `python -m venv env` or `python3 -m venv env` to create the virtual environment
            * If you name your enviornment directory something other than `env` update the gitignore
        * **Windows** -
            * Use `env\Scripts\activate.bat` to start the environment
            * Use `env\Scripts\deactivate.bat` to stop the environment
        * **MacOS / Linux** -
            * Use `source tutorial-env/bin/activate` to start the environment
            * Use  `source tutorial-env/bin/deactivate` to stop the environment
        * Install the Python modules using `python -m pip install -r requirements.txt`

**2. Start the app**
    * If the virtual environment isn't already active use the commands above to activate it
    * In the project base directory run `python app.py`
    * The API should be available at `http://localhost:5556/graphql`
