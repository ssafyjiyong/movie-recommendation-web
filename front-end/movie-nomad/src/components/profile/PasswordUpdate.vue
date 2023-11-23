<template>
  <div class="modal fade" id="updatePassword" tabindex="-1" aria-labelledby="updatePasswordLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="updatePasswordLabel">비밀번호 변경</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitPassword">
            <label class="form-label" for="password1">비밀번호</label>
            <input id="password1" class="form-control" type="password" placeholder="비밀번호(최소 8자리)" v-model="new_password1">
            <label class="form-label" for="password2">비밀번호 확인</label>
            <input id="password2" class="form-control" type="password" placeholder="비밀번호 확인" v-model="new_password2"
              aria-describedby="passwordHelpBlock">
            <div v-show="wrong">비밀번호가 일치하지 않습니다.</div>
            <div class="modal-footer mt-3">
              <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">취소</button>
              <input type="submit" class="btn btn-success btn-sm" value="비밀번호 변경" />
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { updatePassword } from '@/apis/userApi';
import { useUserStore } from '@/stores/userStore';
import { ref, onMounted } from 'vue';
import Swal from 'sweetalert2';
import MovieDetailView from '../../views/MovieDetailView.vue';

const userStore = useUserStore()

const new_password1 = ref(null)
const new_password2 = ref(null)

const alertMessage = (msg) => {
  const result = Swal.fire({
    title: `${msg}`,
    icon: "error",
    confirmButtonColor: "#682cd48c",
    confirmButtonText: "확인",
  });
}

const submitPassword = () => {
  if (!password1.value) {
    alertMessage("비밀번호를 입력해주세요");
    return;
  }

  if (!password2.value) {
    alertMessage("비밀번호 확인을 입력해주세요");
    return;
  }

  if (password1.value.length < 8) {
    alertMessage("비밀번호가 너무 짧습니다. \n 8자리 이상 입력해주세요.");
    return;
  }

  if (password1.value !== password2.value) {
    alertMessage("비밀번호가 일치하지 않습니다");
    return;
  }

  const payload = {
    new_password1: new_password1.value,
    new_password2: new_password2.value,
  };

  updatePassword(payload)
    .then((response) => {
      Swal.fire({
        title: "비밀번호 변경 완료. \n 다시 로그인 해주세요",
        icon: "success",
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "로그인 페이지로 이동"
      })
        .then((result) => {
          if (result.isConfirmed) {
            userStore.afterUpdatePassword()
          }
        })
    })
}
</script>

<style scoped></style>