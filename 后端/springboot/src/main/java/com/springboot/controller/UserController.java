package com.springboot.controller;

import com.springboot.pojo.IdCard;
import com.springboot.pojo.Res;
import com.springboot.pojo.User;
import com.springboot.service.UserService;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.Random;

@RestController
public class UserController {
    @Resource
    protected UserService userService;

    @GetMapping("/")
    public String t() {
        return "Index";
    }

    @PostMapping("/login")
    public Res login(@RequestBody IdCard idCard) {
        if (userService.login(idCard.getPhone(), idCard.getPassword()) != null) {
            String token = String.valueOf(new Random().nextDouble()) + "sss";
            return new Res(200, "登录成功", token);
        } else {
            return new Res(-1, "账号或密码错误", null);
        }
    }

    @PostMapping("/register")
    public Res register(@RequestBody IdCard idCard) {
        if (userService.findByPhone(idCard.getPhone()) == null) {
            userService.register(idCard.getPhone(), idCard.getPassword());
            return new Res(200, "注册成功", null);
        } else {
            return new Res(-1, "该账号已存在", null);
        }
    }

    @GetMapping("/detail")
    public Res detail(String phone) {
        return new Res(200, "加载成功", userService.findByPhone(phone));
    }

    @GetMapping("/changeOpen")
    public Res changeOpen(boolean flag, String phone) {
        if(userService.changeOpen(flag, phone) > 0){
            return new Res(200, "更新成功", null);
        }else{
            return new Res(-1, "更新失败", null);
        }
    }

    @PostMapping("/update")
    public Res update(@RequestBody User user) {
        if(userService.findById(user.getId(),user.getSeatNum()) != null){
            return new Res(-1, "该位置已被占", null);
        }
        User back = userService.findByPhone(user.getPhone());
        if(user.getEmail() == null){
            user.setEmail(back.getEmail());
        }
        if(user.getPassword() == null){
            user.setPassword(back.getPassword());
        }
        if(user.getId() == null){
            user.setId(back.getId());
        }
        if(user.getSeatNum() == null){
            user.setSeatNum(back.getSeatNum());
        }
        if(userService.update(user) > 0){
            return new Res(200, "更新成功", null);
        }else{
            return new Res(-1, "更新失败", null);
        }
    }


}
