<!-- 닉네임 추가해야됨 -->


<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">회원가입</h2>
        <div class="mb-3">
          <label for="nickname" class="form-label">닉네임</label>
          <input v-model="nickname" type="text" class="form-control" id="nickname" placeholder="닉네임을 정해주세요" />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">이메일</label>
          <input v-model="username" type="email" class="form-control" id="email" placeholder="name@example.com" />
        </div>
        <div class="mb-4">
          <label for="password1" class="form-label">비밀번호</label>
          <input v-model="password1" 
          type="password" 
          class="form-control" 
          id="password1" 
          placeholder="비밀번호(최소 8자리)" />
        </div>
        <div class="mb-4">
          <label for="password2" class="form-label">비밀번호 확인</label>
          <input v-model="password2" @keyup.enter="signUp" type="password" class="form-control" id="password2"
            placeholder="비밀번호 확인" />
        </div>
        <div class="d-grid mb-4">
          <button @click="signUp" class="btn fw-bold">회원가입</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/userStore";
import Swal from "sweetalert2";

// 회원 가입
const nickname = ref(null);
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const userStore = useUserStore();

const alertMessage = (msg) => {
  const result = Swal.fire({
    title: `${msg}`,
    icon: "error",
    confirmButtonColor: "#682cd48c",
    confirmButtonText: "확인",
  });
};

const signUp = () => {
  if (!nickname.value) {
    alertMessage("닉네임을 정해해주세요");
    return;
  }

  if (!username.value) {
    alertMessage("아이디를 입력해주세요");
    return;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(username.value)) {
    alertMessage("아이디는 이메일 형식이어야 합니다");
    return;
  }

  if (!password1.value) {
    alertMessage("비밀번호를 입력해주세요");
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
    nickname: nickname.value,
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };

  userStore.signUpUser(payload);
};
</script>

<style scoped>

.btn {
  border-radius: 20px;
  background-color: #7DBE3F;
  color: white;
}
</style>
