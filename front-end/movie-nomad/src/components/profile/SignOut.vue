<template>
  <div class="modal fade" id="signOut" tabindex="-1" aria-labelledby="signOutLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5 fw-bold" id="signOutLabel">회원탈퇴</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          정말 탈퇴하시겠습니까?
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
          <button @click="doIt" type="button" class="btn btn-danger">회원탈퇴</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { signOut,  } from '@/apis/userApi';
import { useUserStore } from '@/stores/userStore';

const userStore = useUserStore()
const token = userStore.token
const nickname = userStore.nickname

const doIt = () => {
  signOut(nickname, token)
    .then(() => {
      window.alert('회원탈퇴가 완료되었습니다.')
    })
    .then((
      userStore.logout()
    ))
    .then(() => {
      location.reload()
    })

}
</script>

<style scoped></style>