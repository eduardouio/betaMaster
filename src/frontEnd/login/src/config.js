const csrfToken='este es el token de seguridad'
const baseUrl='http://localhost:8000'
const responseServer = {
    'response': false,
    'status': 'error',
    'message': 'Usuario o contraseña incorrectos',
}

const serverConfigData = {
    'csrfToken': csrfToken,
    'baseUrl': baseUrl,
    'headers':{
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-CSRFToken': csrfToken
    },
    'response':responseServer,
    'urls': {
        baseUrl : baseUrl,
        url_media : baseUrl + '/media/',
        loginRedirect : baseUrl + '/accounts/home/', // POST
        loginUser : baseUrl + '/accounts/login/', // POST
        registerUser : baseUrl + '/api/user/add/', // POST
        login: baseUrl + '/accounts/login/', // POST
        APILogin : baseUrl + '/api/accounts/login/', // POST
        homeRedirector: baseUrl + '/accounts/home-redirector/', // GET
    }
}

export default serverConfigData;
