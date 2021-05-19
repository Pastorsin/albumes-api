# Álbumes-api
API for managing natural disasters albums

## Features
- Create and view your personal albums of interviews on natural disasters to raise awareness
- View interviews of natural disasters

## Getting Started

### Official website
[Visit](https://albumes-api.herokuapp.com/) the site and start!

### API Documentation
[Docs homepage](https://albumes-api.herokuapp.com/)

### Other sites
Follow Cat Facts on [Twitter](https://twitter.com/datos_de_gatos)

Talk to the DialogFlow bot [here](https://bot.dialogflow.com/d7b47381-1453-4b31-a20c-9825de80cf88)

### Setup
If you want to set up your own version of Álbumes API, follow the instructions below:
1. Clone the repository
   ```bash
   git clone https://github.com/Pastorsin/albumes-api.git
   cd albumes-api
   ```

2. Create a virtualenv
   ```bash
   virtualenv -p python3 venv
   source venv/bin/activate
   ```

3. Install requirements
   ```bash
   pip3 install -r requirements
   ```

4. Make migrations
   ```bash
   python3 manage.py migrate
   ```

5. Define the follow enviroments variables:
   ```bash
   export SECRET_KEY="secret_key"   
   export DEBUG=True
   ```

6. Run server
   ```bash
   python3 manage.py runserver
   ```
