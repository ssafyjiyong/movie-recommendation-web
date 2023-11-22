<template>
  <div>
    <img src="{{ mate.profile_pic }}" alt="">
    {{ mate.nickname }}
  </div>
</template>

<script setup>
defineProps({
  mate: Object
})
</script>

<style scoped>

</style>