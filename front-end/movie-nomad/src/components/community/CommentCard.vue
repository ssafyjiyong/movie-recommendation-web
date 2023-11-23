<template>
  <div>

    <!-- 프로필사진, 작성자, 팔로우 -->
    <div class="mx-5 my-1">
      <span class="fw-bold">작성자　</span>
      <button class="btn btn-follow btn-sm">팔로우</button>
    </div>

    <div class="mx-4 p-2 bg-light commentBox">

    <div>
      <p class="m-0 p-2">댓글 내용 와다다다다다 막 쓰셔요 아주 막 팍팍</p>
    </div>
    <div class="d-flex justify-content-between align-items-start">
        <div>
          <button class="btn btn-light btn-sm border mx-1">답글</button>
        </div>
  
        <div>
          <button class="btn btn-outline-danger m-2 border-danger"><i class="fa-regular fa-thumbs-up"></i> 0</button>
        </div>
      </div>
  </div>
  

  </div>
  <hr>
</template>

<script setup>

</script>

<style scoped>
.commentBox {
  border-radius: 20px;
  width: 60%;
}
.btn-follow {
  background-color: #CFE2FF;
  color: #0D6EFD;
}
.btn-follow:hover {
  background-color: #0D6EFD;
  color: white;
}
</style>