To create a website that shows the current weather in Stockholm, we will use the following technologies:

- Python for the backend
- Flask as the web framework
- OpenWeatherMap API for fetching the weather data (it requires an API key, but it's free)
- HTML and CSS for the frontend

Let's start by laying out the core files and their purposes:

1. `app.py`: The main entry point of the application, containing the Flask app setup and routes.
2. `weather.py`: A module to fetch the weather data from the OpenWeatherMap API.
3. `templates/index.html`: The HTML template for the main page displaying the weather.
4. `static/css/main.css`: The CSS file for styling the main page.
5. `requirements.txt`: The list of Python dependencies for the project.

Now, let's create the content of each file.

app.py
