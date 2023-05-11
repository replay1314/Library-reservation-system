<template lang="">
        <!-- 最外层的大盒子 -->
       <div class="box">
        <!-- 滑动盒子 -->
        <div class="pre-box">
            <h1>WELCOME</h1>
            <p>JOIN US!</p>
            <div class="img-box">
                <img src="/static/img/可莉.png" alt="">
            </div>
        </div>
        <!-- 注册盒子 -->
        <div class="register-form">
            <!-- 标题盒子 -->
            <div class="title-box">
                <h1>注册</h1>
            </div>
            <!-- 输入框盒子 -->
            <div class="input-box">
                <input type="text" placeholder="手机号" v-model="phone">
                <input type="password" placeholder="密码" v-model="password">
                <input type="password" placeholder="确认密码" v-model="repassword">
            </div>
            <!-- 按钮盒子 -->
            <div class="btn-box">
                <button @click="register()">注册</button>
                <!-- 绑定点击事件 -->
                <el-link type="primary" @click="mySwitch()">已有账号?去登录</el-link>
            </div>
        </div>
        <!-- 登录盒子 -->
        <div class="login-form">
            <!-- 标题盒子 -->
            <div class="title-box">
                <h1>登录</h1>
            </div>
            <!-- 输入框盒子 -->
            <div class="input-box">
                <input type="text" placeholder="手机号" v-model="phone">
                <input type="password" placeholder="密码" v-model="password">
            </div>
            <!-- 按钮盒子 -->
            <div class="btn-box">
                
                <button @click = "login()">登录 </button>
                <el-link type="primary" @click="mySwitch()">没有账号?去注册</el-link>
            </div>
        </div>
        <div class="edit-from">

        </div>
       </div>
</template>
<script>
import "../assets/js/login.js";
import "../assets/css/login.css";
export default {
  data() {
    return {
      phone: "",
      password: "",
      repassword: "",
      flag: true,
    };
  },
  methods: {
    login() {
    if(this.password == "" || this.phone == ""){
        this.$message.error("信息不能为空");
        return;
      }
      this.$axios({
        url: "/login",
        method: "post",
        data: {
          phone: this.phone,
          password: this.password,
        },
      }).then((response) => {
        if (response.data.code == 200) {
          this.$message({
            message: response.data.message,
            type: "success",
          });
          window.localStorage.setItem("token", response.data.token);
          window.localStorage.setItem("phone", this.phone);
          this.$router.push("/Person");
        } else {
          this.$message.error(response.data.message);
        }
      });
    },
    register() {
      if (this.password != this.repassword) {
        this.$message.error("密码不一致");
        return;
      }
      if(this.password == "" || this.repassword == "" || this.phone == ""){
        this.$message.error("信息不能为空");
        return;
      }
      this.$axios({
        url: "/register",
        method: "post",
        data: {
          phone: this.phone,
          password: this.password,
        },
      }).then((response) => {
        if (response.data.code == 200) {
          this.$message({
            message: response.data.message,
            type: "success",
          });
        } else {
          this.$message.error(response.data.message);
        }
      });
    },
    mySwitch() {
      if (this.flag) {
        $(".pre-box").css("transform", "translateX(100%)");
        $(".pre-box").css("background-color", "#c9e0ed");
        $("img").attr("src", "/static/img/胡桃.jpg");
      } else {
        $(".pre-box").css("transform", "translateX(0%)");
        $(".pre-box").css("background-color", "#edd4dc");
        $("img").attr("src", "/static/img/可莉.png");
      }
      this.flag = !this.flag;
    },
  },
};
</script>
<style lang="" scoped>
</style>