<template>
  <div class="text-center">
    <img :src="`https://image.tmdb.org/t/p/w500/${actor.profile_path}`" alt="img">
    <div class="text-center">
      <small>
        {{ actor.name }}
      </small>
    </div>
  </div>
</template>

<script setup>
defineProps({
  actor: Object
})
</script>

<style scoped>
img {
  object-fit: cover;
  width: 12vw;
  height: 12vw;
  border-radius: 50%;
}

</style>