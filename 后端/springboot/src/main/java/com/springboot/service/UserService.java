package com.springboot.service;

import com.springboot.dao.UserMapper;
import com.springboot.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {
    @Autowired
    protected UserMapper userMapper;

    public List<User> findAll() {
        return userMapper.findAll();
    }

    public User login(String phone, String password) {
        return userMapper.login(phone, password);
    }

    public User findByPhone(String phone) {
        return userMapper.findByPhone(phone);
    }

    public User findById(String id,String seatNum) {
        return userMapper.findById(id,seatNum);
    }

    public void register(String phone, String password) {
        userMapper.register(phone,password);
    }

    public int changeOpen(boolean flag,String phone) {
        return userMapper.changeOpen(flag,phone);
    }

    public int update(User user) {
        return userMapper.update(user);
    }

}
