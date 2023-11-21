import axios from "axios";
import Swal from "sweetalert2";

const API_URL = "http://127.0.0.1:8000";

// 회원가입
export const signUp = (payload) => {
  return axios
    .post(`${API_URL}/accounts/signup/`, payload)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      if (error.response && error.response.data) {
        const errorData = error.response.data;
        let errorMessage = "";

        Object.values(errorData).forEach((messages) => {
          const translatedMessages = messages
            .map(translateMessage)
            .filter(Boolean);
          errorMessage += `${translatedMessages.join(", ")}<br>`;
        });

        if (errorMessage) {
          Swal.fire({
            title: "회원가입 에러",
            html: errorMessage,
            icon: "error",
            confirmButtonColor: "#682cd48c",
            confirmButtonText: "확인",
          });
        }
      } else {
        console.error("알 수 없는 에러가 발생했습니다.", error);
      }
    });
};

// 오류 번역을 위한 함수(회원가입 쪽에 들어감)
const translateMessage = (message) => {
  const translations = {
    "User with this username already exists.": "이미 존재하는 아이디입니다.",
    "This password is too common.": "비밀번호가 너무 단순합니다.",
  };
  return translations[message] || "";
};

// 로그인
export const logIn = (payload) => {
  return axios
    .post(`${API_URL}/accounts/login/`, payload)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("로그인, API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};

// 로그아웃
export const logOut = () => {
  return axios
    .post(`${API_URL}/accounts/logout/`)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("로그아웃, API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};

// 현재 사용자 정보 조회
export const whoIsCurrentUser = (token) => {
  return axios
    .get(`${API_URL}/accounts/user/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("현재 사용자 정보 조회, API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};


// 현재 사용자 닉네임 조회
export const getCurrentUserInfo = (username) => {
  return axios
    .get(`http://127.0.0.1:8000/myblog/${username}/`)
}

// 특정 유저 정보 조회
export const userProfile = (userName) => {
  return axios
    .get(`${API_URL}/profile/${userName}/`)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("유저 정보 조회, API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};

// 팔로우, 언팔로우
export const following = (token, nickname) => {
  return axios
    .post(
      `${API_URL}/myblog/${nickname}/following/`,
      {},
      {
        headers: {
          Authorization: `Token ${token}`,
        }
      }
    )
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("팔로우, API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};

// 프로필 변경 api
export const profileUpdate = (userPk, payload) => {
  const token = window.localStorage.getItem("token");

  return axios
    .put(`${API_URL}/profile/${userPk}/profileupdate/`, payload, {
      headers: {
        "Content-Type": "multipart/form-data",
        Authorization: `Token ${token}`,
      },
    })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      console.error("API 요청 중 에러가 발생했습니다:", error);
      throw error;
    });
};
