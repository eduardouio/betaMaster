<template>
    <table class="table table-xs">
        <!-- head -->
        <thead class="text-gray-600">
            <tr>
                <th>#</th>
                <th>Emisor</th>
                <th>Tipo</th>
                <th>Contacto</th>
                <th>Estado</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(exp, idx) in userData.references" :key="exp">
                <td>{{ idx + 1 }}</td>
                <td>{{ exp.enterprise }}</td>
                <td>{{ exp.type }}</td>
                <td>{{ exp.name_contact }}</td>
                <td nowrap>
                    <span class="flex gap-2">
                        <CheckIcon v-if="exp.is_verified" class="w-5 h-5 text-success" />
                        <XCircleIcon v-else class="w-5 h-5 text-error" />
                        <span v-if="exp.is_verified">Verificado</span>
                        <span v-else>Pendiente</span>
                    </span>
                </td>
                <td>
                    <span class="flex items-center gap-2">
                        <PencilSquareIcon class="w-5 h-5 text-primary" />
                        <XMarkIcon class="w-5 h-5 text-error" />
                    </span>
                </td>
            </tr>
        </tbody>
    </table>
</template>
<script setup>


const props = defineProps({
    references: Object,
    
})

</script>