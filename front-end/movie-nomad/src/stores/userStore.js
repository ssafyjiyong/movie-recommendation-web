import { ref } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import { signUp, whoIsCurrentUser, logIn, getCurrentUserInfo } from "@/apis/userApi";
import Swal from "sweetalert2";

export const useUserStore = defineStore("user", () => {
  const router = useRouter();
  const token = ref(window.localStorage.getItem("token") || "");
  const isLogin = ref(false);
  const userInfo = ref(null)
  const userData = ref({
    pk: null,
    username: "",
  });
  // const profile = ref({});
  const status = ref('상태메세지를 변경해보세요!')
  const nickname = ref("")

  const setCurrentUser = (user) => {
    userData.value.pk = user.pk;
    userData.value.username = user.username;
  };

  const signUpUser = (payload) => {
    signUp(payload).then((response) => {
      Swal.fire({
        title: "회원가입 완료. \n 로그인 하시겠습니까?",
        icon: "success",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "네",
        cancelButtonText: "아니요",
      }).then((result) => {
        if (result.isConfirmed) {
          // 네를 눌렀을 때, 자동으로 로그인되는 기능
          const loginPayload = {
            username: payload.username,
            password: payload.password1,
          };
          loginUser(loginPayload);
          router.push({ name: "home" });
        } else {
          router.push({ name: "home" });
        }
      })
    });
  };




  const loginUser = (payload) => {
    logIn(payload)
      .then((response) => {
        if (response.data.key) {
          token.value = response.data.key;
          isLogin.value = true;
          window.localStorage.setItem("token", token.value);
          fetchCurrentUser();
          router.push({ name: "home" });
        } else {
          Swal.fire({
            title: "로그인에 실패했습니다. \n 아이디와 비밀번호를 확인하세요",
            icon: "error",
            confirmButtonColor: "#682cd48c",
            confirmButtonText: "확인",
          });
        }
      })
      .catch(() => {
        Swal.fire({
          title: "로그인에 실패했습니다.\n아이디와 비밀번호를 확인하세요",
          icon: "error",
          confirmButtonColor: "#682cd48c",
          confirmButtonText: "확인",
        });
      });
  };


    const fetchCurrentUser = () => {
      if (isLogin.value) {
        whoIsCurrentUser(token.value)
          .then((res) => {
            setCurrentUser(res.data);
            window.localStorage.setItem("userPk", res.data.pk);
          })
          .then(() => {
            getCurrentUserInfo(userData.value['username'])
            .then((res) => {
              userInfo.value = res.data
              return userInfo
            })
            .then((res) => {
              nickname.value = userInfo.value['nickname']
            })
        })
        .catch((err) => {
          console.error(err);
        });
    }
  };

  const logout = () => {
    token.value = "";
    isLogin.value = false;
    userData.value = {
      pk: null,
      username: "",
    };
    nickname.value = "";
    userInfo.value = null;
    window.localStorage.removeItem("token");
    window.localStorage.removeItem("userPk");
    router.push({ name: "home" });
  };

  const afterUpdatePassword = () => {
    token.value = "";
    isLogin.value = false;
    userData.value = {
      pk: null,
      username: "",
    };
    nickname.value = "";
    userInfo.value = null;
    window.localStorage.removeItem("token");
    window.localStorage.removeItem("userPk");
    router.push({ name: "login" });
  };

  return {
    token,
    isLogin,
    userData,
    userInfo,
    setCurrentUser,
    signUpUser,
    loginUser,
    fetchCurrentUser,
    logout,
    afterUpdatePassword,
    status,
    nickname
  };
},
  { persist: true }
);