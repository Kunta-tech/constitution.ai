# Constitution.ai

There are 3 main parts-
- aid_bot
- article_hub
    - news feed
    - knowledge hub
- quiz_game

### requirements
Pip packages
```bash
pip install django python-dotenv google.generativeai markdown
```

use .env file to store Gemini API
```bash
GOOGLE_API_KEY="<your API key>"
```


### Run server
```
python manage.py runserver
```

## Store Static Files
- Store css[Here](/static/css)
- Store js[Here](/static/js)
