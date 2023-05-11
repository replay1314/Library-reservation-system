// 配置axios相关信息

import axios from "axios";

let $axios = axios.create({
    baseURL:"http://121.36.18.179:8088",
    timeout:3000
})

// 配置拦截器
// 拦截器需要配置 axios使用 之前！
// 添加请求拦截器
$axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    return config;   // 一定要return config ，否则 请求无法成功！
}, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});

// 添加响应拦截器
$axios.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    return response;    // return 内容，否则具体的请求响应里面获取不到数据！
}, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
});

export default $axios;