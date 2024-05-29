<script setup>
import { CheckBadgeIcon, ExclamationCircleIcon} from "@heroicons/vue/24/outline";
import { computed } from "vue";

const props = defineProps(
    {
        message: String,
        type_message: String,
    }
);

// elegimos el tipo de mensaje
const message_class = computed(() => {
    let classes = {
        warning:'alert alert-warning',
        success:'alert alert-success',
        info:'alert alert-info',
        error:'alert alert-error',
    };

    return classes[props.type_message];
});


</script>
<template>    
<div role="alert" :class="message_class" class="text-white">
    <ExclamationCircleIcon class="h-6 w-6" v-if="type_message !== 'success'"/>
    <CheckBadgeIcon class="h-6 w-6" v-else/>
    <span class="text-start">{{ type_message.toUpperCase() }}: {{ message }}</span>
  </div>
</template>