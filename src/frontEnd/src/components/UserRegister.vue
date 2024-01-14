<template>
    <div>
    <!-- component -->
    <div class="">
        <!-- Container -->
        <div class="container mx-auto mt-4">
            <h5 class="p-1 text-center text-cyan-900 bg-gradient-to-r from-gray-100  to-slate-100 border">REGISTRO DE USUARIO</h5>
            <div class="flex justify-center px-6 my-6">
                <!-- Row -->
                <div class="w-full flex flex-col md:flex-row rounded-l-lg xl:w-4/4 lg:w-12/12">
                    <!-- Col -->
                    <div class="w-full h-auto bg-gray-400 lg:block lg:w-5/12 rounded-l-lg sm:rounded-r-lg">
                        <img src="../assets/form-registro.jpg" class="object-cover w-full h-full rounded-l-lg sm:rounded-r-lg" alt="">
                    </div>
                    <!-- Col -->
                    <div class="w-full lg:w-7/12 bg-white rounded-lg lg:rounded-l-none">
                        <form class="px-8 pt-6 pb-8 mb-4 rounded">
                            <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="firstName">
                                        Nombres:
                                    </label>
                                    <input
                                        class="my-input w-full max-w-xs x-input"
                                        id="firstName" type="text" placeholder="Nombres" />
                                </div>
                                <div class="mb-4 flex-1 md:ml-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="lastName">
                                        Apellidos
                                    </label>
                                    <input
                                        class="my-input w-full max-w-xs x-input"
                                        id="firstName" type="text" placeholder="Nombres" />
                                </div>
                            </div>
                            <div class="mb-4 flex flex-col lg:flex-row xl:flex-row">
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="email">
                                    Email
                                </label>
                                <input
                                    class="my-input w-full max-w-xs x-input"
                                    id="email" type="email" placeholder="Email" />
                                </div>
                                <div class="mb-4 flex-1 md:mr-2 md:mb-0">
                                    <label class="block mb-2 text-sm font-bold text-gray-700" for="email">
                                    Soy
                                </label>
                                <select class="select w-full max-w-xs selected px-3  mb-3 x-input" name="rol">
                                <option disabled selected>Quiero registrarme como...</option>
                                    <option value="teacher">Profesor</option>
                                    <option value="student">Estudiante</option>
                                    <option value="school">Colegio</option>
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