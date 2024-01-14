// Archivo de incialización de variables globales
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const serverConfigData = {
    'base_url': 'http://localhost:8000',
    'api_url': '/api',
    'login_url': '/login/',
    'logout_url': '/logout/',
    'register_url': '/register/',
    'user_url': '/user/',
    'csrfToken': csrfToken,
    'headers':{
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-CSRFToken': csrfToken
    },
}