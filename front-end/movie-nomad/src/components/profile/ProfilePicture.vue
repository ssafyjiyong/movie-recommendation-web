<template>
  <div class="modal fade" id="profilePicture" tabindex="-1" aria-labelledby="ProfilePictureLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="ProfilePictureLabel">프로필 사진 변경</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="change">
            <label for="image" class="form-label">이미지 업로드</label>
            <input @change="uploadFiles" class="form-control" accept="image/*" type="file" id="image">
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">취소</button>
              <button type="submit" class="btn btn-primary btn-sm">변경</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/userStore';
import { updatePicture } from '@/apis/userApi';

const userStore = useUserStore()
const profilePicture = ref([])

const uploadFiles = (event) => {
  for (let file of event.target.files) {
    profilePicture.value.push(file);
  }
};

const change = function () {
  const payload = {
    profile_pic: profilePicture.value[0],
  }
  updatePicture(userStore.userData['pk'], payload)
    .then(response => {
      location.reload()
    })
}
</script>

<style scoped>
.modal-footer {
  margin-top: 5%;
}
</style>