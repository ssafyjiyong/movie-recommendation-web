<template>
  <div>
    <h1>BarrierView</h1>
  </div>

  <div class="latest-article">
    <div v-for="article in articles" :key="article.id">
      <CommunityGridCard :article="article" />
    </div>
  </div>
</template>

<script setup>


</script>

<style scoped>
.latest-article {
  height: 1300px;
  margin-top: 20px;
  border: 1px solid black;
  border-radius: 10px;
  padding-top: 13px;

}
</style>