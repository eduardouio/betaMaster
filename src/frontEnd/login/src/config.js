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
        logoutUser : baseUrl + '/accounts/logout/', // GET
        registerUser : baseUrl + '/api/user/add/', // POST
    }
}

export default serverConfigData;
