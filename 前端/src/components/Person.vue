<template lang="">
       <div class="box">
        <div class="register-form">
             <div class="img-box">
                <img src="/static/img/可莉.png" alt="">
            </div>
                <h1>当前信息</h1>
<el-descriptions title="" direction="vertical" :column="3" border style = "margin:5%">
  <el-descriptions-item label="教室" >{{this.nid=="1900"?"五楼西-电子预览室":"五楼东-自习室"}}</el-descriptions-item>
  <el-descriptions-item label="座位号" >{{this.nseatNum}}</el-descriptions-item>
  <el-descriptions-item label="邮箱" >{{this.nemail}}</el-descriptions-item>
  <el-descriptions-item label="手机号" >{{this.phone}} </el-descriptions-item>
  <el-descriptions-item label="密码" >{{this.npassword}}</el-descriptions-item>
  <el-descriptions-item label="状态">
        <el-switch @change = "changeOpen()"
        v-model="flag"
        active-color="#13ce66"
        inactive-color="#ff4949">
        </el-switch>
  </el-descriptions-item>
</el-descriptions>
        </div>
        <!-- 登录盒子 -->
        <div class="login-form">
             <div class="img-box" style = "">
                <img src="/static/img/胡桃.jpg" alt="">
            </div>
            <!-- <h1>更新信息</h1> -->
            <div class="input-box">
                          <el-select v-model="id" placeholder="==选择教室==">
                        <el-option
                        v-for="item in option1s"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                </el-select>
                <el-select v-model="seatNum" placeholder="==选择座位==" v-if="id==1900">
                        <el-option
                        v-for="item in option2s"
                        :key="item"
                        :label="item"
                        :value='item'>
                        </el-option>
                </el-select>
                <el-select v-model="seatNum" placeholder="==选择座位==" v-if="id==1901">
                        <el-option
                        v-for="item in option2s"
                        :key="item"
                        :label="item"
                        :value="item"
                        >
                        </el-option>
                </el-select>
                <el-input v-model="email" placeholder="邮箱" style="width:43.5%"></el-input>
                <el-input v-model="password" placeholder="密码" style="width:43.5%"></el-input>
                      <div class="btn-box">
                        <button @click="upDate()" style="background:pink">更新信息</button>
                        </div>
                        
            </div>
        </div>
        <div class="edit-from">

        </div>
       </div>
</template>
<script>
import "@/assets/css/person.css";
export default {
  data() {
    return {
      option1s: [
        {
          value: "1900",
          label: "五楼西-电子预览室",
        },
        {
          value: "1901",
          label: "五楼东-自习室",
        },
      ],
      option2s: 180,
      option3s: 199,
      phone: "",
      flag: true,
      value: "",
      id: "",
      seatNum: 1,
      sseatNum:"",
      password: "",
      email: "",
      nid: "1900",
      nseatNum: "n",
      npassword: "n",
      nemail: "n",
    };
  },
  methods: {
    changeOpen() {
      if (this.flag == true) {
        this.$message({
          message: "打开成功",
          type: "success",
        });
      } else {
        this.$message({
          message: "关闭成功",
          type: "success",
        });
      }
      this.$axios({
        url:
          "/changeOpen?flag=" +
          this.flag +
          "&phone=" +
          window.localStorage.getItem("phone"),
        method: "get",
      });
    },
    upDate() {
      if(this.seatNum < 10){
        this.sseatNum = "00" + this.seatNum;
      }else if(this.seatNum < 100){
        this.sseatNum = "0" + this.seatNum;
      }else{
        this.sseatNum = "" + this.seatNum;
      }
      this.$axios({
        url: "/update",
        method: "post",
        data: {
          phone: this.phone,
          password: this.password,
          id: this.id,
          seatNum: this.sseatNum,
          email: this.email,
          flag: this.flag,
        },
      }).then((response) => {
        console.log(response);
        if (response.data.code == 200) {
          this.$message({
            message: response.data.message,
            type: "success",
          });
          location.reload();
        } else {
          this.$message.error(response.data.message);
        }
      });
    },
    async loadData() {
      let e = await this.$axios({
        url: "/detail?phone=" + window.localStorage.getItem("phone"),
        method: "get",
      });
      console.log(e);
      this.phone = e.data.data.phone;
      this.npassword = e.data.data.password;
      this.nid = e.data.data.id;
      this.nseatNum = e.data.data.seatNum;
      this.nemail = e.data.data.email;
      this.flag = e.data.data.flag;
    },
  },
  async created() {
    this.loadData();
  },
};
</script>
<style lang="">
</style>