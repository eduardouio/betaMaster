<template>
    <div>
    <!-- component -->
    <div class="    ">
        <!-- Container -->
        <div class="container mx-auto mt-8">
            <h3 class="pt-4 text-3xl text-center text-slate-800">Registro de Usuario</h3>
            <div class="flex justify-center px-6 my-6">
                <!-- Row -->
                <div class="w-full xl:w-4/4 lg:w-12/12 flex">
                    <!-- Col -->
                    <div class="w-full h-auto bg-gray-400 hidden lg:block lg:w-5/12 bg-cover rounded-l-lg"
                        style="background-image: url('https://www.telemundo.com/sites/nbcutelemundo/files/images/promo/article/2017/05/18/estudiantes-latinos-graduados.jpg')">
                    </div>
                    <!-- Col -->
                    <div class="w-full lg:w-7/12 bg-white p-4 rounded-lg lg:rounded-l-none">
                        <form class="px-8 pt-6 pb-8 mb-4 bg-white rounded">
                            <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="firstName">
                                        Nombres:
                                    </label>
                                    <input
                                        class="input w-full max-w-xs x-input"
                                        id="firstName" type="text" placeholder="Nombres" />
                                </div>
                                <div class="mb-4 flex-1 md:ml-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="lastName">
                                        Apellidos
                                    </label>
                                    <input
                                        class="input w-full max-w-xs x-input"
                                        id="firstName" type="text" placeholder="Nombres" />
                                </div>
                            </div>
                            <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="email">
                                    Email
                                </label>
                                <input
                                    class="input w-full max-w-xs x-input"
                                    id="email" type="email" placeholder="Email" />
                                </div>
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="email">
                                    Soy
                                </label>
                                <select class="select w-full max-w-xs selected px-3  mb-3 x-input">
                                <option disabled selected>Quiero registrarme como...</option>
                                    <option>Profesor</option>
                                    <option>Estudiante</option>
                                </select>
                            </div>                                
                            </div>                                
                            <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="password">
                                        Contraseña
                                    </label>
                                    <input
                                        class="w-full px-3 py-2 mb-3 x-input"
                                        id="password" type="password" placeholder="******************" />
                                    <p class="text-xs italic text-red-500">Ingerese una Contraseña</p>
                                </div>
                                <div class="md:ml-2 flex-1">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="c_password">
                                        Confirmar
                                    </label>
                                    <input
                                        class="w-full px-3 py-2 mb-3 x-input"
                                        id="c_password" type="password" placeholder="******************" />
                                </div>
                            </div>
                            <div class="mb-6 text-center">
                                <button
                                    class="btn btn-primary"
                                    type="button">
                                    Registrar Cuenta
                                </button>
                            </div>
                            <hr class="mb-6 border-t" />
                            <div class="text-center">
                                <a class="inline-block text-md text-blue-500 align-baseline hover:text-blue-800" href="#">
                                    Recuperar contaseña?
                                </a>
                            </div>
                            <div class="text-center">
                                <a class="inline-block text-md text-blue-500 align-baseline hover:text-blue-800" href="#">
                                    Iniciar Sesión
                                </a>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>