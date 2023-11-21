<template>
  <div>
    {{ actor.name }}
    <img :src="`https://image.tmdb.org/t/p/w500/${actor.profile_path}`" alt="img">
  </div>
</template>

<script setup>
defineProps({
  actor: Object
})
</script>

<style scoped>

</style>