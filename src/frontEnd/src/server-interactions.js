import serverConfigData from '@/config.js';


const  serverInteractions = {
    async getData(url) {
        let response = await fetch(url, {
            method: 'GET',
            headers: serverConfigData.headers,
        });
        if (response.status != 200) {
            let response_fail = await response.text();
            return {
                status: {
                    is_success: false,
                    message: 'Error al obtener la informacion, error en el servidor',
                    url: url,
                    response: response_fail,
                },
                response: null,
            }
        } else {
            let response_success = await response.json();
            return {
                status:{
                    is_success: true,
                    message: 'Informacion obtenida con exito',
                    url: url,
                    response: null,
                },
                response: response_success,
            };
        }
    },
    async postData(url, data) {
        let response = await fetch(url, {
            method: 'POST',
            headers: serverConfigData.headers,
            body: JSON.stringify(data),
        });
        if (response.status != 200) {
            let response_fail = await response.text();
            return {
                status: {
                    is_success: false,
                    message: 'Error al enviar la informacion, error en el servidor',
                    url: url,
                    response: response_fail,
                },
                response: null,
            }
        } else {
            let response_success = await response.json();
            return {
                status:{
                    is_success: true,
                    message: 'Informacion enviada con exito',
                    url: url,
                    response: null,
                },
                response: response_success,
            };
        }
    },
    async postFile(url, formData) {
        let headers = serverConfigData.headersFiles;
        let response = await fetch(url,{
            method: 'POST',
            headers: headers,
            body: formData,
        });

        if(response.status != 201){
            let response_fail = await response.json();
            return {
                status: {
                    is_success: false,
                    message: 'Error al enviar la informacion, error en el servidor',
                    url: url,
                    response: response_fail,
                },
                response: null,
            }
        }else{
            let response_success = await response.json();
            return {
                status:{
                    is_success: true,
                    message: 'Informacion enviada con exito',
                    url: url,
                    response: null,
                },
                response: response_success,
            };
        }



    },
    async putData(url, data){
        let response = await fetch(url, {
            method: 'PUT',
            headers: serverConfigData.headers,
            body: JSON.stringify(data),
        });
        if (response.status != 200) {
            let response_fail = await response.text();
            return {
                status: {
                    is_success: false,
                    message: 'Error al enviar la informacion, error en el servidor',
                    url: url,
                    response: JSON.parse(response_fail),
                },
                response: null,
            }
        } else {
            let response_success = await response.json();
            return {
                status:{
                    is_success: true,
                    message: 'Informacion enviada con exito',
                    url: url,
                    response: null,
                },
                response: response_success,
            };
        }
    },
    async deleteData(url) {
        let response = await fetch(url, {
            method: 'DELETE',
            headers: serverConfigData.headers,
        });
        if (response.status != 200) {
            let response_fail = await response.text();
            return {
                status: {
                    is_success: false,
                    message: 'Error al eliminar la informacion, error en el servidor',
                    url: url,
                    response: response_fail,
                },
                response: null,
            }
        } else {
            let response_success = await response.json();
            return {
                status:{
                    is_success: true,
                    message: 'Informacion eliminada con exito',
                    url: url,
                    response: null,
                },
                response: response_success,
            };
        }
    },
};

export default serverInteractions;